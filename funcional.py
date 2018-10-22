import requests
import json

end_point = 'https://swapi.co/api/'
data = {}


def menu():
    print("1 - Listar personagem\n"
          "0 - Sair")


menu()
opc = int(input())
if (opc == 1):
    r = requests.get(url=end_point + "people/", data=data)
    json_char = json.loads(r.text)
    count = 0
    for nome in json_char['results']:
        count = count + 1
        print(count, "-", nome['name'])
    escolha = int(input("Digite um numero para saber os detalhes: "))
    escolha = str(escolha)
    req = requests.get(url=end_point + "people/" + escolha, data=data)
    json = json.loads(req.text)
    print(json['name'])
    print(json['gender'])
    print(json['created'])
    print(json['birth_year'])
else:

    exit("Atuais logo")