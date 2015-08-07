# -*- coding: utf-8 -*-
from __future__ import division

from CoordinateTransform import CoordinateTransform
import math


class PositionPoint:
    ct54 = CoordinateTransform("54")
    ll = 117 * math.pi / 180

    def __init__(self):
        self.lng = None   # 117.14112364303995
        self.lat = None   # 34.210311754345234
        self.x = None     # 512470.64572097437
        self.y = None     # 3787203.674106625


    def set_xy(self,x,y):
        self.x = x
        self.y = y
        return self


    def set_lnglat(self,lng,lat):
        self.lng = lng
        self.lat = lat
        return self


    def lnglat2xy(self):
        lng = self.lng * math.pi / 180
        lat = self.lat * math.pi / 180
        self.x , self.y = self.ct54.gauss_positive(lat,lng,self.ll)
        return self


    def xy2lnglat(self):
        self.lng , self.lat = self.ct54.gauss_negative(self.y,self.x,self.ll)
        return self


    def export_amap(self):
        """ Amap offset is (534.882, -135.337)"""
        if self.x is None:
            self.lnglat2xy()
        x = self.x + 534.882
        y = self.y + -135.337
        return self.ct54.gauss_negative(y,x,self.ll)
