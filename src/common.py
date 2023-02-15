import random


def formatDateOfBirth(date_of_birth):
    return list(reversed(date_of_birth.split('/')))


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


def calc_third_block(formatted_dob, gender_number):
    string_date = [str(i) for i in formatted_dob]
    number = "".join(string_date) + gender_number
    year = formatted_dob[2]
    if int(year) >= 2000:
        temp = int("2" + number)
        return 97 - (temp % 97)
    else:
        number = int(number)
        print(number)
        return 97 - (int(number) % 97)
