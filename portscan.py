import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('bancocn.com', 80))
cliente.send('mensagemexibida\n\n')
resposta = cliente.recv(1024)
print resposta
