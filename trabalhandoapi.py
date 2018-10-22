import urllib.request
import urllib.parse
import re
import requests
import json

opcao = int(input("1 - Listar Personagens\n0 - Sair"))
if (opcao == 1):
    end_point = 'https://swapi.co/api/'
    data = {}
    r = requests.get(url=end_point + "people/1/", data=data)
    json = json.loads(r.text)
    print(json['results'])