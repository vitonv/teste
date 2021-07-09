from socket import *

portaServidor = 12000

socketServidor = socket (AF_INET, SOCK_STREAM)

socketServidor.bind (('', portaServidor))

socketServidor.listen (1)

# Python 2
# print "O servidor esta pronto para receber"

# Python 3
print ("O servidor esta pronto para receber")

while 1:

    socketConexao, endereco = socketServidor.accept ()
    matricula = socketConexao.recv(1024). decode()
    namefile  = socketConexao.recv(1024). decode()
    with open(matricula+namefile,'wb') as file:
      while 1:
      	data = socketConexao.recv(100000)
      	if not data:
        	break
        file.write(data)
    print("Arquivo recebido")

socketConexao.close ()
