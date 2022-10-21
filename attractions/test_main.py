from typing import List
from fastapi.testclient import TestClient
from .main import app


client = TestClient(app)

def test_index():
    response = client.get('/')
    assert response.status_code == 200
    assert response.json() == {"data":"Hello, lets build that API for Mohammed Ibrahim"}
    
# Location create test  
# def test_create():
#     payload = {
#         "name": "string",
#         "city": "string",
#         "description": "string",
#         "images": [
#             {
#             "url": "https://string.com/img.jpg"
#             }
#         ],
#         "prices": [
#             {
#             "nationality": "string",
#             "amount": 0
#             }
#         ],
#         "packages": [
#             {
#             "offers": "string"
#             }
#         ]
#     }
#     response = client.post('/locations', json=payload)
#     assert response.status_code == 201
#     assert response.json() == payload

# # get all locations
# def test_all_locations():
#     response = client.get('/locations')
#     assert response.status_code == 200
    

# # get one location by id
# def test_location_by_id():
#     response = client.get('/locations/2')
#     assert response.status_code == 200
    
    