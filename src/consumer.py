import pika
import json
from detector import detect_people_from_path  
import os
from db_manager import update_task 

def callback(ch, method, properties, body):
    message = json.loads(body)
    task_id = message['task_id']
    image_path = message['image_path']

    update_task(task_id, status='in_progress', people_count=0)

    print(f"Now consuming: {task_id}, path to image: {image_path}")

    if not os.path.exists(image_path):
        print(f"path {image_path} does not exsist.")
        update_task(task_id, status='done', people_count=0)
        ch.basic_ack(delivery_tag=method.delivery_tag)
        return

    num_people = detect_people_from_path(image_path)

    print(f"Person detected: {num_people} task: {task_id}")
    update_task(task_id, status='done', people_count=num_people)

    ch.basic_ack(delivery_tag=method.delivery_tag)


RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'task_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

print('Waiting...')
channel.start_consuming()
