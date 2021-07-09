from socket import *

from time import sleep
nomeServidor = '192.0.2.20'

portaServidor = 12000

socketCliente = socket (AF_INET, SOCK_STREAM)

socketCliente.connect ((nomeServidor, portaServidor))

# Python 3
matricula = raw_input('Informe a sua matricula: ')
socketCliente.send(matricula.encode())

namefile =raw_input("Informe o nome do arquivo referente ao municipio de pesquisa: ")

socketCliente.send(namefile.encode())
sleep(1)
with open(namefile,'rb') as file:
	for data in file.readlines():
		socketCliente.send(data)
print('Arquivo enviado')

