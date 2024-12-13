import requests
from django.conf import settings


# from django.conf import settings

def nearby_search_api(geolocation, cuisine):
    """
    Google Places APIを使って近くのレストランを検索する
    :param geolocation: {'lat': float, 'lng': float, 'zoom': float}
    :param cuisine: str
    :return: dict
    """
    url = 'https://places.googleapis.com/v1/places:searchNearby'
    headers = {'Content-Type': 'application/json',
               'X-Goog-Api-Key': settings.SERVER_MAPS_API_KEY,
               'X-Goog-FieldMask': 'places.displayName,places.googleMapsUri,places.location,places.photos,places.primaryTypeDisplayName,places.rating,places.businessStatus,places.userRatingCount'
               }
    data = {'includedPrimaryTypes': [cuisine],
            'maxResultCount': 20,
            'languageCode': 'ja',
            'regionCode': 'JP',
            'rankPreference': 'POPULARITY',
            'locationRestriction': {
                'circle': {
                    'center': {
                        'latitude': geolocation['lat'],
                        'longitude': geolocation['lng']},
                    'radius': calculate_radius(geolocation['zoom'])
                }
            }
            }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        return

    return response.json()


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
