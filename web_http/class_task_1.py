import sys
from mapapi_PIL import *
from geocoder import *


def main():
    toponym_to_find = ' '.join(sys.argv)

    if toponym_to_find:
        lat, lon = get_coordinates(toponym_to_find)
        # fixed spn
        spn = '0.005,0.005'
        show_map(**{'ll': "{lat},{lon}", 'spn': spn})

        # object spn without point

        ll, spn = get_ll_span(toponym_to_find)
        show_map(**{'ll': "{lat},{lon}", 'spn': spn})

        # object spn wist point
        ll, spn = get_ll_span(toponym_to_find)
        show_map(**{'ll': "{lat},{lon}", 'spn': spn, 'pt': f'{ll}'})
    else:
        print('No data')


if __name__ == '__main__':
    main()


