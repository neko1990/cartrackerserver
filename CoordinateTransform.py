# -*- coding: utf-8 -*-
import math
class StationPoint:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def to_DFM(self):
        x = str(self.x)
        xdd = int(x[0:3])
        xmm = int(x[3:5])
        xss = float(x[5:])
        xx = xdd+xmm/60.0+xss/3600.0;
        y = str(self.y)
        ydd = int(y[0:2])
        ymm = int(y[2:4])
        yss = float(y[4:])
        yy = ydd+ymm/60.0+yss/3600.0;
        return [xx,yy]

class CoordinateTransform:
    def __init__(self,e):
        if e=="54":
            self.a = 6378245.0
            self.f =  1/298.3
            self.e2 = 0.006693421622966
        elif e=="80":
            self.a = 6378140.0; #西安80椭球 IGA75
            self.f = 1/298.257; #西安80椭球 IGA75   扁率
            self.e2 = 0.006694384999588; #第一偏心率平方
        elif e=="84":
            self.a=6378137.0
            self.f=1/298.257223563
            self.e2=0.0066943799013
        else:
            raise Exception("Unknow e")

    def gauss_positive(self, B, L, L0):
        e2 = self.e2
        a = self.a

        m0 = a * (1 - e2);
        m2 = 3.0 / 2 * e2 * m0;
        m4 = 5.0 / 4 * e2 * m2;
        m6 = 7.0 / 6 * e2 * m4;
        m8 = 9.0 / 8 * e2 * m6;
        a0 = m0 + m2 / 2 + (3.0 / 8.0) * m4 + (5.0 / 16.0) * m6 + (35.0 / 128.0) * m8;
        a2 = m2 / 2 + m4 / 2 + 15.0 / 32 * m6 + 7.0 / 16 * m8;
        a4 = m4 / 8 + 3.0 / 16 * m6 + 7.0 / 32 * m8;
        a6 = m6 / 32 + m8 / 16;
        a8 = m8 / 128;
        xx = 0.0;
        yy = 0.0;

        l = L - L0;
        X = a0 * B - math.sin(B) * math.cos(B) * ((a2 - a4 + a6) + (2 * a4 - 16.0 / 3.0 * a6) * math.sin(B) * math.sin(B) + 16.0 / 3.0 * a6 * (math.sin(B) ** 4)) + a8 / 8.0 * math.sin(8 * B);
        t = math.tan(B);
        h2 = e2 / (1 - e2) * math.cos(B) * math.cos(B);
        N = a / math.sqrt(1 - e2 * math.sin(B) * math.sin(B));
        m = math.cos(B) * l;
        xx = X + N * t * ((0.5 + (1.0 / 24.0 * (5 - t * t + 9 * h2 + 4 * h2 * h2) + 1.0 / 720.0 * (61 - 58 * t * t + (t ** 4)) * m * m) * m * m) * m * m);
        yy = N * ((1 + (1.0 / 6.0 * (1 - t * t + h2) + 1.0 / 120.0 * (5 - 18 * t * t + (t ** 4) + 14 * h2 - 58 * h2 * t * t) * m * m) * m * m) * m);
        yy = yy + 500000;
        return StationPoint(yy,xx)

    def gauss_negative(self, x, y ,L0):
        e2 = self .e2
        a = self.a
        f = self.f
        def calculateBf(x):
            currf = f;   #扁率
            currb = a * (1 - currf);   #b,短半轴
            e2 = (a * a - currb * currb) / (a * a);   #e的平方
            e4 = e2 * e2;
            e6 = e2 * e2 * e2;
            e8 = (e2 ** 4);
            e10 = (e2 ** 5);
            e12 = (e2** 6);
            e14 = (e2** 7);
            e16 = (e2** 8);
            c0 = 1 + e2 / 4 + 7 * e4 / 64 + 15 * e6 / 256 + 579 * e8 / 16384 + 1515 * e10 / 65536 + 16837 * e12 / 1048576 + 48997 * e14 / 4194304 + 9467419 * e16 / 1073741824;
            c0 = a / c0;

            b0 = x / c0;
            d1 = 3 * e2 / 8 + 45 * e4 / 128 + 175 * e6 / 512 + 11025 * e8 / 32768 + 43659 * e10 / 131072 + 693693 * e12 / 2097152 + 10863435 * e14 / 33554432;
            d2 = -21 * e4 / 64 - 277 * e6 / 384 - 19413 * e8 / 16384 - 56331 * e10 / 32768 - 2436477 * e12 / 1048576 - 196473 * e14 / 65536;
            d3 = 151 * e6 / 384 + 5707 * e8 / 4096 + 53189 * e10 / 163840 + 4599609 * e12 / 655360 + 15842375 * e14 / 1048576;
            d4 = -1097 * e8 / 2048 - 1687 * e10 / 640 - 3650333 * e12 / 327680 - 114459079 * e14 / 27525120;
            d5 = 8011 * e10 / 1024 + 874457 * e12 / 98304 + 216344925 * e14 / 3670016;
            d6 = -682193 * e12 / 245760 - 46492223 * e14 / 1146880;
            d7 = 36941521 * e14 / 3440640;

            bf = b0 + math.sin(2 * b0) * (d1 + math.sin(b0) * math.sin(b0) * (d2 + math.sin(b0) * math.sin(b0) * (d3 + math.sin(b0) * math.sin(b0) * (d4 + math.sin(b0) * math.sin(b0) * (d5 + math.sin(b0) * math.sin(b0) * (d6 + d7 * math.sin(b0) * math.sin(b0)))))));
            return bf

        BB = 0.0
        LL = 0.0

        y = y - 500000.0;
        Bf = calculateBf(x);
        Vf = math.sqrt(1 + e2 / (1 - e2) * math.cos(Bf) * math.cos(Bf));
        tf = math.tan(Bf);
        hf2 = e2 / (1 - e2) * math.cos(Bf) * math.cos(Bf);
        Nf = a / math.sqrt(1 - e2 * math.sin(Bf) * math.sin(Bf));
        BB = (Bf - 0.5 * Vf * Vf * tf * ((y / Nf) ** 2) - 1.0 / 12 * (5 + 3 * tf * tf + hf2 - 9 * hf2 * tf * tf) * ((y / Nf) ** 4) + 1.0 / 360 * (61 + 90 * tf * tf + 45 * tf * tf) * ((y / Nf) ** 6)) * 180 / math.pi;

        Bdu = int(math.floor(BB))
        Bfen = int((BB - Bdu) * 60)
        Bmiao = ((BB - Bdu) * 60 - Bfen) * 60;
        BB = Bdu + 0.01 * Bfen + 0.0001 * Bmiao;
        BB = Bdu*10000 + Bfen*100 + Bmiao;
        l = 1.0 / math.cos(Bf) * (y / Nf - 1.0 / 6.0 * (1 + 2 * tf * tf + hf2) * ((y / Nf) ** 3) + 1.0 / 120.0 * (5 + 28 * tf * tf + 24 * (tf ** 4) + 6 * hf2 + 8 * hf2 * tf * tf) * ((y / Nf) ** 5)) * 180.0 / math.pi;

        LL = L0*180/math.pi + l;
        Ldu = int(math.floor(LL))
        Lfen = int((LL - Ldu) * 60)
        Lmiao = ((LL - Ldu) * 60 - Lfen) * 60;
        LL = Ldu + 0.01 * Lfen + 0.0001 * Lmiao;
        LL = Ldu*10000 + Lfen*100 + Lmiao;
        return  StationPoint(LL,BB)

    def gauss_zone(self, x, y, L0, L0new):
        point_Old = gauss_negative(x, y, L0);
        point_New = gauss_positive(point_Old.y, point_Old.x, L0new);
        return point_New

if __name__ == "__main__":
    ll = 117 * math.pi / 180
    delta_x = 513804.041 - 513269.1590
    delta_y = 3788034.879 - 3788170.2160
    ct = CoordinateTransform("54")
    with open('C:/Users/miaomiao/workspace/CoordinateTransformProject/bin/input.txt','r') as f:
        lines = f.readlines()
    for line in lines:
        x,y = line.strip().split()
        sp  = ct.gauss_negative(float(y)+delta_y,float(x)+delta_x,ll)
        xx,yy = sp.to_DFM()
        print xx,yy
