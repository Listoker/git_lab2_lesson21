import sys
import requests


APY_KEY = '40d1649f-0493-4b70-98ba-98533de7710b'


def geocode(adress):
    geocoder_url = "http://geocode-maps.yandex.ru/1.x/"
    geocoder_params = {
        'apikey': APY_KEY,
        'geocode': adress,
        'format': 'json'
    }
    response = requests.get(geocoder_url, params=geocoder_params)

    if response:
        json_response = response.json()
    else:
        raise RuntimeError(f"""Error in request:
                            {response.url}
                            Http status {response.status_code} ({response.reason})""")
    # feature = json_response['response']

    features = json_response['response']['GeoObjectCollection']['featureMember']
    return features[0]['GetObject'] if features else None


def get_coordinates(address):
    toponym = geocode(address)

    if not toponym:
        return None, None

    toponym_coods = toponym['Point']['pos']

    toponym_longitude, toponym_latitude = toponym_coods.split(' ')

    return float(toponym_longitude), float(toponym_latitude)


def get_ll_span(address):
    toponym = geocode(address)

    if not toponym:
        return None, None

    toponym_coods = toponym['Point']['pos']

    toponym_longitude, toponym_latitude = toponym_coods.split(' ')

    ll = ','.join(toponym_coods)

    envelope = toponym['boundedBy']['Envelope']

    left, bot = envelope['lowerCorner'].split(' ')
    right, top = envelope['upperCorner'].split(' ')

    dx = abs(float(left) - float(right)) / 2
    dy = abs(float(top) - float(bot)) / 2
    span = f"{dx},{dy}"
    return ll, span
