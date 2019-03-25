# Script do Cliente_ChatRoom

import socket
import threading

BUFFSIZE = 1024


def receber_msg():
    while True:
        try:
            msg_rec = CLIENT.recv(BUFFSIZE).decode()
            if msg_rec:
                print(msg_rec)
        except OSError:
            break


def enviar_msg():
    while True:
        msg_a_enviar = str(input())
        if msg_a_enviar == '[exit]':
            CLIENT.send(msg_a_enviar.encode())
            CLIENT.close()
            break
        else:
            CLIENT.send(msg_a_enviar.encode())


server_ip = '127.0.0.1'
porta = 2024

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect((server_ip, porta))

RECEBER_THR = threading.Thread(target=receber_msg).start()
ENVIAR_THR = threading.Thread(target=enviar_msg).start()

