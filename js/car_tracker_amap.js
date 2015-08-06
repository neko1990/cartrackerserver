var cars = {};

function initialize(){
  var center_position=new AMap.LngLat(117.143077,34.2148767);

  // Create Map
  mapObj=new AMap.Map("mapContainer",{
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
  });

  // Create Map Control
  mapObj.plugin(["AMap.MapType"],function(){
    var type= new AMap.MapType({
      defaultType:0 //使用2D地图
    });
    mapObj.addControl(type);
  });
};

function displayRoute(){
  var arr = new Array();//经纬度坐标数组
  arr.push(new AMap.LngLat(117.14112364303995,34.210311754345234));
  arr.push(new AMap.LngLat(117.14112364303995,34.210311754345234));
  arr.push(new AMap.LngLat(117.14112364361056,34.21032008767882));
  arr.push(new AMap.LngLat(117.1411219785662,34.21034342109164));
  arr.push(new AMap.LngLat(117.14111365585528,34.21049675482356));
  arr.push(new AMap.LngLat(117.14109719272037,34.213465089036106));
  arr.push(new AMap.LngLat(117.14405731199231,34.21583994918714));
  arr.push(new AMap.LngLat(117.14676830384131,34.218547923965836));
  arr.push(new AMap.LngLat(117.15027451951548,34.21855494666698));
  arr.push(new AMap.LngLat(117.15060066165954,34.21747963992061));
  var polyline = new AMap.Polyline({
    map:mapObj,
    path:arr,
    strokeColor:"red",
    strokeOpacity:0.4,
    strokeWeight:3
  });

  //调整视野到合适的位置及级别
  mapObj.setFitView();
}

function websocketToServer(){
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
