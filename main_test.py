import pytest
from fastapi.testclient import TestClient
from main import api

client = TestClient(api)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Message" in response.json()

#test index
def test_index():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}

#test post
def test_add_ticket():
    ticket_data = {
        "id": 1,
        "flight_name": "Air Asia",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Bangkok"
    }
    response = client.post("/ticket", json=ticket_data)
    assert response.status_code == 200
    assert response.json() == ticket_data

#test all get
def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) >= 1

#tes put
def test_update_ticket():
    updated_ticket_data = {
        "id": 1,
        "flight_name": "Air Asia Updated",
        "flight_date": "2025-10-16",
        "flight_time": "15:00",
        "destination": "Singapore"
    }
    response = client.put("/ticket/1", json=updated_ticket_data)
    assert response.status_code == 200
    assert response.json() == updated_ticket_data

#test delete
def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    assert response.json()=={
        "id":1,
        "flight_name":"Air Asia Updated",
        "flight_date":"2025-10-16",
        "flight_time":"15:00",
        "destination":"Singapore"
    }

