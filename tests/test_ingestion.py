from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "running"

def test_schema_validation():
    response = client.post("/api/analyze", json={"message": ""})
    assert response.status_code == 422
