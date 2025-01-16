from fastapi.testclient import TestClient
from main import app  # Ensure the FastAPI app is imported correctly

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={
        "name": "John Doe",
        "age": 30,
        "gender": "male",
        "email": "john.doe@example.com",
        "city": "New York",
        "interests": ["reading", "sports"]
    })
    assert response.status_code == 200
    assert response.json()["name"] == "John Doe"

def test_get_users():
    response = client.get("/users/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_user():
    response = client.put("/users/1", json={
        "name": "John Updated",
        "age": 31,
        "gender": "male",
        "email": "john.updated@example.com",
        "city": "New York",
        "interests": ["music"]
    })
    assert response.status_code == 200
    assert response.json()["name"] == "John Updated"

def test_delete_user():
    response = client.delete("/users/1")
    assert response.status_code == 200
