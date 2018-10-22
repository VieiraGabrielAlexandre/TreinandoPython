economia = ['dinheiro']
economias = [ 'dolar']
economiass = ['contas']

noticia = open('noticia.txt', 'r')
linhas = noticia.readlines()

qtdEconmia = 0
qtdEconomias = 0
qtdEconomiass = 0
for linha in linhas:
    for i in range(0, economia.__len__()):
        qtdEconmia += linha.count(economia[i], 0, linha.__len__())
    for i in range (0, economias.__len__()):
        qtdEconomias += linha.count(economias[i], 0, linha.__len__())
        for i in range(0, economias.__len__()):
            qtdEconomiass += linha.count(economiass[i], 0, linha.__len__())

print (qtdEconmia)
print (qtdEconomias)
print (qtdEconomiass)