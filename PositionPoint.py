# -*- coding: utf-8 -*-
from __future__ import division

from CoordinateTransform import CoordinateTransform
import math


class PositionPoint:
    ct54 = CoordinateTransform("54")

    def __init__(self):
        self.lng = None
        self.lat = None
        self.x = None
        self.y = None
        # TODO 高斯坐标和经纬度坐标应该分成两个类
        self.set_l0(117) # default 117

    def set_l0(self,l0):
        self.ll = l0 * math.pi / 180
        return self

    def set_xy(self,x,y):
        self.x = x
        self.y = y
        self._xy2lnglat()
        return self


    def set_lnglat(self,lng,lat):
        self.lng = lng
        self.lat = lat
        self.set_l0(round(self.lng / 3.0) * 3)
        return self


    def _lnglat2xy(self):
        lng = self.lng * math.pi / 180
        lat = self.lat * math.pi / 180
        self.x , self.y = self.ct54.gauss_positive(lat,lng,self.ll)
        return self


    def _xy2lnglat(self):
        self.lng , self.lat = self.ct54.gauss_negative(self.y,self.x,self.ll)
        return self


    def export_amap(self):
        """ Amap offset is (534.882, -135.337)"""
        if self.x is None:
            self._lnglat2xy()
        x = self.x + 534.882
        y = self.y + -135.337
        return self.ct54.gauss_negative(y,x,self.ll)

    def export_google(self):
        if self.lng is None:
            self._xy2lnglat()
        return [self.lng,self.lat]
