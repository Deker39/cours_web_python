import socket
import threading
import time
from datetime import datetime

nick = input("Enter nickname: ")
password = input("Enter pass: ")
sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message == 'NICKNAME':
                sock.send(str([nick, password]).encode('utf-8'))
            elif message == 'REPEATPASS':
                sock.send(str(input("Enter pass: ")).encode('utf-8'))
            elif message == 'REPEATNICK':
                sock.send(str(input("Enter nickname: ")).encode('utf-8'))
            else:
                print(message)
                write_th = threading.Thread(target=write)
                write_th.start()
        except:
            print("Error")
            sock.close()
            break


def write():
    while True:
        message = input('')
        date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        sock.send(f'[{date_now}] {nick}: {message}'.encode('utf-8'))

        if message == 'q':
            break


receive_th = threading.Thread(target=receive)
receive_th.start()
