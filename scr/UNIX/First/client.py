import socket
import re
from threading import *

sock = socket.socket()
sock.setblocking(True)
isOpen = False


def client():
    global isOpen
    adr = str(input('Введите адрес сервера = '))
    if re.search(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", adr):
        port = int(input('Введите порт сервера = '))
        if 1024 < port < 65535:
            sock.connect((adr, port))
            isOpen = True
            print("Подключение установленно")
            while True:
                msg = input()
                sock.send(msg.encode())

                if msg == "exit":
                    break
        else:
            print("Не верный Порт")
    else:
        print("Не верный IP")


def server():
    global isOpen
    while True:
        if isOpen:
            data = sock.recv(1024)
            if data is not None or data != "":
                print(data.decode())


if __name__ == "__main__":
    client = Thread(target=client)
    server = Thread(target=server)

    client.start()
    server.start()
