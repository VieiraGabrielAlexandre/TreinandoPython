#encoding: utf-8
try:
    num1 = float(input('Digite um numero'))
    num2 = float(input('Digite outro numero'))

    division = (num1 / num2)

    print(division)
except ZeroDivisionError:
    print ("Divisao por zero é burrice")
except ValueError:
    print ("Letra")