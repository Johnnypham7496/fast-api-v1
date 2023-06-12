from fastapi.testclient import TestClient
from main import app

# TestClient: TestClient is a class provided by testing frameworks like pytest or libraries like FastAPI or Flask. 
# It is designed to simulate HTTP requests and interact with your application as if it were a real client.

# client = TestClient(): This line creates an instance of the TestClient class and assigns it to the variable client. 
# You can then use this client object to make HTTP requests to your application during testing.
client = TestClient(app)


def test_tc0001_welcome():
    td_message = {"message": "Hello, welcome to Autobots FastAPI bootcamp"}
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == td_message


def test_tc0002_health():
    td_message = {"status": "OK"}
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == td_message