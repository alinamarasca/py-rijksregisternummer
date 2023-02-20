import random


def extractYear(year):
    str_array = [*year]
    return "".join(str_array[2:])


def formatDateOfBirth(dob):
    date = dob.split('/')
    yy = extractYear(date[2])
    date[2] = yy
    return list(reversed(date))


def calc_second_block(gender):
    # male - odd
    if gender == "A" or gender == "A".lower():
        return random.choice(
            [i for i in range(1, 997) if i % 2 != 0]
        )
    # female - even
    elif gender == "B" or gender == "B".lower():
        return int(random.choice(
            [i for i in range(2, 998) if i % 2 == 0]
        ))
    else:
        return "Error: wrong data"


def calc_third_block(formatted_dob, year, gender_number):
    string_date = [str(i) for i in formatted_dob]
    concatenation = "".join(string_date) + gender_number
    return concat_2_if_more_than_2000(concatenation, year)

def concat_2_if_more_than_2000(number, year):
    if int(year) >= 2000:
        temp = int("2" + number)
        return str(97 - (temp % 97))
    else:
        number = int(number)
        return str(97 - (int(number) % 97))


def check_date_input_format(dob):
    if len(dob) == 10 and dob[:2].isnumeric() and dob[3:5].isnumeric() and dob[6:].isnumeric() and \
            dob[2] == "/" and dob[50 == "/"]:
        return True
    else:
        return False
