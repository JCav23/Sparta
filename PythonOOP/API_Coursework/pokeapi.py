import requests
import json

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
json_string = pokemon_req.content.decode('utf-8')
data = json.loads(json_string)
print(type(data))

with open("charizard_raw.json") as jsonfile:
    charizard = json.load(jsonfile)
    print(charizard['abilities'][0]['ability'])
    print(charizard['moves'][1]['move'])
    print(charizard['moves'][7]['move'])
    print(charizard['moves'][17]['move'])
    print(charizard['moves'][18]['move'])
    print(charizard['stats'][:])

