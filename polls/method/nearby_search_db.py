import requests
from django.conf import settings
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from ..models import PassedRestaurant


def nearby_search_db(geolocation, cuisine):
    """
    DBに保存されているデータを使って近くのレストランを検索する
    :param geolocation: {'lat': float, 'lng': float, 'zoom': float}
    :param cuisine: str
    :return: dict
    """
    # 座標をポイントとして作成
    user_location = Point(geolocation['lng'], geolocation['lat'], srid=4326)

    # PassedRestaurantモデルとCandidateRestaurantモデルを結合
    # その後、cuisineに一致するものを取得し、~m以内のお店を近い順に3軒取得
    if cuisine == 'restaurant':
        restaurants = PassedRestaurant.objects.annotate(
            distance=Distance('candidate_restaurant__location', user_location)
        ).filter(distance__lte=calculate_radius(geolocation['zoom'])).order_by('distance')[:3]
    else:
        restaurants = PassedRestaurant.objects.filter(primary_type_display_name=cuisine).annotate(
            distance=Distance('candidate_restaurant__location', user_location)
        ).filter(distance__lte=calculate_radius(geolocation['zoom'])).order_by('distance')[:3]

    # レスポンス用のデータを作成
    places = []
    for restaurant in restaurants:
        # places.append(text_search_api(restaurant.display_name, restaurant.location.y, restaurant.location.x))
        places.append(text_search_api(restaurant.candidate_restaurant.display_name,
                                       restaurant.candidate_restaurant.location.y,
                                       restaurant.candidate_restaurant.location.x))
    return {'places': places}


def text_search_api(display_name, restaurant_lat, restaurant_lng):
    """
    Google Places APIを使ってテキスト検索する
    :param display_name: str
    :param restaurant_lat: float
    :param restaurant_lng: float
    :return: dict
    """
    url = 'https://places.googleapis.com/v1/places:searchText'
    headers = {'Content-Type': 'application/json',
               'X-Goog-Api-Key': settings.SERVER_MAPS_API_KEY,
               'X-Goog-FieldMask': 'places.displayName,places.googleMapsUri,places.location,places.photos,places.primaryTypeDisplayName,places.rating,places.businessStatus,places.userRatingCount'
               }
    data = {'textQuery': display_name,
            'maxResultCount': 1,
            'languageCode': 'ja',
            'regionCode': 'JP',
            "locationBias": {
                "circle": {
                    "center": {
                        "latitude": restaurant_lat,
                        "longitude": restaurant_lng
                    },
                    "radius": 5000.0
                }
            }
            }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        return

    return response.json()['places'][0]


def calculate_radius(zoom):
    """
    zoomレベルから半径を計算して返す
    :param zoom: float
    :return: float
    """
    earth_circumference_meters = 40075000  # 地球の赤道円周（メートル）
    # zoomの範囲を10～21に制限
    zoom = max(9, min(zoom, 21))
    # 地図の直径を計算
    diameter = earth_circumference_meters / (2 ** zoom)
    # 直径の範囲を100000までに
    diameter = min(diameter, 100000)

    # 半径に変換して返す
    return diameter / 2
