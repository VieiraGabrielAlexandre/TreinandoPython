import socket
host = '10.117.4.45'
porta = 8800

soquete  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
envio = (host,porta)
soquete.connect(envio)

print ("\n Pressione S para encerrar")
print ("\nDigite a mensagem")
mensagem = input()
while mensagem not in ('s','S'):
    soquete.send(str(mensagem).encode())
    mensagem = input()
