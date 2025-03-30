import requests
from flask import Blueprint, render_template, abort
from models import User

views = Blueprint('views', __name__)

YANDEX_MAPS_API_KEY = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
YANDEX_GEOCODER_API_URL = "https://geocode-maps.yandex.ru/1.x/"


import requests

def get_coordinates(city_name):
    params = {
        "geocode": city_name,
        "format": "json",
        "apikey": YANDEX_MAPS_API_KEY
    }
    try:
        response = requests.get(YANDEX_GEOCODER_API_URL, params=params)
        response.raise_for_status()

        data = response.json()
        if "response" in data:
            geo_objects = data["response"]["GeoObjectCollection"]["featureMember"]
            if geo_objects:
                coordinates = geo_objects[0]["GeoObject"]["Point"]["pos"]
                longitude, latitude = map(float, coordinates.split())
                return latitude, longitude

        return None, None

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        if response is not None:
            print(f"Response content: {response.content}")
        return None, None
    except ValueError as e:
        print(f"Error parsing the response: {e}")
        return None, None



@views.route('/users_show/<int:user_id>')
def users_show(user_id):
    user = User.query.get(user_id)

    if user is None:
        abort(404, description="User not found")

    city = user.city_from
    latitude, longitude = get_coordinates(city)

    if latitude is None or longitude is None:
        abort(404, description="City coordinates not found")

    map_url = f"https://static-maps.yandex.ru/1.x/?ll={longitude},{latitude}&spn=0.2,0.2&l=map&pt={longitude},{latitude},pm2rdm"

    return render_template("login.html", user=user, city=city, map_url=map_url)
