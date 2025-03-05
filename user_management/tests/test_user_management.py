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
