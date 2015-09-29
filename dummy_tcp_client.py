import socket
import settings

TCP_IP = settings.EXTERNAL_IP
TCP_PORT = 8885
BUFFER_SIZE = 1024

MESSAGE = "Hello Server"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print TCP_IP,TCP_PORT
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
while True:
    data = s.recv(BUFFER_SIZE)
    print data
