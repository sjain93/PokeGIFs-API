import json
import requests

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
print(body["name"]) # should be "pikachu"
