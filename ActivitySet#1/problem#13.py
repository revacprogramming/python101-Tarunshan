# Network Programming
# https://www.py4e.com/lessons/network
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "www.data.pr4e.org"
PORT = 80
mysock.connect((HOST, PORT))
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\n\n".encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
