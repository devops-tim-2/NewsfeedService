from common.database import db_session
from models.models import PostFeed, CampaignFeed

def get_for_user(user_id):
    return PostFeed.query.filter(PostFeed.u_id == user_id).order_by(PostFeed.p_id.desc()).all()


def get_campaigns_for_user(user_id):
    return CampaignFeed.query.filter(CampaignFeed.u_id == user_id).order_by(CampaignFeed.c_id.desc()).all()