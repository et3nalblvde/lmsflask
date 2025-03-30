import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_get_jobs(client):
    response = client.get('/api/v2/jobs')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data['jobs'], list)


def test_post_job(client):
    new_job = {
        "title": "Тестирование API",
        "description": "Создание тестов для API"
    }
    response = client.post('/api/v2/jobs', json=new_job)
    assert response.status_code == 201
    data = response.get_json()
    assert 'id' in data
    assert data['title'] == new_job['title']


def test_post_job_missing_title(client):
    new_job = {
        "description": "Создание тестов для API"
    }
    response = client.post('/api/v2/jobs', json=new_job)
    assert response.status_code == 400
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == "Title is required"


def test_post_job_invalid_title(client):
    new_job = {
        "title": "T",
        "description": "Описание"
    }
    response = client.post('/api/v2/jobs', json=new_job)
    assert response.status_code == 400
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == "Title must be at least 3 characters long"


def test_get_job_by_invalid_id(client):
    job_id = 9999  # Невалидный ID
    response = client.get(f'/api/v2/jobs/{job_id}')
    assert response.status_code == 404
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == "Job not found"


def test_put_job(client):
    job_id = 1
    updated_job = {
        "title": "Обновленное название работы",
        "description": "Обновленное описание работы"
    }
    response = client.put(f'/api/v2/jobs/{job_id}', json=updated_job)
    assert response.status_code == 200
    data = response.get_json()
    assert data['title'] == updated_job['title']
    assert data['description'] == updated_job['description']


def test_put_job_invalid_data(client):
    job_id = 1
    updated_job = {
        "title": "T",
        "description": "Обновленное описание"
    }
    response = client.put(f'/api/v2/jobs/{job_id}', json=updated_job)
    assert response.status_code == 400
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == "Title must be at least 3 characters long"


# Корректный запрос: Удаление работы
def test_delete_job(client):
    job_id = 1
    response = client.delete(f'/api/v2/jobs/{job_id}')
    assert response.status_code == 200
    data = response.get_json()
    assert data['message'] == 'Job deleted'


def test_delete_nonexistent_job(client):
    job_id = 9999
    response = client.delete(f'/api/v2/jobs/{job_id}')
    assert response.status_code == 404
    data = response.get_json()
    assert 'message' in data
    assert data['message'] == "Job not found"
