# Script do Cliente

import socket

server_ip = '127.0.0.1'
porta = 2024

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((server_ip, porta))
    s.sendall(b'Ola Mundo')
    data = s.recv(1024)

print('Recebido', repr(data))
