import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "app"))
from app import app

def test_index():
    client = app.test_client()
    r = client.get("/")
    assert r.status_code == 200
    assert b"Capstone" in r.data
