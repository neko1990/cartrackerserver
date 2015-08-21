# -*- coding: utf-8 -*-

import socket
import time
import math
from CoordinateTransform import CoordinateTransform

#SERVER_IP = "106.185.49.44"
#SERVER_IP = "180.123.139.174"
SERVER_IP = "127.0.0.1"
UDP_PORT = 8887
TCP_PORT = 8897


def get_poss():
    ct = CoordinateTransform("54")
    ll = 117 * math.pi / 180
    with open('input.txt','r') as f:
        lines = f.readlines()
    for line in lines:
        x,y = line.strip().split()
        sp  = ct.gauss_negative(float(y),float(x),ll)
        yield sp

if __name__ == "__main__":
    server_address = (SERVER_IP,TCP_PORT)
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(server_address)
    for c,pos in enumerate(get_poss()):
        # if c > 50:
        #     break
        time.sleep(0.01)
        msg = ','.join(['V2', 'TCP_V2', str(pos[0]), str(pos[1]), "ORI", "V", "ACC", "TS"])+'\n'
        try:
            sock.sendall(msg)
            data = sock.recv(10)
            print data
        except Exception as e:
            print e
    sock.close()
