import socket
import time
import math
from CoordinateTransform import CoordinateTransform

#UDP_IP = "106.185.49.44"
#UDP_IP = "180.123.137.237"
UDP_IP = "127.0.0.1"
UDP_PORT = 8887

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

def get_poss():
    ll = 117 * math.pi / 180
    delta_x = 513804.041 - 513269.1590
    delta_y = 3788034.879 - 3788170.2160
    ct = CoordinateTransform("54")
    with open('input.txt','r') as f:
        lines = f.readlines()
    for line in lines:
        x,y = line.strip().split()
        sp  = ct.gauss_negative(float(y)+delta_y,float(x)+delta_x,ll)
        yield [x,y]

if __name__ == "__main__":
    for pos in get_poss():
        time.sleep(0.1)
        # msg = json.dumps({"name":"XHC#1","pos":[pos[0],pos[1]]})
        msg = ','.join(['V1', 'XHC#1', str(pos[0]), str(pos[1]), "ORI", "V", "ACC", "TS"])
        print msg
        sock.sendto(msg, (UDP_IP, UDP_PORT))
