import json
import requests
import os
key = os.environ.get("GIPHY_KEY")

res = requests.get("http://pokeapi.co/api/v2/pokemon/pikachu/")
body = json.loads(res.content)
print(body["name"]) # should be "pikachu"

url = "https://api.giphy.com/v1/gifs/search?api_key={}&q=pikachu&rating=g".format(key)
res2 = requests.get(url)
body2 = json.loads(res2.content)
print(body2['data'][0]['url']) #psychedelic pikachu url
