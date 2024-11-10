let map, infoWindow, pos;

async function initMap() {
    const { InfoWindow, Map } = await google.maps.importLibrary("maps");
    infoWindow = new InfoWindow();

    // 現在地の取得
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            async (position) => {
                pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                initializeMap();  // 現在地が取得できたらマップを初期化
            },
            () => {
                console.error("現在地が取得できませんでした。");
                pos = { lat: 35.16647380016069, lng: 136.90548000133316 };
                initializeMap();  // デフォルト位置でマップを初期化
            }
        );
    } else {
        console.error("このブラウザではGeolocation APIがサポートされていません。");
        pos = { lat: 35.16647380016069, lng: 136.90548000133316 };
        initializeMap();  // デフォルト位置でマップを初期化
    }
}

// 地図を初期化する関数
function initializeMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: pos,
        zoom: 3,
        mapId: "4d7250671e5b361d",
    });

    // 1秒後にリダイレクト
    setTimeout(() => {
        const center = map.getCenter();
        let geolocation = center.lat() + "," + center.lng();
        window.location.href = "/polls/searches/" + geolocation + "/";
    }, 1000);
}

initMap();