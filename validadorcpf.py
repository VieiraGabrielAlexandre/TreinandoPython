cpf = input('Digite o número do seu CPF: ')

lista = list(cpf)


# print(lista);

def validarCPF():
    cont = 10;
    dig1 = 0;
    for i in range(9):
        dig1 = dig1 + (int(lista[i]) * cont);
        cont = cont - 1;
    dig1 = dig1 % 11;
    if (dig1 == 0 or dig1 == 1):
        dig1 = 0;
    else:
        dig1 = 11 - dig1;

    dig2 = 0;
    cont = 11;
    for i in range(9):
        dig2 = dig2 + (int(lista[i]) * cont);
        cont = cont - 1;
    dig2 = dig2 + (dig1 * 2);
    dig2 = dig2 % 11;

    if (dig2 == 0 or dig2 == 1):
        dig2 = 0;
    else:
        dig2 = 11 - dig2;

    if ((dig1 == int(lista[9])) and (dig2 == int(lista[10]))):
        print('O CPF é válido!')
    else:
        print('O CPF é inválido');


validarCPF();