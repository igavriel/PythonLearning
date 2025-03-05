To add unit tests to your Flask application, we'll use the `unittest` framework, which is part of the standard library, along with `Flask-Testing` for some helpful utilities. We will create tests for the user management API endpoints to ensure that they are functioning correctly.

First, install the necessary packages:

```bash
pip install Flask-Testing
```

### Project Structure
Add a new `tests/` directory to hold the test files:

```
user_management/
├── app.py
├── models.py
├── resources.py
├── schemas.py
├── swagger_config.py
└── tests/
    └── test_user_management.py
```

### tests/test_user_management.py
This file contains the unit tests for the user management system.

```python
import unittest
from app import app, db
from models import User

class UserManagementTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_users.db'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.drop_all()

    def test_create_user(self):
        response = self.app.post('/users', json={
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('User created successfully', response.get_json()['message'])

    def test_get_user(self):
        with app.app_context():
            user = User(name='John Doe', email='john.doe@example.com')
            db.session.add(user)
            db.session.commit()
            user_id = user.id

        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'John Doe')
        self.assertEqual(data['email'], 'john.doe@example.com')

    def test_update_user(self):
        with app.app_context():
            user = User(name='John Doe', email='john.doe@example.com')
            db.session.add(user)
            db.session.commit()
            user_id = user.id

        response = self.app.put(f'/users/{user_id}', json={
            'name': 'Jane Doe',
            'email': 'jane.doe@example.com'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('User updated successfully', response.get_json()['message'])

        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['name'], 'Jane Doe')
        self.assertEqual(data['email'], 'jane.doe@example.com')

    def test_delete_user(self):
        with app.app_context():
            user = User(name='John Doe', email='john.doe@example.com')
            db.session.add(user)
            db.session.commit()
            user_id = user.id

        response = self.app.delete(f'/users/{user_id}')
        self.assertEqual(response.status_code, 200)
        self.assertIn('User deleted successfully', response.get_json()['message'])

        response = self.app.get(f'/users/{user_id}')
        self.assertEqual(response.status_code, 404)

    def test_get_users(self):
        with app.app_context():
            user1 = User(name='John Doe', email='john.doe@example.com')
            user2 = User(name='Jane Doe', email='jane.doe@example.com')
            db.session.add(user1)
            db.session.add(user2)
            db.session.commit()

        response = self.app.get('/users')
        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['name'], 'John Doe')
        self.assertEqual(data[1]['name'], 'Jane Doe')

if __name__ == '__main__':
    unittest.main()
```

### Running the Tests
To run the tests, navigate to the project directory and execute:

```bash
python -m unittest discover tests
```

This command will discover and run all the test cases defined in the `tests/` directory.

### Explanation
- **setUp**: This method sets up the test environment. It creates a test client and a new SQLite database for testing.
- **tearDown**: This method cleans up after each test by dropping all tables from the test database.
- **test_create_user**: This test checks if a new user can be created successfully.
- **test_get_user**: This test checks if a user can be retrieved by ID.
- **test_update_user**: This test checks if a user's information can be updated.
- **test_delete_user**: This test checks if a user can be deleted.
- **test_get_users**: This test checks if all users can be retrieved.

These tests ensure that the API endpoints for user management are working as expected. You can extend the tests by adding more scenarios and edge cases to improve coverage.