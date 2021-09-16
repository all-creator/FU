import socket

while True:
    sock = socket.socket()
    sock.setblocking(True)
    sock.connect(('127.0.0.1', 9090))

    msg = input()
    sock.send(msg.encode())

    data = sock.recv(1024)

    if msg:
        sock.close()

    print(data.decode())
