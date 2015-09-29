# -*- coding: utf-8 -*-

import socket
import time
import math

from CoordinateTransform import CoordinateTransform
import settings

UDP_IP = settings.EXTERNAL_IP
UDP_PORT = 8887

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

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
    for pos in get_poss():
        time.sleep(0.1)
        msg = ','.join(['V2', 'XHC#N1', str(pos[0]), str(pos[1]), "ORI", "V", "ACC", "TS"])
        print msg
        sock.sendto(msg, (UDP_IP, UDP_PORT))
