var cars = {}

function initialize() {
  var centerPoint = new BMap.Point(117.143077,34.2148767);
  map = new BMap.Map('mapContainer')
  map.centerAndZoom(centerPoint, 17);
  map.addControl(new BMap.NavigationControl());
  map.addControl(new BMap.MapTypeControl());
  websocketToServer();
}

function websocketToServer(){
  // var host = "106.185.49.44";
  var host = "180.123.139.174";
  var port = "8886";
  var uri = "/ws?map=google"
  ws = new WebSocket("ws://" + host + ":" + port + uri);
  ws.onopen = function(evt) {
    console.log("Connect Successful");
  };

  // Handle incoming websocket message callback
  ws.onmessage = function(evt){
    var data = JSON.parse(evt.data)
    if (data) {updateMarkerBaidu(data);}
  };

  // Close Websocket callback
  ws.onclose = function(evt) {
    alert("Connection close");
  };
}

function updateMarkerBaidu(data){
  data.forEach(function (car){
    var pos = new BMap.Point(car.pos[0],car.pos[1]);
    if (car.name in cars){
      cars[car.name].setPosition(pos);
    } else {
      cars[car.name] = createMarkerBaidu(car.name,pos);
    }
  });
}

function createMarkerBaidu(name,pos){
  var marker = new BMap.Marker(pos,{
    icon: new BMap.Icon("icon/bus_icon_48.png",new BMap.Size(48,48)),
    title: name
  });
  map.addOverlay(marker);
  return marker;
}
