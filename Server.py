# Script do Servidor

import socket

server_ip = '127.0.0.1'
porta = 2024

# A linha abixo inicializa o socket com o protocolo ipv4(AF_INET) e tcp(SOCK_STREAM).
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((server_ip, porta))
    print('Servidor Iniciado')

    # No listen também pode ser passado o parâmetro de numero de conexões simultaneas.
    # Faz com que a porta passe a ser de escuta, e o permite aceitar conexões(Accept logo abaixo).
    s.listen()

    # Accept "Trava" o programa até que ele receba uma conexão.
    # O socket que é usado para poder escutar, é diferente do socket de comunicação, por isso o conn
    while True:
        conn, addr = s.accept()
        print('Conectado à', addr)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            num_letras = 'O tamanho da string recebida é : {}'.format(len(data.decode()))
            conn.sendall(num_letras.encode())
