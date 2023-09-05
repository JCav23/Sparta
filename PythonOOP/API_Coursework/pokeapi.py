import requests
import json
import random

pokemon_req = requests.get("https://pokeapi.co/api/v2/pokemon/charizard")
json_string = pokemon_req.content.decode('utf-8')
data = json.loads(json_string)

with open("charizard_raw.json") as jsonfile:
    charizard = json.load(jsonfile)
    # print(charizard['height'])
    # print(charizard['abilities'][0]['ability']['name'])
    # print(charizard['moves'][1]['move'])
    # print(charizard['moves'][7]['move'])
    # print(charizard['moves'][17]['move'])
    # print(charizard['moves'][18]['move'])
    # print(charizard['stats'][6]['stat'])

# def pokemon_types(raw_data):
#     types = []
#     for poke_type in raw_data['types'][0:2]:
#         p_type = raw_data['types'][poke_type]['type']['name']
#         types.append(p_type)
#     return types
#
# print(pokemon_types(charizard))


def random_move_generator(raw_data):
    moves = []
    counter = 0
    while counter < 4:
        move = raw_data['moves'][random.randint(0, 124)]['move']['name']
        counter += 1
        if move not in moves:
            moves.append(move)
        else:
            continue
    return moves


print(random_move_generator(charizard))


def pokedex_entry(raw_data):
    pokemon = {
        'Name': raw_data['name'],
        'Pokedex ID': raw_data['id'],
        'Ability': raw_data['abilities'][0]['ability']['name'],
        'Type': raw_data['types'][0]['type']['name'],
        'Moves': random_move_generator(raw_data),
        'Height': raw_data['height'],
        'Weight': raw_data['weight'],
        'Base Stats': {
            'HP': raw_data['stats'][0]['base_stat'],
            'Attack': raw_data['stats'][1]['base_stat'],
            'Defense': raw_data['stats'][2]['base_stat'],
            'Special Attack': raw_data['stats'][3]['base_stat'],
            'Special Defence': raw_data['stats'][4]['base_stat'],
            'Speed': raw_data['stats'][5]['base_stat']
        }
    }
    return pokemon


with open("pokedex_charizard.json", "w") as jsonfile:
    json.dump(pokedex_entry(charizard), jsonfile)


