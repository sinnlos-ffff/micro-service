import pika, json
import os
from dotenv import load_dotenv

load_dotenv()

params = pika.URLParameters(os.environ.get('RABBITMQ_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    print(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties= pika.BasicProperties( method))