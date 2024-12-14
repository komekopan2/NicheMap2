import requests
import os
from django.conf import settings


def saving_restaurants(restaurants):
    saved_restaurants = []
    for restaurant in restaurants:
        try:
            restaurant_photo_name = restaurant['photos'][0]['name']
            served_photo_name = restaurant_photo_name[8:18] + '.jpg'
            # もし、すでに保存されている場合は、保存しない
            if os.path.exists('polls/static/media/' + served_photo_name):
                pass
            else:
                url = "https://places.googleapis.com/v1/" + restaurant_photo_name + "/media?key=" + settings.SERVER_MAPS_API_KEY + "&maxHeightPx=400&maxWidthPx=400"
                response = requests.get(url)
                if response.status_code != 200:
                    print(response.status_code)
                    print(response.text)
                    return
                # /staticにjpgを保存
                with open('polls/static/media/' + served_photo_name, 'wb') as f:
                    f.write(response.content)

            saved_restaurant = {
                'display_name': restaurant['displayName']['text'],
                'google_maps_uri': restaurant['googleMapsUri'],
                'location': restaurant['location'],
                'photos': served_photo_name,
                'primary_type_display_name': restaurant['primaryTypeDisplayName']['text'],
                'rating': restaurant['rating'],
                'business_status': restaurant['businessStatus'],
                'user_rating_count': restaurant['userRatingCount'],
            }
            saved_restaurants.append(saved_restaurant)
        except KeyError:
            pass
    return saved_restaurants
