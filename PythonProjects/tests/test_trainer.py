import requests
import pytest

URL='https://api.pokemonbattle.ru/v2'
TOKEN='faf640537f43b72eb455d29e926337d9'
HEADER={'Content-Type':'application/json', 'trainer_token' : TOKEN} 
TRAINER_ID='20922'

def test_status_code():
    responce = requests.get(url=f'{URL}/trainers',params= {'trainer_id' : TRAINER_ID})
    assert  responce.status_code == 200

def test_statu():
    responce = requests.get(url=f'{URL}/trainers')
    assert  responce.status_code == 200

