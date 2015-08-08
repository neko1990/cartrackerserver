# -*- coding: utf-8 -*-
from tornado import websocket, web, ioloop, httpserver
import socket
import json
import udpserver
from PositionPoint import PositionPoint
from db import setup_position_db_log, get_db_connection, db_write, insert_log

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
    conn = get_db_connection()
    def handle_datagram(self,data, address):
        try:
            pts = data.split(",")
            version = pts[0]
            if version == "V1":
                name = pts[1]
                X = float(pts[2])
                Y = float(pts[3])
                res = PositionPoint().set_xy(X,Y).export_amap()
                insert_log(name,res[0],res[1])
                cars[name] =  res
            elif version == "V2":
                name = pts[1]
                lng = float(pts[2])
                lat = float(pts[3])
                res = PositionPoint().set_lnglat(lng,lat).export_amap()
                insert_log(name,lng,lat)
                cars[name] = res
        except Exception as e:
            print "error",e,data


if __name__ == "__main__":
    setup_position_db_log()
    io_loop = ioloop.IOLoop.current()
    http_server = httpserver.HTTPServer(app)
    http_server.listen(8886, '0.0.0.0')

    broadcast_task = ioloop.PeriodicCallback(bc_clients, 1000) # 1s
    broadcast_task.start()

    db_write_task = ioloop.PeriodicCallback(db_write , 3300) # 3.3s
    db_write_task.start()

    collect_server = CollectServer()
    collect_server.bind(8887, '0.0.0.0')
    collect_server.start()

    io_loop.start()
