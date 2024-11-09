import requests
from django.conf import settings


# from django.conf import settings

def nearby_search_api(geolocation):
    url = 'https://places.googleapis.com/v1/places:searchNearby'
    headers = {'Content-Type': 'application/json',
               'X-Goog-Api-Key': settings.SERVER_MAPS_API_KEY,
               'X-Goog-FieldMask': 'places.displayName,places.googleMapsUri,places.location,places.photos,places.primaryTypeDisplayName,places.rating,places.businessStatus,places.userRatingCount'
               }
    data = {'includedPrimaryTypes': ['restaurant'],
            'maxResultCount': 20,
            'languageCode': 'ja',
            'regionCode': 'JP',
            'rankPreference': 'POPULARITY',
            'locationRestriction': {
                'circle': {
                    'center': {
                        'latitude': geolocation['lat'],
                        'longitude': geolocation['lng']},
                    'radius': 500.0
                }
            }
            }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        return

    return response.json()

