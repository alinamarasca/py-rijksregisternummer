import random
import string
import common as c
from collections import OrderedDict


# ignore = [17, 18, 66, 72, 73, 74, 75, 76, 77, 78, 79]

def gen_landline():
    country_code = OrderedDict()
    country_code['be'] = '+32'

    selected = input('''
    Select country
    1. be
    
    ''')

    index = int(selected) - 1
    international = list(country_code.values())[index]
    random_number = c.select_from_range()
    area = c.format_area_code(str(random_number))

    subscriber = c.gen_subscriber_number(area)

    return international + area + subscriber
