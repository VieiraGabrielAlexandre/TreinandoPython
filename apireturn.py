import urllib.request
import urllib.parse
import re
import requests
import json

end_point = 'https://swapi.co/api/'
data = {}
r = requests.get(url = end_point+"people/", data = data)
json = json.loads(r.text)
print (json)
print (json ['count'])