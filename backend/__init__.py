import os

from flask import Flask, send_from_directory
from pymongo import MongoClient
from flask_login import LoginManager
from flask_cors import CORS, cross_origin

from .routes import main_routes, discrete_exchange_routes

# see: https://flask-login.readthedocs.io/en/latest/
# see: https://pythonbasics.org/flask-login/

# create login manager
login_manager = LoginManager()
login_manager.login_view = 'login'

# function to create app instance
def create_app():

    app = Flask(__name__, static_folder='build')
    
    # CORS(app)
    CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    # Serve React App
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def serve(path):
        if path != "" and os.path.exists(app.static_folder + '/' + path):
            return send_from_directory(app.static_folder, path)
        else:
            return send_from_directory(app.static_folder, 'index.html')
        
    @app.after_request
    def after_request(response):
        # response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    
    
    
    # configure upload destination for submitted files
    app.config['UPLOAD_DEST'] = os.path.dirname(__file__) + '/submitted_traders'
    
    # initialize login manager
    login_manager.init_app(app)
    
    # blueprints
    app.register_blueprint(main_routes)
    app.register_blueprint(discrete_exchange_routes)
    
    return app
