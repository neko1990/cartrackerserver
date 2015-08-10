var cars = {};

function initialize(){
  var center_position=new AMap.LngLat(117.143077,34.2148767);

  // Create Map
  var mapOptions = {
    resizeEnable: true,
    rotateEnable: false,
    dragEnable: true,
    zoomEnable: true,
    zooms: [16,18],
    layers:[
      new AMap.TileLayer(),//加载地图底图
      new AMap.TileLayer.RoadNet()
      // new AMap.TileLayer.Satellite(),
    ],
    view: new AMap.View2D({
      center:center_position,
      zoom:17,
      rotation:0
    }),
    lang:"zh_cn"
  };
  mapObj = new AMap.Map("mapContainer",mapOptions);

  // Create Map Control
  mapObj.plugin(["AMap.MapType"],function(){
    var type= new AMap.MapType({
      defaultType:0 //使用2D地图
    });
    mapObj.addControl(type);
  });

  websocketToServer();
};

function websocketToServer(){
  // var host = "106.185.49.44";
  var host = "180.123.139.174";
  var port = "8886";
  var uri = "/ws"
  ws = new WebSocket("ws://" + host + ":" + port + uri);
  ws.onopen = function(evt) {
    console.log("Connect Successful");
  };

  // Handle incoming websocket message callback
  ws.onmessage = function(evt){
    var data = JSON.parse(evt.data)
    if (data) {updateMarker(data);}
  };

  // Close Websocket callback
  ws.onclose = function(evt) {
    alert("Connection close");
  };
}

function updateMarker(data){
  data.forEach(function (car){
    var pos = new AMap.LngLat(car.pos[0],car.pos[1]);
    if (car.name in cars){
      cars[car.name].setPosition(pos);
    } else {
      cars[car.name] = createMarker(car.name,pos);
    }
  });
}

function createMarker(name,lnglat){
  var marker = new AMap.Marker({ //创建自定义点标注
    map:mapObj,
    draggable:false, // default
    title:name,
    position: lnglat,
    offset: new AMap.Pixel(-24,-24),
    icon: "icon/bus_icon_48.png",
    autoRotation:false
  });
  return marker;
};
