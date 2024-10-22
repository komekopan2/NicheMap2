let map, infoWindow;

async function initMap() {
    if (navigator.geolocation) {
        const { InfoWindow, Map } = await google.maps.importLibrary("maps");
        infoWindow = new InfoWindow();  // InfoWindowを初期化
        navigator.geolocation.getCurrentPosition(
            async (position) => {
                const pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                map = new Map(document.getElementById("map"), {
                    center: pos,
                    zoom: 4,
                    mapId: "4d7250671e5b361d",
                });

                setTimeout(() => {
                    // 中心座標の取得
                    const center = map.getCenter();
                    let geolocation = center.lat() + "," + center.lng();
                    window.location.href = "/polls/searches/" + geolocation + "/";
                }, 1000); // 1秒後にリダイレクト
            },
            () => {
                handleLocationError(true, infoWindow, {lat: 0, lng: 0}); // mapが存在しない場合のデフォルト位置
            }
        );
    } else {
        // Browser doesn't support Geolocation
        handleLocationError(false, infoWindow, {lat: 0, lng: 0}); // デフォルト位置
    }
}

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
    infoWindow.setPosition(pos);
    infoWindow.setContent(
        browserHasGeolocation
            ? "Error: The Geolocation service failed."
            : "Error: Your browser doesn't support geolocation."
    );
    infoWindow.open(map);
}

initMap();