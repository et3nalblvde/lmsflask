import requests

BASE_URL = "http://127.0.0.1:5000/api/users"


response = requests.get(BASE_URL)
print("GET /api/users:", response.status_code, response.json())


new_user = {
    "name": "Иван Петров",
    "email": "ivan@example.com",
    "age": 35,
    "city_from": "Москва"
}
response = requests.post(BASE_URL, json=new_user)
print("POST /api/users:", response.status_code, response.json())


user_id = response.json().get("id", 1)
response = requests.get(f"{BASE_URL}/{user_id}")
print(f"GET /api/users/{user_id}:", response.status_code, response.json())


updated_user = {
    "name": "Иван Иванов",
    "age": 36
}
response = requests.put(f"{BASE_URL}/{user_id}", json=updated_user)
print(f"PUT /api/users/{user_id}:", response.status_code, response.json())


response = requests.delete(f"{BASE_URL}/{user_id}")
print(f"DELETE /api/users/{user_id}:", response.status_code, response.json())


response = requests.get(f"{BASE_URL}/9999")
print("GET /api/users/9999 (not found):", response.status_code, response.text)
