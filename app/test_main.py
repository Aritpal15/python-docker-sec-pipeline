from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "data-processor"}


def test_process_data_success():
    payload = {"key": "sensor_id", "value": "temp_24c"}
    response = client.post("/process", json=payload)
    assert response.status_code == 200
    assert response.json() == {
        "processed": True,
        "input_key": "sensor_id",
        "result": "TEMP_24C"
    }


def test_process_data_empty_key():
    payload = {"key": "   ", "value": "test"}
    response = client.post("/process", json=payload)
    assert response.status_code == 400
    assert response.json()["detail"] == "Key cannot be empty"
