from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from ..models import CandidateRestaurant


def nearby_search_db(geolocation, cuisine):
    """
    DBに保存されているデータを使って近くのレストランを検索する
    :param geolocation: {'lat': float, 'lng': float, 'zoom': float}
    :param cuisine: str
    :return: dict
    """
    # 座標をポイントとして作成
    user_location = Point(geolocation['lng'], geolocation['lat'], srid=4326)

    # ~m以内のお店を
    restaurants = CandidateRestaurant.objects.annotate(
        distance=Distance('location', user_location)
    ).filter(distance__lte=calculate_radius(geolocation['zoom'])).order_by('distance')

    # レスポンス用のデータを作成
    places = []
    for restaurant in restaurants:
        places.append({
            'display_name': restaurant.display_name,
            # TODO: urlうまくいくかわかんない
            'google_maps_uri': "https://www.google.com/maps/search/?api=1&query=" + str(restaurant.location.y) + "," + str(restaurant.location.x),
            'location': {'latitude': restaurant.location.y, 'longitude': restaurant.location.x},
            'photos': restaurant.photos.url[20:] if restaurant.photos else 'no_image_square.jpg',
            'distance': restaurant.distance.m,
            'review': restaurant.review,
            # TODO: saving_restaurantsで保存しているデータと同じ形式にする必要があるかも
        })
    print(places)

    return {'places': places}


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
