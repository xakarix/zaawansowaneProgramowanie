import tensorflow as tf 
import numpy as np 
import cv2
import os
from utils import load_image_from_path
from image_utils import draw_boxes 

OUTPUT_FOLDER = "../processed_images"
MODEL_PATH = "/Users/aleksandraspyra/Downloads/ssd_mobilenet_v2_coco_2018_03_29/saved_model"
model = tf.saved_model.load(MODEL_PATH)
model_fn = model.signatures['serving_default']


def detect_people_from_path(image_path):
    image = load_image_from_path(image_path) 
    return person_detection(image, image_path) 

def person_detection(image, image_path): 
    # Przetwarzanie obrazu
    input_tensor = tf.convert_to_tensor(image)
    input_tensor = input_tensor[tf.newaxis, ...]

    # Detekcja
    detections = model_fn(input_tensor)

    boxes = detections['detection_boxes'][0].numpy()
    scores = detections['detection_scores'][0].numpy()
    num_people_detected = len([score for score in scores if score > 0.5])

    processed_image = draw_boxes(image, boxes, scores)

    output_image_path = os.path.join(OUTPUT_FOLDER, f"processed_{os.path.basename(image_path)}")  
    cv2.imwrite(output_image_path, processed_image)

    return num_people_detected

