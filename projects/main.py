import requests
token = "trainer_token"
data_new_poke={
      "name": "Бульбазавр",
        "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

response = requests.post("https://pokemonbattle.me:9104/pokemons",
                         headers={"Content-Type":"application/json","trainer_token":token},
                         json=data_new_poke)
print(response.text)

data_change_poke={
    "pokemon_id": "12469",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}
response = requests.put("https://pokemonbattle.me:9104/pokemons",
                        headers={"Content-Type":"application/json", "trainer_token":token},
                        json=data_change_poke)

print(response.text)

response = requests.post("https://pokemonbattle.me:9104/trainers/add_pokeball",
                         headers={"Content-Type":"application/json", "trainer_token":token},
                         json={"pokemon_id":"12469"})
print(response.text)
