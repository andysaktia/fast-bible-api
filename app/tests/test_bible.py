from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_verse():
    response = client.get("/bible/Genesis/1/1", headers={"Authorization": "your-secret-token"})
    assert response.status_code == 200
    assert response.json()["text"] == "In the beginning God created the heaven and the earth."
