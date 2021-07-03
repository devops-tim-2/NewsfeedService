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

        return newsfeed_service.get_for_user(payload), 200
        
