Creating a user management system with Flask and Swagger involves several steps. Below is an example project that demonstrates a simple implementation of a user management system with Flask for the backend and Swagger for API documentation.

### Prerequisites
Make sure you have Python and pip installed. Then, install the necessary packages:

```bash
pip install Flask Flask-RESTful flask-sqlalchemy flasgger
```

### Project Structure
```
user_management/
├── app.py
├── models.py
├── resources.py
├── schemas.py
└── swagger_config.py
```

### app.py
This is the main entry point for the Flask application.

```python
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
```

### models.py
This file contains the SQLAlchemy model for the User.

```python
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'
```

### resources.py
This file contains the Flask-RESTful resources for the User endpoints.

```python
from flask import request
from flask_restful import Resource
from models import db, User

class UserResource(Resource):
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'name': user.name, 'email': user.email}

    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        return {'message': 'User updated successfully'}

    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}

class UserListResource(Resource):
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]

    def post(self):
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201
```

### schemas.py
This file defines the schemas for Swagger documentation.

```python
user_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer",
            "example": 1
        },
        "name": {
            "type": "string",
            "example": "John Doe"
        },
        "email": {
            "type": "string",
            "example": "john.doe@example.com"
        }
    }
}

user_list_schema = {
    "type": "array",
    "items": user_schema
}
```

### swagger_config.py
This file configures Swagger for the Flask application.

```python
swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "User Management API",
        "description": "API documentation for the User Management system",
        "version": "1.0.0"
    },
    "basePath": "/",
    "schemes": [
        "http",
        "https"
    ],
    "securityDefinitions": {
        "ApiKeyAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header"
        }
    },
}

swagger_config = {
    "headers": [],
    "specs": [
        {
            "endpoint": 'apispec_1',
            "route": '/apispec_1.json',
            "rule_filter": lambda rule: True,  # all in
            "model_filter": lambda tag: True,  # all in
        }
    ],
    "static_url_path": "/flasgger_static",
    "swagger_ui": True,
    "specs_route": "/swagger/"
}
```

### Running the Application
To run the application, navigate to the project directory and run:

```bash
python app.py
```

You can then access the Swagger UI at `http://localhost:5000/swagger/` to interact with the API and view the documentation.

This example provides a basic setup for a user management system with CRUD operations and Swagger documentation. You can expand it by adding authentication, more sophisticated error handling, and other features as needed.