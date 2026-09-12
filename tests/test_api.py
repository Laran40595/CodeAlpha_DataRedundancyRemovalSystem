import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_create_unique_user():
    response = client.post(
        "/users",
        json={
            "name": "Automated Test User",
            "email": "automated_unique@example.com",
            "phone": "08044444444"
        }
    )

    assert response.status_code == 200
    assert response.json()["classification"] == "UNIQUE"


def test_reject_duplicate_user():
    client.post(
        "/users",
        json={
            "name": "Duplicate Test User",
            "email": "duplicate_test@example.com",
            "phone": "08055555555"
        }
    )

    response = client.post(
        "/users",
        json={
            "name": "Another Duplicate User",
            "email": "duplicate_test@example.com",
            "phone": "08066666666"
        }
    )

    assert response.status_code == 200
    assert response.json()["classification"] == "REDUNDANT"


def test_reject_invalid_email():
    response = client.post(
        "/users",
        json={
            "name": "Invalid Email User",
            "email": "not-an-email",
            "phone": "08077777777"
        }
    )

    assert response.status_code == 422
    assert response.json()["classification"] == "INVALID"


def test_reject_short_name():
    response = client.post(
        "/users",
        json={
            "name": "A",
            "email": "shortname@example.com",
            "phone": "08088888888"
        }
    )

    assert response.status_code == 422
    assert response.json()["classification"] == "INVALID"