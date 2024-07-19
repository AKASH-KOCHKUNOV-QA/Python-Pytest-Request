import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '00966bcb5eaa7ac3ab4c2fa33c0b7157'
HEADER = {'Content-Type' : 'application/json','trainer_token': TOKEN}

body_registration =     {
    "trainer_token": TOKEN,
    "email": "akashkochkunov@yandex.ru",
    "password": "Iloveqa1"
}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "44280",
    "name": "akash",
    "photo_id": 2

}
body_pokeball =  {
    "pokemon_id": "44280"
}


response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response.text)

response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeball)
print(response.text)