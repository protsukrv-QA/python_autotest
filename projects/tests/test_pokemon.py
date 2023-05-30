import requests
import pytest

host = "https://pokemonbattle.me:9104"

def test_status_code():
    response = requests.get(f'{host}/trainers', params={"trainer_id":"4325"}, headers={"Content-Type":"application/json"})
    assert response.status_code == 200

def test_text_name():
    response_body = requests.get(f"{host}/trainers", params={"trainer_id":"4325"})
    assert response_body.json()["trainer_name"] == "Родион" 