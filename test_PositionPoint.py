from PositionPoint import PositionPoint
lng = 117.14112364303995
lat = 34.210311754345234
x =512470.64572097437
y =  3787203.674106625
pt = PositionPoint().set_lnglat(lng,lat)
pt.lnglat2xy()
print pt.lng,' ',pt.lat
print pt.x,' ',pt.y

pt = PositionPoint().set_xy(x,y)
pt.xy2lnglat()
print pt.lng,' ',pt.lat
print pt.x,' ',pt.y
