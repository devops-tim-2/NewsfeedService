# from broker.consumer import AdminConsumer, UserConsumer
import pika
from os import environ

params = pika.URLParameters(environ.get('RABBITMQ_URI'))
connection = pika.BlockingConnection(params)
channel = connection.channel()

# user_queue = UserConsumer(channel)
# admin_queue = AdminConsumer(channel)

# print(f'Started user_queue: {type(user_queue)}')
# print(f'Started admin_queue: {type(admin_queue)}')

channel.start_consuming()
channel.close()