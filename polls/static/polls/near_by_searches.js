var map;
var service;
var infowindow;

// function initMap() {
//   var sydney = new google.maps.LatLng(-33.867, 151.195);
//
//   infowindow = new google.maps.InfoWindow();
//
//   map = new google.maps.Map(
//       document.getElementById('map'), {center: sydney, zoom: 15});
//
//   var request = {
//     query: 'Museum of Contemporary Art Australia',
//     fields: ['name', 'geometry'],
//   };
//
//   var service = new google.maps.places.PlacesService(map);
//
//   service.findPlaceFromQuery(request, function(results, status) {
//     if (status === google.maps.places.PlacesServiceStatus.OK) {
//       for (var i = 0; i < results.length; i++) {
//         createMarker(results[i]);
//       }
//       map.setCenter(results[0].geometry.location);
//     }
//   });
// }

///////////////////////////////////////////////////////////
function initMap() {
  var pyrmont = new google.maps.LatLng(35.16363182,136.90907037);

  map = new google.maps.Map(document.getElementById('map'), {
      center: pyrmont,
      zoom: 15
    });

  var request = {
    location: pyrmont,
    radius: '500',
    type: ['レストラン','カフェ'],
    rankBy: google.maps.places.RankBy.PROMINENCE
  };

  service = new google.maps.places.PlacesService(map);
  service.nearbySearch(request, callback);
}

function callback(results, status) {
  if (status == google.maps.places.PlacesServiceStatus.OK) {
    for (var i = 0; i < results.length; i++) {
      createMarker(results[i]);
    }
  }
}
///////////////////////////////////////////////////////////
// 下記はplace_searchライブラリで共通なので変えない
///////////////////////////////////////////////////////////
function createMarker(place) {
  if (!place.geometry || !place.geometry.location) return;

  const marker = new google.maps.Marker({
    map,
    position: place.geometry.location,
  });

  google.maps.event.addListener(marker, "click", () => {
    infowindow.setContent(place.name || "");
    infowindow.open(map);
  });
}

window.initMap = initMap;
