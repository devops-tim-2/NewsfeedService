from flask_restful import Resource, reqparse
from flask import request
from common.utils import auth
from service import newsfeed_service

 
class NewsfeedResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self):        
        try:
            payload = auth(request.headers)
        except Exception as e:
            return (e.message if hasattr(e, 'message') else str(e),403)

        page = int(request.args.get('page')) if request.args.get('page') else 1
        per_page = int(request.args.get('per_page')) if request.args.get('per_page') else 10

        return newsfeed_service.get_for_user(payload, page, per_page), 200
        
class CampaignsResource(Resource):
    def __init__(self):
        # To be implemented.
        pass
 
    def get(self):        
        try:
            payload = auth(request.headers)
        except Exception as e:
            return (e.message if hasattr(e, 'message') else str(e),403)

        page = int(request.args.get('page')) if request.args.get('page') else 1
        per_page = int(request.args.get('per_page')) if request.args.get('per_page') else 2

        return newsfeed_service.get_campaigns_for_user(payload, page, per_page), 200
        
