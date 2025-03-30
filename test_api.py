import pytest
import requests


def test_get_users(client):
    response = client.get('/api/v2/users')
    assert response.status_code == 200

    try:
        data = response.json()
        print("Response JSON:", data)
    except ValueError:
        data = None
        print("Error: Response is not valid JSON.")

    if data is not None:
        assert isinstance(data, list)
        assert len(data) == 0


def test_post_user(client):
    new_user = {
        "name": "Иван Иванов",
        "email": "ivan@example.com",
        "age": 30,
        "city_from": "Москва"
    }

    response = client.post('/api/v2/users', json=new_user)
    assert response.status_code == 201

    try:
        data = response.json()
        print("Created user:", data)
    except ValueError:
        data = None
        print("Error: Response is not valid JSON.")

    if data is not None:
        assert 'id' in data
        assert data['name'] == new_user['name']


def test_post_invalid_user(client):
    new_user = {
        "name": "Петр Петров",
        "age": 25,
        "city_from": "Санкт-Петербург"
    }

    response = client.post('/api/v2/users', json=new_user)
    assert response.status_code == 400

    try:
        data = response.json()
        print("Error response:", data)
    except ValueError:
        data = None
        print("Error: Response is not valid JSON.")

    if data is not None:
        assert 'message' in data
