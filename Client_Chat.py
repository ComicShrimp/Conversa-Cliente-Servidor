# Script do Cliente_ChatRoom

import socket
import threading as Thread

BUFFSIZE = 1024


def receber_msg():
    while True:
        try:
            print(CLIENT.recv(BUFFSIZE).decode())
        except OSError:
            break


def enviar_msg():
    while True:
        CLIENT.send(bytes(input()))


server_ip = '127.0.0.1'
porta = 2024

CLIENT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
CLIENT.connect((server_ip, porta))

RECEBER_THR = Thread(target=receber_msg).start()
ENVIAR_THR = Thread(target=enviar_msg).start()

RECEBER_THR.join()
ENVIAR_THR.join()

CLIENT.close()
