from __future__ import division
import math
from CoordinateTransform import CoordinateTransform

def du2miao(x,y):
    if not (isinstance(x,float) and isinstance(y,float)) :
        raise Exception("du2miao not float argument")
    xdd = math.floor(x)
    x = (x-xdd)*60
    xmm = math.floor(x)
    xss = (x-xmm)*60
    xx = xdd * 10000 + xmm * 100 + xss
    # same for y
    ydd = math.floor(y)
    y = (y-ydd)*60
    ymm = math.floor(y)
    yss = (y-ymm)*60
    yy = ydd * 10000 + ydd * 100 + yss
    return [xx,yy]


def miao2du(x,y):
    x = str(x)
    xdd = int(x[0:3])
    xmm = int(x[3:5])
    xss = float(x[5:])
    xx = xdd+xmm/60.0+xss/3600.0;
    y = str(y)
    ydd = int(y[0:2])
    ymm = int(y[2:4])
    yss = float(y[4:])
    yy = ydd+ymm/60.0+yss/3600.0;
    return [xx,yy]


ll = 117 * math.pi / 180
x=   512470.64572097437
y=   3787203.674106625
lng =117.14112364303995
lat =34.210311754345234
ct54 = CoordinateTransform("54")


print ct54.gauss_negative(y,x,ll)
print ct54.gauss_positive(lat * math.pi / 180, lng * math.pi / 180,ll)
