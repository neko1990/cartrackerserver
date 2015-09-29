from tornado import tcpserver
import logging

from db import get_db_connection
from db import insert_log

import udpserver
from PositionPoint import PositionPoint


def decode_protocol(data):
    pts = data[:-1].strip().split(",")
    version = pts[0]
    if version == "V1":
        name = pts[1]
        X = float(pts[2])
        Y = float(pts[3])
        pt = PositionPoint().set_xy(X,Y)
    elif version == "V2":
        name = pts[1]
        lng = float(pts[2])
        lat = float(pts[3])
        pt = PositionPoint().set_lnglat(lng,lat)
    elif version == "V3":
        name = pts[1]
        lng_d = float(pts[2][:3])
        lng_m = float(pts[2][3:])
        lng = lng_d + lng_m / 60
        lat_d = float(pts[3][:2])
        lat_m = float(pts[3][2:])
        lat = lat_d + lat_m / 60
        pt = PositionPoint().set_lnglat(lng,lat)
    else:
        raise Exception("unknown version "+version)
    return name,pt


class CollectServerUDP(udpserver.UDPServer):
    ## conn = get_db_connection()
    def handle_datagram(self,data, address):
        try:
            name,pt = decode_protocol(data)
            insert_log(name,pt.lng,pt.lat)
            # cars[name] = pt
        except Exception as e:
            print "error",e,data


class CollectConnection:
    tcp_devices = set()
    def __init__(self,stream,address):
        self.stream = stream
        if self.stream.socket.family not in (socket.AF_INET, socket.AF_INET6):
            # Unix (or other) socket; fake the remote address
            address = ('0.0.0.0', 0)
        self.address = address
        self.stream.set_close_callback(self._on_disconnect)

        CollectConnection.tcp_devices.add(self)
        logging.info('incoming device connection from %r', address)

        self.read_message()

    def _on_disconnect(self):
        logging.info('%r leaves',self.address)
        CollectConnection.tcp_devices.remove(self)

    def read_message(self):
        self.stream.read_until('*',self.record_position)

    def record_position(self,data):
        try:
            name,pt = decode_protocol(data)
            insert_log(name,pt.lng,pt.lat)
            # cars[name] = pt
        except Exception as e:
            print "error",e,data
        self.stream.write("M")
        self.read_message()


class CollectServerTCP(tcpserver.TCPServer):
    def handle_stream(self,stream,address):
        CollectConnection(stream,address)
