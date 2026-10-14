import pytest
import os
import sys
import json

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
import database as db

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_api_predict(client):
    payload = {
        "property_type": "Residential",
        "city": "Patiala",
        "area_sqft": 1200,
        "bedrooms": 2,
        "bathrooms": 2,
        "property_age": 5,
        "has_parking": 1,
        "furnishing": "Semi-Furnished",
        "price": 5000000
    }
    response = client.post("/api/predict", json=payload)
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "predicted_price" in data["data"]
    assert "barometer_verdict" in data["data"]

def test_get_properties(client):
    response = client.get("/api/properties")
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert isinstance(data["data"], list)
    assert len(data["data"]) > 0

def test_create_property(client):
    new_prop = {
        "title": "Modern Penthouse Test",
        "description": "Lovely rooftop views",
        "property_type": "Apartment",
        "city": "Mohali",
        "locality": "Sector 70",
        "area_sqft": 1800,
        "bedrooms": 3,
        "bathrooms": 3,
        "property_age": 2,
        "has_parking": 1,
        "furnishing": "Fully-Furnished",
        "price": 11500000,
        "seller_name": "Test Seller",
        "seller_phone": "+91 99999 88888"
    }
    response = client.post("/api/properties", json=new_prop)
    assert response.status_code == 201
    data = response.get_json()
    assert data["success"] is True
    assert "property_id" in data

def test_chat_and_appointment_workflow(client):
    # 1. Post a message to property 1
    msg_payload = {
        "sender_type": "buyer",
        "sender_name": "Haneesh (Buyer)",
        "message_text": "Is the price negotiable?"
    }
    msg_res = client.post("/api/properties/1/messages", json=msg_payload)
    assert msg_res.status_code == 201

    # 2. Schedule site visit appointment
    appt_payload = {
        "property_id": 1,
        "buyer_name": "Haneesh",
        "buyer_phone": "+91 99887 76655",
        "visit_date": "2026-10-10",
        "visit_time": "15:00",
        "notes": "Would like to see parking area"
    }
    appt_res = client.post("/api/appointments", json=appt_payload)
    assert appt_res.status_code == 201
    appt_data = appt_res.get_json()
    appt_id = appt_data["appointment_id"]

    # 3. Confirm appointment (computes time-to-appointment)
    confirm_res = client.post(f"/api/appointments/{appt_id}/confirm")
    assert confirm_res.status_code == 200
    confirm_data = confirm_res.get_json()
    assert confirm_data["status"] == "confirmed"
    assert "time_to_appointment_seconds" in confirm_data

    # 4. Process payment for visit token
    pay_payload = {
        "property_id": 1,
        "appointment_id": appt_id,
        "buyer_name": "Haneesh",
        "amount": 500.0,
        "payment_method": "UPI"
    }
    pay_res = client.post("/api/payments", json=pay_payload)
    assert pay_res.status_code == 201
    pay_data = pay_res.get_json()
    assert pay_data["success"] is True
    assert "transaction_id" in pay_data

def test_metrics_endpoint(client):
    response = client.get("/api/metrics")
    assert response.status_code == 200
    data = response.get_json()
    assert data["success"] is True
    assert "ml_model" in data
    assert "marketplace" in data
    assert "appointments" in data
