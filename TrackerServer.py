# -*- coding: utf-8 -*-
from tornado import websocket, web, ioloop, httpserver
import socket
import json
import udpserver
from PositionPoint import PositionPoint

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
    def handle_datagram(self,data, address):
        try:
            pts = data.split(",")
            version = pts[0]
            if version == "V1":
                name = pts[1]
                X = float(pts[2])
                Y = float(pts[3])
                res = PositionPoint().set_xy(X,Y).export_amap()
                cars[name] =  res
            elif version == "V2":
                name = pts[1]
                Lng = float(pts[2])
                Lat = float(pts[3])
                res = PositionPoint().set_lnglat(Lng,Lat).export_amap()
                cars[name] = res
        except Exception as e:
            print "error",e,data


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
