import random
import string
import common as c
from collections import OrderedDict


# ignore = [17, 18, 66, 72, 73, 74, 75, 76, 77, 78, 79]

def gen_landline():
    country_code = OrderedDict()
    country_code['be'] = '+32'
    country_code['de'] = '+49'

    selected = input('''
    Select country
    1. be
    2. de
    ''')

    index = int(selected) - 1
    country = list(country_code.keys())[index]
    international = country_code[country]
    area = c.select_from_range(country)
    # area = c.format_area_code(str(random_number))

    subscriber = c.gen_subscriber_number(country, area)

    return f"{international} {area} {subscriber}"
