# -*- coding: utf-8 -*-
from tornado import websocket, web, ioloop, httpserver, tcpserver
import socket
import json
import logging
logging.basicConfig(filename='server.log',level=logging.INFO)

from db import setup_position_db_log
from db import db_write
from db import insert_log
from db import get_cars

from Collector import CollectServerTCP
from Collector import CollectServerUDP

# TODO: ugly global variable, eliminate them
clients = {}

def bc_clients():
    if len(cars) == 0:
        return
    cars = get_cars():
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

def TCPBroadcastConnection(stream,address):
    tcp_clients = set()
    def __init__(self,stream,address):
        self.stream = stream
        if self.stream.socket.family not in (socket.AF_INET, socket.AF_INET6):
            # Unix (or other) socket; fake the remote address
            address = ('0.0.0.0', 0)
        self.address = address
        self.stream.set_close_callback(self._on_disconnect)

        clients[self.stream] = "tcp"
        CollectConnection.tcp_clients.add(self)
        logging.info('client %r connected', address)
        self.stream.write_message = self.stream.write    # fix interface issue

    def _on_disconnect(self):
        del clients[self.stream]
        CollectConnection.tcp_devices.remove(self)
        logging.info('client %r disconnected',self.address)

class TCPBroadcastHandler(tcpserver.TCPServer):
    def handle_stream(self,stream,address):
        TCPBroadcastConnection(stream,address)

class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")

app = web.Application([
    (r"/", MainHandler),
    (r"/ws", WSBroadcastHandler),
])

if __name__ == "__main__":
    setup_position_db_log()

    # Main Webserver Handler
    # TODO: merge pages and js files
    io_loop = ioloop.IOLoop.current()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8886, '0.0.0.0')
    logging.info("Ready to server tcp clients on port 8885")

    # Periodic Tasks
    broadcast_task = ioloop.PeriodicCallback(bc_clients, 1000) # 1s
    broadcast_task.start()
    db_write_task = ioloop.PeriodicCallback(db_write , 3300) # 3.3s
    db_write_task.start()

    # Server TCP clients
    tcp_broadcast_handler = TCPBroadcastHandler()
    tcp_broadcast_handler.bind(8885,'0.0.0.0')
    tcp_broadcast_handler.start()
    logging.info("ready to server tcp clients on port 8885")

    # Collector Servers
    collect_server_udp = CollectServerUDP()
    collect_server_udp.bind(8887, '0.0.0.0')
    collect_server_udp.start()
    logging.info("ready to collect udp packets from cars on port 8887.")

    collect_server_tcp = CollectServerTCP()
    collect_server_tcp.bind(8897, '0.0.0.0')
    collect_server_tcp.start()
    logging.info("ready to handle tcp connections from cars on port 8897.")

    logging.info("server start!")
    io_loop.start()
