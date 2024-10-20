import requests
from django.conf import settings


# from django.conf import settings

def nearby_search_api(geolocation):
    url = 'https://places.googleapis.com/v1/places:searchNearby'
    headers = {'Content-Type': 'application/json',
               'X-Goog-Api-Key': settings.SERVER_MAPS_API_KEY,
               'X-Goog-FieldMask': 'places.displayName,places.websiteUri,places.googleMapsUri,places.id,places.location,places.photos,places.primaryTypeDisplayName,places.id'
    }
    data = {'includedPrimaryTypes': ['restaurant'],
            'maxResultCount': 3,
            'languageCode': 'ja',
            'regionCode': 'JP',
            'rankPreference': 'POPULARITY',
            'locationRestriction': {
                'circle': {
                    'center': {
                        'latitude': geolocation['lat'],
                        'longitude': geolocation['lng']},
                    'radius': 1000.0
                }
            }
            }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code != 200:
        print(response.status_code)
        print(response.text)
        return

    return response.json()


