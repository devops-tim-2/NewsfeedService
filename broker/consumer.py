import json
from common.database import init_db
init_db()

from models.models import Post, PostFeed, User, Follow, Block


from common.database import db_session
class UserConsumer:
    def __init__(self, channel):
        self.exchange_name = 'user'
        self.channel = channel
        channel.exchange_declare(exchange=self.exchange_name, exchange_type='fanout')
        q = channel.queue_declare(queue='')
        channel.queue_bind(exchange=self.exchange_name, queue=q.method.queue)
        channel.basic_consume(queue=q.method.queue, on_message_callback=self.on_message, auto_ack=True)

    def on_message(self, ch, method, properties, body):
        try:
            data = json.loads(body)

            if properties.content_type == 'user.created':            
                user = User(id=data['id'], age=data['age'], sex=data['sex'], region=data['region'], interests=data['interests'])
                db_session.add(user)
                db_session.commit()
            elif properties.content_type == 'user.deleted':
                User.query.get(data['id']).delete()
                Follow.query.filter(Follow.src == data['id']).delete()
                Follow.query.filter(Follow.dst == data['id']).delete()
                Block.query.filter(Block.src == data['id']).delete()
                Block.query.filter(Block.dst == data['id']).delete()
                db_session.commit()
            elif properties.content_type == 'user.updated':
                user = User.query.get(data['id'])
                if user.public != data['public']:
                    user.public = data['public']
                    db_session.commit()
            elif properties.content_type == 'user.follow.created':
                follow = Follow(id=data['id'], src=data['src'], dst=data['dst'], mute=data['mute'])
                db_session.add(follow)
                db_session.commit()
            elif properties.content_type == 'user.block.created':
                block = Block(id=data['id'], src=data['src'], dst=data['dst'])
                db_session.add(block)
                db_session.commit()
            elif properties.content_type == 'user.follow.updated':
                follow = Follow.query.get(data['id'])
                follow.mute = data['mute']
                db_session.commit()
        except Exception:
            # don't crash
            pass


class PostConsumer:
    def __init__(self, channel):
        self.exchange_name = 'post'
        self.channel = channel
        channel.exchange_declare(exchange=self.exchange_name, exchange_type='fanout')
        q = channel.queue_declare(queue='')
        channel.queue_bind(exchange=self.exchange_name, queue=q.method.queue)
        channel.basic_consume(queue=q.method.queue, on_message_callback=self.on_message, auto_ack=True)

    def on_message(self, ch, method, properties, body):
        data = json.loads(body)
        try:
            if properties.content_type == 'post.created':            
                post = Post(id=data['id'])
                db_session.add(post)
                db_session.commit()
            elif properties.content_type == 'post.deleted':
                Post.query.get(data['id']).delete()
                PostFeed.query.filter(PostFeed.p_id == data['id']).delete()
                db_session.commit()
            elif properties.content_type == 'post.published':
                following = list(map(lambda follower: follower.src, Follow.query.filter(Follow.dst == data['user_id']).all()))
                self_id = [data['user_id']]
                for subscriber_id in [*following, *self_id]:
                    db_session.add(PostFeed(u_id = subscriber_id, p_id = data['id']))
                db_session.commit()
        except Exception as e:
            # don't crash
            print(e)
            pass
        


