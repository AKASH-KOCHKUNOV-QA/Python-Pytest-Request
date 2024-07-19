import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '00966bcb5eaa7ac3ab4c2fa33c0b7157'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}
TRAINER_ID = 4427


def test_status_code():
    response = requests.get(url= f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200


def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'Бульбазавр'