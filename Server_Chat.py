# Script do Servidor_ChatRoom

import socket
import threading

server_ip = '127.0.0.1'
porta = 2024


def accept_connection():
    # Função Responsavel por receber as novas conexões.
    while True:
        cliente, cliente_addr = SERVER.accept()
        print("{} Conectou-se ao servidor.".format(cliente_addr))
        cliente.send(bytes('Seja Bem Vindo ao chat !!!, Digite seu nome para começar.'.encode()))
        addr_list[cliente] = cliente_addr
        threading.Thread(target=handle_client, args=(cliente,)).start()


def handle_client(cliente):
    #Classe para lidar com clientes
    nome = cliente.recv(1024).decode()
    cliente.send(bytes("Olá {}, Atenção, se quiser  sair do chat, digite [exit].".format(nome).encode()))
    msg_todos(bytes("{} Entrou no chat !!!".format(nome).encode()))
    clientes[cliente] = nome

    while True:
        msg = cliente.recv(1024)
        msg_todos(msg, nome + " : ")


def msg_todos(msg, nome=""):
    # Manda a mensagem para todos conectados à sala
    for socket in clientes:
        socket.send(bytes(nome.encode()) + msg)


clientes = {}
addr_list = {}

# A linha abixo inicializa o socket com o protocolo ipv4(AF_INET) e tcp(SOCK_STREAM).
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.bind((server_ip, porta))
print('Servidor Iniciado')



# No listen também pode ser passado o parâmetro de numero de conexões simultaneas.
# Faz com que a porta passe a ser de escuta, e o permite aceitar conexões(Accept logo abaixo).
SERVER.listen(5)
print('Aguardando Conexões')

ACCEPT_THREAD = threading.Thread(target=accept_connection())
ACCEPT_THREAD.start()
ACCEPT_THREAD.join()
SERVER.close()
