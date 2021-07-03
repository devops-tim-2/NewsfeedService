from common.database import db_session
from models.models import PostFeed

def get_for_user(user_id):
    return PostFeed.query.filter(PostFeed.u_id == user_id).order_by(PostFeed.p_id.desc()).all()


