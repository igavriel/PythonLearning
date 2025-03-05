import pytest
from app import app, db
from models import User

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_users.db'
    with app.app_context():
        db.create_all()
    yield app.test_client()
    with app.app_context():
        db.drop_all()

def test_create_user(client):
    response = client.post('/users', json={
        'name': 'John Doe',
        'email': 'john.doe@example.com'
    })
    assert response.status_code == 201
    assert 'User created successfully' in response.get_json()['message']

def test_get_user(client):
    with app.app_context():
        user = User(name='John Doe', email='john.doe@example.com')
        db.session.add(user)
        db.session.commit()
        user_id = user.id

    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'John Doe'
    assert data['email'] == 'john.doe@example.com'

def test_update_user(client):
    with app.app_context():
        user = User(name='John Doe', email='john.doe@example.com')
        db.session.add(user)
        db.session.commit()
        user_id = user.id

    response = client.put(f'/users/{user_id}', json={
        'name': 'Jane Doe',
        'email': 'jane.doe@example.com'
    })
    assert response.status_code == 200
    assert 'User updated successfully' in response.get_json()['message']

    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['name'] == 'Jane Doe'
    assert data['email'] == 'jane.doe@example.com'

def test_delete_user(client):
    with app.app_context():
        user = User(name='John Doe', email='john.doe@example.com')
        db.session.add(user)
        db.session.commit()
        user_id = user.id

    response = client.delete(f'/users/{user_id}')
    assert response.status_code == 200
    assert 'User deleted successfully' in response.get_json()['message']

    response = client.get(f'/users/{user_id}')
    assert response.status_code == 404

def test_get_users(client):
    with app.app_context():
        user1 = User(name='John Doe', email='john.doe@example.com')
        user2 = User(name='Jane Doe', email='jane.doe@example.com')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()

    response = client.get('/users')
    assert response.status_code == 200
    data = response.get_json()
    assert len(data) == 2
    assert data[0]['name'] == 'John Doe'
    assert data[1]['name'] == 'Jane Doe'
