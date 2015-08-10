var cars = {}

function initialize() {
  var myLatlng = new google.maps.LatLng(34.2148767,117.143077);
  var mapOptions = {
    zoom: 17,
    center: myLatlng
  }
  map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

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
    if (data) {updateMarkerGoogle(data);}
  };

  // Close Websocket callback
  ws.onclose = function(evt) {
    alert("Connection close");
  };
}

function updateMarkerGoogle(data){
  data.forEach(function (car){
    var pos = new google.maps.LatLng(car.pos[1],car.pos[0]);
    if (car.name in cars){
      cars[car.name].setPosition(pos);
    } else {
      cars[car.name] = createMarkerGoogle(car.name,pos);
    }
  });
}

function createMarkerGoogle(name,lnglat){
  var marker = new google.maps.Marker({
    position: lnglat,
    icon: "icon/bus_icon_48.png",
    map: map,
    title: name
  });
  return marker;
}

google.maps.event.addDomListener(window, 'load', initialize);
