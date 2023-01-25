import  socket
import time

sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.connect((HOST, PORT))
sock.send('hello'.encode('utf-8'))
data = sock.recv(1024)
sock.close()
print(data)