# -*- coding: utf-8 -*-
from tornado import websocket, web, ioloop, httpserver, tcpserver
import socket
import json
import udpserver
from PositionPoint import PositionPoint
from db import setup_position_db_log, get_db_connection, db_write, insert_log
import logging
logging.basicConfig(filename='server.log',level=logging.INFO)

clients = {}
cars = {}


def bc_clients():
    if len(cars) == 0:
        return
    amap_msg = json.dumps([{"name": name, "pos": cars[name].export_amap() } for name in cars])
    google_msg = json.dumps([{"name": name, "pos": cars[name].export_google() } for name in cars])
    for client in clients:
        if clients[client] == "amap":
            client.write_message(amap_msg)
        elif clients[client] == "google":
            client.write_message(google_msg)

class WSBroadcastHandler(websocket.WebSocketHandler):
    """ Websockets for broswer clients. Amap/GoogleMap/BaiduDitu. """
    def open(self):
        map_provider = self.get_argument("map","amap")
        if map_provider in ["google","amap"]:
            clients[self] = map_provider
        else:
            # default using amap
            clients[self] = "amap"
        logging.info("new %r client:%s",map_provider,id(self))

    def on_message(self, message):
        print 'message received:  %s' % message

    def on_close(self):
        del clients[self]
        logging.info("client %s closed.",id(self))

    def check_origin(self, origin):
        return True


class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")


app = web.Application([
    (r"/", MainHandler),
    (r"/ws", WSBroadcastHandler),
])


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
    conn = get_db_connection()
    def handle_datagram(self,data, address):
        try:
            name,pt = decode_protocol(data)
            insert_log(name,pt.lng,pt.lat)
            cars[name] = pt
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
            cars[name] = pt
        except Exception as e:
            print "error",e,data
        self.stream.write("M")
        self.read_message()


class CollectServerTCP(tcpserver.TCPServer):
    def handle_stream(self,stream,address):
        CollectConnection(stream,address)


if __name__ == "__main__":
    setup_position_db_log()
    io_loop = ioloop.IOLoop.current()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8886, '0.0.0.0')

    broadcast_task = ioloop.PeriodicCallback(bc_clients, 1000) # 1s
    broadcast_task.start()

    db_write_task = ioloop.PeriodicCallback(db_write , 3300) # 3.3s
    db_write_task.start()

    collect_server_udp = CollectServerUDP()
    collect_server_udp.bind(8887, '0.0.0.0')
    collect_server_udp.start()

    collect_server_tcp = CollectServerTCP()
    collect_server_tcp.bind(8897, '0.0.0.0')
    collect_server_tcp.start()

    logging.info("server start")
    io_loop.start()
