import pika 
import os
from dotenv import load_dotenv

load_dotenv()

params = pika.URLParameters(os.environ.get('RABBITMQ_URL'))

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish():
    channel.basic_publish(exchange='', routing_key='main', body='hello')