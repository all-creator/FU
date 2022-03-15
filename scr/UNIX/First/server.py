import socket
from threading import Thread

sock = socket.socket()
sock.bind(('', 9090))
sock.listen(0)

clients = []


def listener(conn_m, addr_m):
	print("Register new client")
	while True:
		msg = ''
		data = conn_m.recv(1024)
		msg += data.decode()
		conn_m.send("Вы: ".encode() + data)
		for client_each in clients:
			if client_each != conn_m:
				client_each.send(str(addr_m[0]).encode() + ": ".encode() + data)
		print("LOG: " + addr_m[0] + ": " + msg)


print("start server")
while True:
	conn, addr = sock.accept()
	clients.append(conn)
	client = Thread(target=listener, args=(conn, addr))
	client.run()
