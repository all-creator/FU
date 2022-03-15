import socket
import re
from threading import Thread

sock = socket.socket()
sock.setblocking(True)
isOpen = False
main_port = -1
is_find_port = True
ports = [i for i in range(1024, 65535)]
thead_count = 0


def client():
    global isOpen, is_find_port
    adr = str(input('Введите адрес сервера = '))
    if re.search(d"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", adr):
        find_port(adr)
        while is_find_port:
            continue
        sock.connect((adr, main_port))
        isOpen = True
        print("Подключение установленно")
        while True:
            msg = input()
            sock.send(msg.encode())
            if msg == "exit":
                break
    else:
        print("Не верный IP")


def find_port(adr):
    global thead_count
    cof = 100
    for i in range(1024, 65535, cof):
        cof_i = i+cof if i+cof <= 65535 else 65535
        #print("Запускаю поток: " + str(i_) + ", " + str(cof_i))
        thead_count += 1
        #print("Кол-во потоков: " + str(thead_count))
        find = Thread(target=find_port_from_to, args=(adr, i, cof_i))
        find.start()


def find_port_from_to(adr, st, fn):
    global main_port, is_find_port, thead_count
    for port in range(st, fn):
        if not is_find_port:
            break
        if port == 65534:
            is_find_port = False
        try:
            sock.connect((adr, port))
            print("Найден порт: " + str(port))
            main_port = port
            is_find_port = False
        except socket.error:
            continue
    thead_count -= 1


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
