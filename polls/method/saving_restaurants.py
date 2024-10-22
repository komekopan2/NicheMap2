import requests
from django.conf import settings


def saving_restaurants(restaurants):
    saved_restaurants = []
    for restaurant in restaurants:
        restaurant_photo_name = restaurant['photos'][0]['name']
        served_photo_name = restaurant_photo_name[8:18] + '.jpg'
        # もし、すでに保存されている場合は、保存しない
        try:
            with open('polls/static/media/' + served_photo_name, 'rb') as f:
                pass
        except FileNotFoundError:
            url = "https://places.googleapis.com/v1/" + restaurant_photo_name + "/media?key=" + settings.SERVER_MAPS_API_KEY + "&maxHeightPx=100&maxWidthPx=100"
            response = requests.get(url)
            if response.status_code != 200:
                print(response.status_code)
                print(response.text)
                return
            # /staticにjpgを保存
            with open('polls/static/media/' + served_photo_name, 'wb') as f:
                f.write(response.content)
        finally:
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
            print(saved_restaurants)
    return saved_restaurants
