function initMap() {
    var pyrmont = new google.maps.LatLng(35.16363182, 136.90907037);

    var map = new google.maps.Map(document.getElementById('map'), {
        center: pyrmont,
        zoom: 15
    });

    var nearbySearchRequest = {
        location: pyrmont,
        radius: '500',
        type: ['レストラン', 'カフェ'],
        rankBy: google.maps.places.RankBy.PROMINENCE
    };

    var service = new google.maps.places.PlacesService(map);

    // Place detail Windowを一つのみにするため、ここで宣言
    const infowindow = new google.maps.InfoWindow();

    service.nearbySearch(nearbySearchRequest, (results, status) => {
        if (status != google.maps.places.PlacesServiceStatus.OK) return;
        for (var i = 0; i < results.length; i++) {
            var getDetailsRequest = {
                placeId: results[i].place_id,
                fields: ["name", "formatted_address", "place_id", "geometry"],
            };
            // Place detail Windowを複数にするため、ここで宣言
            // const infowindow = new google.maps.InfoWindow();

            service.getDetails(getDetailsRequest, (place) => {
                if (
                    place &&
                    place.geometry &&
                    place.geometry.location
                ) {
                    const marker = new google.maps.Marker({
                        map,
                        position: place.geometry.location,
                    });

                    google.maps.event.addListener(marker, "click", () => {
                        const content = document.createElement("div");

                        const nameElement = document.createElement("h2");
                        nameElement.textContent = place.name;
                        content.appendChild(nameElement);

                        const placeIdElement = document.createElement("p");
                        placeIdElement.textContent = place.place_id;
                        content.appendChild(placeIdElement);

                        const placeAddressElement = document.createElement("p");
                        placeAddressElement.textContent = place.formatted_address;
                        content.appendChild(placeAddressElement);

                        infowindow.setContent(content);
                        infowindow.open(map, marker);
                    });
                }
            });
        }
    });
}

window.initMap = initMap;
