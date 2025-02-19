import requests

URL='https://api.pokemonbattle.ru/v2'

TOKEN='faf640537f43b72eb455d29e926337d9'

HEADER={'Content-Type':'application/json', 'trainer_token' : TOKEN} 

body_registration= {
    "trainer_token": TOKEN,
    "email": "sautin1001@yandex.ru",
    "password": "B2h0ms7b"
}

body_activ= {
    "trainer_token": TOKEN
}

body_pokemon= {
    "name": "Daf",
    "photo_id": -1
}

body_rename= {
    "pokemon_id": "239739",
    "name": "New",
    "photo_id": 2
}

body_inpokeball= {
    "pokemon_id": "239739"
}


response = requests.post(url=f'{URL}/trainers/reg',headers=HEADER,json=body_registration)
print (response.text)

response_activ = requests.post(url=f'{URL}/trainers/confirm_email',headers=HEADER,json=body_activ)
print (response_activ.text)

response_pokemon = requests.post(url=f'{URL}/pokemons',headers=HEADER,json=body_pokemon)
print (response_pokemon.text)

message = response_pokemon.json() ['message']
print (message)

response_rename = requests.post(url=f'{URL}/pokemons',headers=HEADER,json=body_rename)
print (response_rename.text)

response_inpokeball = requests.post(url=f'{URL}/trainers/add_pokeball',headers=HEADER,json=body_inpokeball)
print (response_inpokeball.text)


