'''
This is the main entry point for the Flask application.
'''

from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from models import db
from resources import UserResource, UserListResource
from swagger_config import swagger_template, swagger_config

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
api = Api(app)

with app.app_context():
    db.create_all()

swagger = Swagger(app, template=swagger_template, config=swagger_config)

api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserListResource, '/users')

if __name__ == '__main__':
    app.run(debug=True)