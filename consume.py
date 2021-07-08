from broker.consumer import PostConsumer, UserConsumer, CampaignConsumer
import pika
from os import environ

params = pika.URLParameters(environ.get('RABBITMQ_URI'))
connection = pika.BlockingConnection(params)
channel = connection.channel()


user_queue = UserConsumer(channel)
post_queue = PostConsumer(channel)
campaign_consumer = CampaignConsumer(channel)

print(f'Started user_queue: {type(user_queue)}')
print(f'Started post_queue: {type(post_queue)}')
print(f'Started post_queue: {type(campaign_consumer)}')

channel.start_consuming()
channel.close()