import socket
import json
import hashlib
from threading import Thread

sock = socket.socket()
port = 9090
client_name = {}
client_auth = {}
clients_file_path = "clients.json"
pass_file_path = "pass.json"
logs = []


def save_log():
	with open("logs.txt", "w") as log_file:
		log_file.write("\n".join(logs))


def log(string):
	print(string)
	logs.append(string)
	save_log()


def is_port_in_use(port_):
	try:
		sock.bind(('', port_))
	except OSError:
		return True


def find_port():
	global port
	while is_port_in_use(port):
		port = port + 1
	log("Port is " + str(port))


find_port()
sock.listen(0)

clients = []
onRegister = []
onAuth = []


def save_clients():
	with open(clients_file_path, "w") as clients_file_:
		json.dump(client_name, clients_file_)


def save_pass(auth_):
	with open(pass_file_path, "w") as clients_file_:
		json.dump(auth_, clients_file_)


def listener(conn_m, addr_m):
	log("Register client")
	if register(conn_m, addr_m):
		msg = 'Привет ' + client_name.get(addr_m[0]) + "!"
		conn_m.send(msg.encode())
		log("SEND: " + addr_m[0] + ": " + msg)
		if auth(conn_m, addr_m):
			msg = 'Добро пожаловать, ' + client_name.get(addr_m[0]) + "!"
			conn_m.send(msg.encode())
			log("SEND: " + addr_m[0] + ": " + msg)
	else:
		if auth(conn_m, addr_m):
			msg = 'Добро пожаловать, ' + client_name.get(addr_m[0]) + "!"
			conn_m.send(msg.encode())
			log("SEND: " + addr_m[0] + ": " + msg)
	while True:
		try:
			msg = ''
			data = conn_m.recv(1024)
			if data is not None and data != "":
				msg += data.decode()
				if conn_m in onRegister:
					if addr_m[0] in client_name.keys():
						password = hashlib.md5(msg.encode('utf-8')).hexdigest()
						save_pass({addr_m[0]: password})
						onRegister.remove(conn_m)
						conn_m.send("Вы успешно зарегистрировались!".encode())
						continue
					client_name.setdefault(addr_m[0], msg)
					log("REGISTER: " + addr_m[0] + " AS " + msg)
					conn_m.send("Создайте Пароль:".encode())
					save_clients()
					continue
				if conn_m in onAuth:
					password = hashlib.md5(msg.encode('utf-8')).hexdigest()
					with open(pass_file_path, "d") as pass_file:
						if password == dict(json.load(pass_file))[addr_m[0]]:
							onAuth.remove(conn_m)
							conn_m.send("Вы успешно вошли!".encode())
						else:
							conn_m.send("Не верный пароль!".encode())
							continue
					client_auth.setdefault(addr_m[0], True)
					log("AUTH: " + addr_m[0] + " SUCCESS")
					continue
				if addr_m[0] in client_auth.keys() and client_auth[addr_m[0]]:
					log("RECEIVE: " + addr_m[0] + ": " + msg)
					conn_m.send("Вы: ".encode() + data)
					for client_each in clients:
						if client_each != conn_m:
							client_each.send(client_name[addr_m[0]].encode() + ": ".encode() + data)
					log("SEND: " + addr_m[0] + ": " + msg)
		except ConnectionResetError:
			continue
		except BrokenPipeError:
			continue


def register(conn_m, addr_m):
	if addr_m[0] not in client_name.keys():
		log("Register new client")
		msg = 'Введите имя:'
		conn_m.send(msg.encode())
		onRegister.append(conn_m)
		return False
	return True


def auth(conn_m, addr_m):
	if addr_m[0] not in client_auth.keys():
		log("Auth client")
		msg = 'Введите пароль:'
		conn_m.send(msg.encode())
		onAuth.append(conn_m)
		return False
	return True


if __name__ == '__main__':
	log("start server")
	log("load clients")
	with open(clients_file_path, "d") as clients_file:
		client_name = dict(json.load(clients_file))
	log("load success")
	while True:
		conn, addr = sock.accept()
		clients.append(conn)

		client = Thread(target=listener, args=(conn, addr))
		client.run()
