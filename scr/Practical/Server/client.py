import socket
import re
from threading import Thread

sock = socket.socket()
sock.setblocking(True)
main_port = 9090
isOpen = False


def client():
    adr = str(input('Введите адрес сервера = '))
    if re.search(d"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", adr):
        port = input('Введите порт сервера = ')
        if port != "" and 1024 < int(port) < 65535:
            client_connection(adr, int(port))
        else:
            print("Не верный Port использую "+str(main_port))
            client_connection(adr, main_port)
    else:
        print("Не верный IP")


def client_connection(adr, port):
    global isOpen
    sock.connect((adr, port))
    print("Подключение установленно")
    isOpen = True
    while True:
        msg = input()
        sock.send(msg.encode())
        if msg == "exit":
            break


def server():
    global isOpen
    while True:
        if isOpen:
            data = sock.recv(1024)
            if data is not None and data != "":
                print(data.decode())


if __name__ == "__main__":
    client = Thread(target=client)
    server = Thread(target=server)

    client.start()
    server.start()
