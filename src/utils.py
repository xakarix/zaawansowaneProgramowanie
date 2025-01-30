import os 
import glob
import cv2
from PIL import Image
import requests
import numpy as np
from io import BytesIO


def load_image_from_path(image_path):
    if not os.path.exists(image_path):
        raise ValueError(f"Plik {image_path} nie istnieje.")
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Nie udało się załadować obrazu z podanej ścieżki: {image_path}")
    return image




def save_to_folder(output_folder, image_path, num_people):
    os.makedirs(output_folder, exist_ok=True)
    image_extension = 'png'

    original_name = os.path.splitext(os.path.basename(image_path))[0]
    new_file_name = f"{original_name}_{num_people}.{image_extension}"
    output_path = os.path.join(output_folder, new_file_name)

    cv2.imwrite(output_path, image_to_save)
    print(f"Zapisano obraz: {output_path}, liczba osób: {num_people}")

