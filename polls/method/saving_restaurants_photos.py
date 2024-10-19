import requests
from django.conf import settings


def saving_restaurants_photos(restaurants):
    saved_restaurants = []
    for restaurant in restaurants:
        restaurant_photo_name = restaurant['photos'][0]['name']
        url = "https://places.googleapis.com/v1/" + restaurant_photo_name + "/media?key=" + settings.SERVER_MAPS_API_KEY + "&maxHeightPx=100&maxWidthPx=100"
        response = requests.get(url)
        if response.status_code != 200:
            print(response.status_code)
            print(response.text)
            return
        # /staticにjpgを保存
        served_photo_name = restaurant_photo_name[8:18] + '.jpg'
        with open('polls/static/media/' + served_photo_name, 'wb') as f:
            f.write(response.content)
        saved_restaurant = {
            'location': restaurant['location'],
            'display_name': restaurant['displayName']['text'],
            'photos': served_photo_name
        }
        saved_restaurants.append(saved_restaurant)
    return saved_restaurants
