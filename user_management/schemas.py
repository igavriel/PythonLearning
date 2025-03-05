'''
This file defines the schemas for Swagger documentation.
'''

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