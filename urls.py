import urllib.request
import urllib.parse
import re
import json

url = str(input("Digite a url: "))
print (url)
f = urllib.request.urlopen(url)
conteudo = f.read().decode('utf-8')
