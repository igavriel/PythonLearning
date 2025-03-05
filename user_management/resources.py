from flask import request
from flask_restful import Resource
from models import db, User
from flasgger import swag_from

class UserResource(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'User retrieved successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer', 'example': 1},
                        'name': {'type': 'string', 'example': 'John Doe'},
                        'email': {'type': 'string', 'example': 'john.doe@example.com'}
                    }
                }
            }
        }
    })
    def get(self, user_id):
        user = User.query.get_or_404(user_id)
        return {'id': user.id, 'name': user.name, 'email': user.email}

    @swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'example': 'John Doe'},
                        'email': {'type': 'string', 'example': 'john.doe@example.com'}
                    }
                }
            }
        ],
        'responses': {
            200: {
                'description': 'User updated successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'User updated successfully'}
                    }
                }
            }
        }
    })
    def put(self, user_id):
        user = User.query.get_or_404(user_id)
        data = request.get_json()
        user.name = data['name']
        user.email = data['email']
        db.session.commit()
        return {'message': 'User updated successfully'}

    @swag_from({
        'responses': {
            200: {
                'description': 'User deleted successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'User deleted successfully'}
                    }
                }
            }
        }
    })
    def delete(self, user_id):
        user = User.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User deleted successfully'}

class UserListResource(Resource):
    @swag_from({
        'responses': {
            200: {
                'description': 'List of users',
                'schema': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'id': {'type': 'integer', 'example': 1},
                            'name': {'type': 'string', 'example': 'John Doe'},
                            'email': {'type': 'string', 'example': 'john.doe@example.com'}
                        }
                    }
                }
            }
        }
    })
    def get(self):
        users = User.query.all()
        return [{'id': user.id, 'name': user.name, 'email': user.email} for user in users]

    @swag_from({
        'parameters': [
            {
                'name': 'body',
                'in': 'body',
                'required': True,
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'example': 'John Doe'},
                        'email': {'type': 'string', 'example': 'john.doe@example.com'}
                    }
                }
            }
        ],
        'responses': {
            201: {
                'description': 'User created successfully',
                'schema': {
                    'type': 'object',
                    'properties': {
                        'message': {'type': 'string', 'example': 'User created successfully'}
                    }
                }
            }
        }
    })
    def post(self):
        data = request.get_json()
        new_user = User(name=data['name'], email=data['email'])
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User created successfully'}, 201
