import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import random
import os
import ipdb

def pokeview(request, id):
    key = os.environ.get("GIPHY_KEY")
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
    gif_api_url = ""
    res = requests.get(api_url)
    body = json.loads(res.content)
    name = body["name"]
    id = body['id']
    types = []

    for item in body['types']:
        types.append(item['type']['name'])

    gif_api_url = "https://api.giphy.com/v1/gifs/search?api_key={}&q={}&rating=g".format(key, name)
    res2 = requests.get(gif_api_url)
    body2 = json.loads(res2.content)
    link_url = []

    for bunny in body2['data']:
        link_url.append(bunny['url'])

    # ipdb.set_trace()
    return JsonResponse({"name": name, "id":id, "types":types, "gif":random.choice(link_url)})
