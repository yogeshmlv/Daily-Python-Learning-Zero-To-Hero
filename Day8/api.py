print('Api Fetiching...')
# import requests
# from pprint import pprint

# response = requests.get ('https://pokeapi.co/api/v2/pokemon/pikachu')
# pocker_data = response.json()
# pprint(pocker_data.keys())

import requests
import json #json is a built-in module in Python that provides functions for working with JSON data. It allows you to convert Python objects to JSON format and vice versa. In this code, we will use the json module to save the fetched data from the API into a JSON file.

response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
pocker_data = response.json()
with open('pocker_data.json', 'w') as f: #This line opens a file named 'pocker_data.json' in write mode ('w'). If the file does not exist, it will be created. If it already exists, its contents will be overwritten.
    json.dump(pocker_data, f, indent=4)
print('Data saved to pocker_data.json')