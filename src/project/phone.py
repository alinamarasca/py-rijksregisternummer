import random
import string
from collections import OrderedDict


operators = {
    "proximus": [460, 471, 472, 473, 474, 476, 476, 477, 478, 479],
    "telenet": [465, 467],
    "orange": [490, 491, 492, 493, 494, 495, 496, 467, 498, 466]
}
country_code = OrderedDict()
country_code = {
    "be": "+32"
}


# def calc_phone():
def random_in_dictionary(dic):
    maximum = len(dic) - 1
    return random.randint(0, maximum)

print(random_in_dictionary(country_code))
# print(c_index)
country_code = country_code[random_in_dictionary(country_code)]
print(country_code)
# operators = operators[random_in_dictionary(operators)]
# abo_number = "".join(random.choices(string.digits, 6))

# print("HERE", country_code, operators, abo_number)
