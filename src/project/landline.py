import json
from phonenumbers_db import phones as db
import common as c


def landline_generate():
    selected_country = input('''Which country?''')
    # phone_type = "landline"
    data = json.loads(db)[selected_country]

    international_prefix = "+" + data[0]["prefix"]
    country_area = c.area_code_array(data[1]["landlineAreaCode"])
    landline_number = c.landline_number_gen(data[2]["length"], country_area)
    print(f"{international_prefix} {country_area} {landline_number}")
