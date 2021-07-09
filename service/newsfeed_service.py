from models.models import PostFeed
from repository import newsfeed_repository

def get_for_user(user: dict, page: int, per_page: int):
    pf = newsfeed_repository.get_for_user(user['id'])
    pfd = [i.get_dict() for i in pf][(page-1)*per_page : page*per_page]
    return pfd

def get_campaigns_for_user(user, page, per_page):
    pf = newsfeed_repository.get_campaigns_for_user(user['id'])
    pfd = [i.get_dict() for i in pf][(page-1)*per_page : page*per_page]
    return pfd
