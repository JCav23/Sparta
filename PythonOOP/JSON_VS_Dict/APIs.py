import requests
import json

headers = {'Content-Type': 'application/json'}
json_data = json.dumps({'postcodes': ["PR3 0SG", "M45 6GN", "EX165BL"]})

# post_code_req = requests.get("https://api.postcodes.io/postcodes/ME143DW")
post_code_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_data)


# print(post_code_req.status_code)
# print(post_code_req.headers)
# print(post_code_req.content)
# print(post_code_req.json())
# print(type(post_code_req.json()))
print(post_code_req.json()['result'][0]['result']['country'])