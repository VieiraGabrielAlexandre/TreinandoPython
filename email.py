import re
email = str(input("Informe um e-mail"))
if (re.search('[a-z]|[0-9]+@[a-z]|[0-9]+.com', email)):
    print ("Email valido")
    print ("E-mail:", email)
else:
    print ("Email invalido")