import json
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
import ipdb

key = os.environ.get("GIPHY_KEY")

def pokeview(request, id):
    api_url = "http://pokeapi.co/api/v2/pokemon/{}/".format(id)
    res = requests.get(api_url)
    body = json.loads(res.content)
    name = body["name"]
    id = body['id']
    types = []
    for item in body['types']:
        types.append(item['type']['name'])
    # ipdb.set_trace()
    return JsonResponse({"name": name, "id":id, "types":types})
