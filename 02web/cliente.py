from socket import *

serverHost = 'localhost'
serverPorta = 50007
mensagem = [b'Ola, bem vindo!']

sockobj = socket(AF_INET, SOCK_STREAM) #voce esta usando um servidor tcp/ip
sockobj.connect((serverHost, serverPorta))

for linha in mensagem:
    sockobj.send(linha)
    data = sockobj.recv(1024)
    print('Cliente recebeu: ', data)


sockobj.close()
