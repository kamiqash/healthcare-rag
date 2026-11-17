from fastapi.testclient import TestClient

# app is the name of the folder so app.main where main is the name of the file.
# Then app is also the name of the object created in main.py.
from app.main import app 


def test_health_endpoint():
    with TestClient(app) as client:                   #creates a test client connected to your FastAPI app
        response = client.get("/health")              #sends get request to /health which is matched by FastAPI to health_check()

    assert response.status_code == 200                #response check.
    assert response.json() == {"status": "ok"}