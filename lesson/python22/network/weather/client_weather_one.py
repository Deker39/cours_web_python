import socket
import threading
import time

city = input("Enter city: ")

sock = socket.socket()
HOST = '127.0.0.1'
PORT = 9999
sock.connect((HOST, PORT))


def receive():
    while True:
        try:
            message = sock.recv(1024).decode('utf-8')
            if message == 'CITY':
                sock.send(city.encode('utf-8'))

            else:
                print(message)
                new_city = input("Enter city: ")
                sock.send(new_city.encode('utf-8'))
        except:
            print("Error")
            sock.close()
            break

#
# def write():
#     while True:
#         new_city = input("Enter city: ")
#         sock.send(new_city.encode('utf-8'))


receive_th = threading.Thread(target=receive)
receive_th.start()

# write_th = threading.Thread(target=write)
# write_th.start()
# write()
