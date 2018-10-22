import re
cpf = str(input("Informe um CPF: "))
if (re.search('\d{3}.\d{3}.\d{3}-\d{2}', cpf)):
    print("CPF Vᬩdo")
    print ("CPF:", cpf)
else:
    print ("CPF INVALIDO")
