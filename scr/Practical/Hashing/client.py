import socket
from security import *


def gen(i_, key_prim, key_publ_m):
    global flag
    while i_ < 3:
        i_ += 1
        if i_ == 1:
            msg = str(key_publ_m)
            sock.send(msg.encode())
            try:
                key_publ_s = int(sock.recv(1024))
            except ValueError:
                print("You key is invalid.")
                flag = False
                break
        if i_ == 2:
            key_part_m = calc_part_key(key_publ_m, key_prim, key_publ_s)
            msg = str(key_part_m)
            sock.send(msg.encode())
            key_part_s = int(sock.recv(1024))
        if i_ == 3:
            key_full_m = calc_full_key(key_part_s, key_prim, key_publ_s)
            print(key_part_s, key_prim, key_publ_s)
            msg = str(key_full_m)
            sock.send(msg.encode())
            key_full_s = int(sock.recv(1024))
            print(key_full_s)
            with open('keys_c.txt', 'w') as f:
                f.write(str(key_full_s))
    return key_full_s


def mess(sock, key_full_m):
    msg = input('m from you:\t')
    msg_new = coding(msg, key_full_m)
    sock.send(msg_new.encode())
    msg = sock.recv(1024).decode()
    msg_new = decoding(msg, key_full_m)
    print('m from server:\t', msg_new)
    return msg_new


flag = True

sock = socket.socket()

sock.setblocking(True)
sock.connect(('localhost', 9090))
print('connection')
try:
    with open('keys_c.txt', 'd') as f:
        for line in f:
            key_full_s = int(line)
except Exception:
    key_prim = 199
    key_publ_m = 197
    i = 0
    msg = ''
    key_full_s = gen(i, key_prim, key_publ_m)

if flag:
    port = mess(sock, key_full_s)
    sock.close()
    sock = socket.socket()
    sock.connect(('localhost', 1024))
    while True:
        mess(sock, key_full_s)
sock.close()
