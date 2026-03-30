# Api fetch 

import requests

print ('Welcome to the Pokemon API Fetching!')

while True:
    pokemon_name = input('Enter the name of a Pokemon (or type "exit" to quit): ')
    if pokemon_name.lower() == "exit":
        break

    response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}')
    if response.status_code == 200:
        pokemon_data = response.json()
        print(f"Name: {pokemon_data['name'].capitalize()}")
        print(f"Height: {pokemon_data['height']}")
        print(f"Weight: {pokemon_data['weight']}")
    else:
        print("Pokemon not found!")