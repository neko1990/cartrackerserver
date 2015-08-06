# -*- coding: utf-8 -*-
from tornado import websocket, web, ioloop, httpserver
import socket
import json
import udpserver

clients = []
cars = {}


def render_cars():
    msg = json.dumps([{"name": name, "pos": [cars[name][0], cars[name][1]]} for name in cars])
    return msg


def bc_clients():
    for client in clients:
        client.write_message(render_cars())


class WSHandler(websocket.WebSocketHandler):
    def open(self):
        print 'new connection'
        clients.append(self)
        self.write_message(render_cars())

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
            cars[name] = [float(X), float(Y)]
        except Exception as e:
            print e
        bc_clients()


if __name__ == "__main__":
    io_loop = ioloop.IOLoop.current()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8886, '0.0.0.0')

    collect_server = CollectServer()
    collect_server.bind(8887, '0.0.0.0')

    collect_server.start()
    io_loop.start()
