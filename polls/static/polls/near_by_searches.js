function initMap() {
    var pyrmont = new google.maps.LatLng(35.16363182, 136.90907037);

    var map = new google.maps.Map(document.getElementById('map'), {
        center: pyrmont,
        zoom: 15
    });

    var nearbySearchRequest = {
        location: pyrmont,
        radius: '500',
        type: ['restaurant','cafe'],
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
                fields: ["name", "photo","business_status","formatted_address", "geometry", "rating", "user_ratings_total", "url"],
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
                        icon: place.photos[0].getUrl({maxWidth: 35, maxHeight: 35}),
                        position: place.geometry.location,
                    });

                    google.maps.event.addListener(marker, "click", () => {
                        showPlaceDetails(place, infowindow, map, marker);
                    });
                }
            });
        }
    });
}

function showPlaceDetails(place, infowindow, map, marker) {
    const content = document.createElement("div");

    const imageElement = document.createElement("img");
    imageElement.src = place.photos[0].getUrl({maxWidth: 200, maxHeight: 200});
    content.appendChild(imageElement);

    const nameElement = document.createElement("h2");
    nameElement.textContent = place.name;
    content.appendChild(nameElement);

    // business_statusがOPERATIONALの場合は「営業中」、CLOSED_TEMPORARILYの場合は「一時休業中」、CLOSED_PERMANENTLYの場合は「閉店済み」と表示
    const placeBusinessStatusElement = document.createElement("p");
    if (place.business_status === "OPERATIONAL") {
        placeBusinessStatusElement.textContent = "営業中";
    } else if (place.business_status === "CLOSED_TEMPORARILY") {
        placeBusinessStatusElement.textContent = "一時休業中";
    } else if (place.business_status === "CLOSED_PERMANENTLY") {
        placeBusinessStatusElement.textContent = "閉店済み";
    }
    content.appendChild(placeBusinessStatusElement);

    // 住所を表示
    const placeAddressElement = document.createElement("p");
    placeAddressElement.textContent = place.formatted_address;
    content.appendChild(placeAddressElement);

    // 評価を表示
    const placeRatingElement = document.createElement("p");
    placeRatingElement.textContent = `評価: ${place.rating}`;
    content.appendChild(placeRatingElement);

    // レビュー数を表示
    const placeRatingsTotalElement = document.createElement("p");
    placeRatingsTotalElement.textContent = `レビュー数: ${place.user_ratings_total}`;
    content.appendChild(placeRatingsTotalElement);

    // 「Google Mapsで見る」リンクを挿入し、新しいタブで開くようにする
    const placeUrlElement = document.createElement("a");
    placeUrlElement.href = place.url;
    placeUrlElement.target = "_blank";
    placeUrlElement.textContent = "Google Mapsで見る";
    content.appendChild(placeUrlElement);

    infowindow.setContent(content);
    infowindow.open(map, marker);
}

window.initMap = initMap;
