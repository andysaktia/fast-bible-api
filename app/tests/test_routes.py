import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_verse():
    response = client.get(
        "/bible/Genesis/1/1",
        headers={"Authorization": "your-secret-token"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "book_id": "Gen",
        "book_name": "Genesis",
        "chapter": 1,
        "verse": 1,
        "text": "In the beginning God created the heaven and the earth.",
        "translation_id": "KJV"
    }

def test_get_invalid_chapter():
    response = client.get(
        "/bible/Genesis/999",
        headers={"Authorization": "your-secret-token"}
    )
    assert response.status_code == 404
    assert response.json() == {"detail": "Chapter not found"}
