import socket
import threading
import time


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
        except:
            print("Error")
            sock.close()
            break


def write():
    while True:
        message = input('>> ')
        sock.send(f'{nick}: {message}'.encode('utf-8'))


receive_th = threading.Thread(target=receive)
receive_th.start()
receive_th.join()
## TODO СДЕЛАТЬ ТАК ЧТОБЫ ВТОРОЙ ПОТОК ЖДАЛ ПОКА НЕ ВЫПОЛНЕТЬСЯ ПЕРВЫЙ
write_th = threading.Thread(target=write)
write_th.start()


write()
