import socket as s
from time import time
# import fcntl
# import os
HOST = '127.0.0.1'
PORT = 8080
start_time = time()
it_time = time()
s.timeout(1)
sock = s.socket(s.AF_INET, s.SOCK_STREAM)
sock.connect((HOST, PORT))
sock.setblocking(0)
# fcntl.fcntl(sock, fcntl.F_SETFL, os.O_NONBLOCK)
sock.send(b'pidor')
try:
	while True:
		if time() - it_time > 1:
			sock.send(b'ok\n')
			it_time = time()
		try:
			data = sock.recv(1024)
			if data:
				print(data.decode("utf-8"))
		except BlockingIOError:
			pass
		#	print(*data, sep="\n", end="\n\n\n\n\n")
		if time() - start_time > 65:
			sock.close()
			raise KeyboardInterrupt
except KeyboardInterrupt:
	sock.send(b'bye\n')
	sock.close()
