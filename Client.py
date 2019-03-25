# Script do Cliente

import socket

server_ip = '170.238.73.10'
porta = 6202

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((server_ip, porta))
        msg = input('Digita a mensagem: ')
        s.sendall(msg.encode())
        data = s.recv(1024)

    print(repr(data.decode()))
