from flask import Flask, render_template, request, jsonify, send_from_directory
import tensorflow as tf
import cv2
import os
import shutil
import requests
from db_manager import pending_tasks, in_progress_tasks, done_tasks, get_task
from queue_manager import add_to_queue
from datetime import datetime

app = Flask(__name__)

app = Flask(__name__, template_folder="../templates", static_folder="../static")
IMAGE_FOLDER = '../images'
app.config['UPLOAD_FOLDER'] = IMAGE_FOLDER
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route("/")
def upload_form():
    return render_template("index.html")

@app.route("/fetch-path", methods=["GET"])
def fetch_path():
    image_path = request.args.get('image_path')
    if not image_path:
        return jsonify({"error": "No 'image_path' provided"}), 400
    
    if not os.path.exists(image_path):
        return jsonify({"error": "Ścieżka do obrazu nie istnieje"}), 400


    if allowed_file(image_path):
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        file_name = f"{timestamp}.jpg"

        # Nowa ścieżka do pliku
        new_image_path = os.path.join(IMAGE_FOLDER, file_name)

        # Kopiujemy obraz do folderu
        shutil.copy(image_path, new_image_path)
    else:
        return jsonify({"error": "Niedozwolony format pliku"}), 400

    full_image_path = os.path.abspath(new_image_path)

    task_id = add_to_queue(image_path=full_image_path)

    return jsonify({"message": "Obraz przesłany i zadanie dodane do kolejki"})
  
    add_to_queue(image_id=image_id, image_path=image_path)

    return jsonify({"message": "Image path processed successfully", "image_id": image_id})



#Endpoint 2 URL
@app.route("/fetch-url", methods=["GET"])
def fetch_url():
    image_url = request.args.get("url")
    if not image_url:
        return jsonify({"error": "Not found url"}), 400

    try:
        response = requests.get(image_url, stream=True)
        response.raise_for_status()  # Sprawdzenie czy odpowiedź zakończyła się sukcesem

        content_type = response.headers.get("Content-Type", "").lower()
        if content_type not in ["image/png", "image/jpeg", "image/jpg"]:
            return jsonify({"error": "Niedozwolony typ pliku"}), 400

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        file_extension = ".jpg" if "jpeg" in content_type else ".png"
        file_name = f"{timestamp}{file_extension}"
        image_path = os.path.join(IMAGE_FOLDER, file_name)

        with open(image_path, "wb") as f:
            shutil.copyfileobj(response.raw, f)

        task_id = add_to_queue(image_path=image_path)

        return jsonify({
            "message": "Obraz został pobrany i zadanie dodane do kolejki",
            "task_id": task_id,
            "image_path": image_path
        })

    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Nie udało się pobrać obrazu", "details": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Wystąpił błąd: {str(e)}"}), 500


#Endpoint 3 metoda POST
@app.route("/fetch_multiple", methods=["POST"])
def fetch_multiple():
    if "images" not in request.files:
        return jsonify({"error": "Brak przesłanych obrazów"}), 400

    files = request.files.getlist("images")
    if not files:
        return jsonify({"error": "Nie przesłano żadnych plików"}), 400

    saved_files = []
    for file in files:
        if file and allowed_file(file.filename):
            try:
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                file_extension = os.path.splitext(file.filename)[1].lower()
                file_name = f"{timestamp}_{file.filename}"
                file_path = os.path.join(IMAGE_FOLDER, file_name)

                file.save(file_path)

                task_id = add_to_queue(image_path=file_path)

                saved_files.append({
                    "file_name": file_name,
                    "file_path": file_path,
                    "task_id": task_id
                })
            except Exception as e:
                return jsonify({"error": f"Błąd podczas przetwarzania pliku {file.filename}: {str(e)}"}), 500
        else:
            return jsonify({"error": f"Plik {file.filename} ma niedozwolony format"}), 400

    return jsonify({
        "message": "Pliki zostały pomyślnie przesłane i dodane do kolejki",
        "files": saved_files
    }), 200




if __name__ == "__main__":
    app.run(debug=True)
