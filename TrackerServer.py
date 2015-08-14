# -*- coding: utf-8 -*-
from tornado import websocket, web, ioloop, httpserver
import socket
import json
import udpserver
from PositionPoint import PositionPoint
from db import setup_position_db_log, get_db_connection, db_write, insert_log

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
    def open(self):
        map = self.get_argument("map","amap")
        if map in ["google","amap"]:
            clients[self] = map
        else:
            # default using amap
            clients[self] = "amap"

    def on_message(self, message):
        print 'message received:  %s' % message

    def on_close(self):
        del clients[self]
        print 'connection closed'

    def check_origin(self, origin):
        return True


class MainHandler(web.RequestHandler):
    def get(self):
        self.write("Hello, world")


app = web.Application([
    (r"/", MainHandler),
    (r"/ws", WSBroadcastHandler),
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
                pt = PositionPoint().set_xy(X,Y)
                insert_log(name,pt.lng,pt.lat)
                cars[name] = pt
            elif version == "V2":
                name = pts[1]
                lng = float(pts[2])
                lat = float(pts[3])
                pt = PositionPoint().set_lnglat(lng,lat)
                insert_log(name,lng,lat)
                cars[name] = pt
            elif version == "V3":
                name = pts[1]
                lng_d = float(pts[2][:3])
                lng_m = float(pts[2][3:])
                lng = lng_d + lng_m / 60
                lat_d = float(pts[3][:2])
                lat_m = float(pts[3][2:])
                lat = lat_d + lat_m / 60
                pt = PositionPoint().set_lnglat(lng,lat)
                insert_log(name,lng,lat)
                cars[name] = pt
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
