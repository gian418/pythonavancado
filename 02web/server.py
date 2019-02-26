from socket import *

meuHost = ''
minhaPorta = 50007
sockobj = socket(AF_INET, SOCK_STREAM) #voce esta usando um servidor tcp/ip
sockobj.bind((meuHost, minhaPorta))
sockobj.listen(5)

while True:
    conexao, endereco = sockobj.accept()
    print('O servidor esta conectado por', endereco)

    while True:
        data = conexao.recv(1024)
        if not data:
            break
        conexao.send(b'Eco=>' + data)

    conexao.close()
