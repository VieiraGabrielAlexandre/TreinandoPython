import socket
import re
host = "127.0.0.1"
porta = 8800

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recebe = (host,porta)
soquete.bind(recebe)
soquete.listen(2)

print ("\nServidor Rodando: Host %s Ports %s"%(host,porta))
while True:
    conexao, enderecoIP = soquete.accept()
    print ("\nServidor acessado pelo cliente ", enderecoIP)
    while True:
        mensagem = conexao.recv(2048)
        if not mensagem:
            break
        print ("\nIP Cliente: ", enderecoIP)
        print ("MENSAGEM: ", mensagem.decode())