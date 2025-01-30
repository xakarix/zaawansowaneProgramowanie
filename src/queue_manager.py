import pika
import json
import uuid
from db_manager import add_task

RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'task_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue=QUEUE_NAME)

def add_to_queue(image_path):
    task_id = str(uuid.uuid4())
    add_task(file_path=image_path, task_id=task_id)

    message = {'task_id': task_id, 'image_path': image_path}
    print(f"Adding message to queue: {message}")



    channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=json.dumps(message))

    return task_id


