import socket
import time

sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.bind((HOST, PORT))
sock.listen()
conn, addr = sock.accept()
print(f'connection: {addr}')

while True:
    time.sleep(1)
    data = conn.recv(1024)
    if not data:
        break

    conn.send(data.upper())
    print(data)

conn.close()