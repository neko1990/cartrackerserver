# -*- coding: utf-8 -*-
from tornado import websocket, web, ioloop, httpserver
import socket
import json
import udpserver
import math
from CoordinateTransform import CoordinateTransform

ct = CoordinateTransform("54")
ll = 117 * math.pi / 180
delta_x = 513804.041 - 513269.1590
delta_y = 3788034.879 - 3788170.2160
clients = []
cars = {}


def bc_clients():
    msg = json.dumps([{"name": name, "pos": [cars[name][0], cars[name][1]]} for name in cars])
    for client in clients:
        client.write_message(msg)


class WSHandler(websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        clients.append(self)

    def on_message(self, message):
        print 'message received:  %s' % message

    def on_close(self):
        clients.remove(self)
        print 'connection closed'

    def check_origin(self, origin):
        return True


class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")


app = web.Application([
    (r"/", MainHandler),
    (r"/ws", WSHandler),
])


class CollectServer(udpserver.UDPServer):
    def handle_datagram(self, data, address):
        print data
        try:
            version, name, X, Y, ORI, V, ACC, T = data.split(',')
            x = float(X)+delta_x
            y = float(Y)+delta_y
            cars[name] =  ct.gauss_negative(y,x,ll).to_DFM()
            print cars[name]
        except Exception as e:
            print e


if __name__ == "__main__":
    io_loop = ioloop.IOLoop.current()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8886, '0.0.0.0')

    sched = ioloop.PeriodicCallback(bc_clients, 1000) # 1s
    sched.start()

    collect_server = CollectServer()
    collect_server.bind(8887, '0.0.0.0')
    collect_server.start()

    io_loop.start()
