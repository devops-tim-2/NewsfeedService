from models.models import PostFeed
from repository import newsfeed_repository

def get_for_user(user: dict):
    pf = newsfeed_repository.get_for_user(user['id'])
    pfd = [i.get_dict() for i in pf]
    return pfd
