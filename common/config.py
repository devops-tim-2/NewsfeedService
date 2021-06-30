from os import environ
from flask_cors import CORS
from flask.app import Flask
from flask_wtf import CSRFProtect
from flask_restful import Api

config = {
    'test': 'TEST_DATABASE_URI',
    'dev': 'DEV_DATABASE_URI'
}

def setup_config(cfg_name: str):
    environ['SQLALCHEMY_DATABASE_URI'] = environ.get(config[cfg_name])
    
    app = Flask(__name__)
    if environ.get('ENABLE_CSRF') == 1:
        app.config['SECRET_KEY'] = environ.get('SECRET_KEY')
        app.config['WTF_CSRF_SECRET_KEY'] = environ.get('WTF_CSRF_SECRET_KEY')
        csrf = CSRFProtect()
        csrf.init_app(app)
        
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000", "send_wildcard": "False"}})
    api = Api(app)


    # This import must be postponed because importing common.database has side-effects
    from common.database import init_db
    init_db()


    
    # This import must be postponed after init_db has been called
    # from controller.post_controller import PostResource, PostListResource, ProfileResource, LikeResource, DislikeResource, FavoriteResource, CommentResource
    # api.add_resource(PostResource, '/api/<post_id>')
    # api.add_resource(PostListResource, '/api')
    # api.add_resource(ProfileResource, '/api/profile/<user_id>')
    # api.add_resource(LikeResource, '/api/like/<post_id>')
    # api.add_resource(DislikeResource, '/api/dislike/<post_id>')
    # api.add_resource(FavoriteResource, '/api/favorite/<post_id>')
    # api.add_resource(CommentResource, '/api/comment/<post_id>')


    # This import must be postponed after init_db has been called
    # from models.models import Block, Comment, Favorite, Follow, Like, Post, Tagged, User
    # if cfg_name == 'test':
    #     Block.query.delete()
    #     Comment.query.delete()
    #     Favorite.query.delete()
    #     Follow.query.delete()
    #     Like.query.delete()
    #     Tagged.query.delete()
    #     Post.query.delete()
    #     User.query.delete()

    return app
