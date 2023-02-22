import random

def extractYear(year):
    str_array = [*year]
    return "".join(str_array[2:])


def formatDateOfBirth(dob):
    print(dob)
    date = dob.split('/')
    date[2] = extractYear(date[2])
    return list(reversed(date))


def calc_second_block(gender):
    # male - odd
    if gender.lower() == "a":
        num = random.choice(
            [i for i in range(1, 999) if i % 2 != 0]
        )
        return concat_zero_for_three_chars(num)

        # female - even
    elif gender.lower() == "b":
        num = int(random.choice(
            [i for i in range(2, 998) if i % 2 == 0]
        ))
        return concat_zero_for_three_chars(num)
    else:
        return "Error: wrong data"


def concat_zero_for_three_chars(number):
    if number < 10:
        num = "00" + str(number)
        return num
    elif 10 <= number < 100:
        num = "0" + str(number)
        return num
    else:
        return str(number)


def calc_third_block(formatted_dob, year, gender_number):
    string_date = [str(i) for i in formatted_dob]
    concatenation = "".join(string_date) + gender_number

    if int(year) >= 2000:
        return calc_final_number("2" + concatenation)
    else:
        return calc_final_number(concatenation)


def calc_final_number(number):
    return str(97 - (int(number) % 97))


def check_date_input_format(dob):
    if len(dob) == 10 and dob[:2].isnumeric() and dob[3:5].isnumeric() and dob[6:].isnumeric() and \
            dob[2] == "/" and dob[50 == "/"]:
        return True
    else:
        return False