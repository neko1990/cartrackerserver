import socket
import time
import math

import settings

UDP_IP = settings.EXTERNAL_IP
UDP_PORT = 8887

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

def get_poss():
    with open('input.txt','r') as f:
        lines = f.readlines()
    for line in lines:
        x,y = line.strip().split()
        yield [x,y]

if __name__ == "__main__":
    for pos in get_poss():
        time.sleep(0.1)
        # V1,XHC#1,512470.64375693223,3787205.153150127,ORI,V,ACC,TS
        msg = ','.join(['V1', 'XHC#1', str(pos[0]), str(pos[1]), "ORI", "V", "ACC", "TS"])
        print msg
        sock.sendto(msg, (UDP_IP, UDP_PORT))
