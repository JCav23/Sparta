import json

course = {"name": "Data 249", "Trainer": "Paula"}

# reading from python dict and writing to a json file
with open("new_json_data.json", "w") as jsonfile:
    json.dump(course, jsonfile)

# # reading from a json file and writing as a python dict
# with open("new_json_data.json") as jsonfile:
#     course_file = json.load(jsonfile)
#     print(course_file['name'])
#     print(type(course_file))

# Helpful article discussing working with json files within python:
# https://realpython.com/python-json/