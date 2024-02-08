from PIL import Image
from io import BytesIO
import requests


def show_map(l='map', **kwargs):
    kwargs.update({'l': l})
    api_url = f"http://geocode-maps.yandex.ru/1.x/"
    response = requests.get(api_url, params=kwargs)
    if not response:
        raise RuntimeError(f"""Error in request:
                                    {response.url}
                                    Http status {response.status_code} ({response.reason})""")
    Image.open(BytesIO(response.content)).show()


if __name__ == '__main__':
    lon = '57.530887'
    lat = '60.703118'
    delta = '0.002'

    params = {
        'll': ",".join([lon, lat]),
        "spn": ",".join([delta, delta]),
        "l": 'map'
    }
    show_map(**params)
