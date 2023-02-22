import random
import datetime
import common as com


def calc_isnz():
    # first block
    while True:
        date_of_birth = input("What's your date of birth? dd/mm/yy")
        if com.check_date_input_format(date_of_birth):
            break
        else:
            print("Invalid input, try again.")
            continue

    formatted_dob = com.formatDateOfBirth(date_of_birth)
    first_block = ".".join(formatted_dob)

    # second block
    while True:
        gender = input("Are you male or female? Type A if you are a male, B if you are female. ")
        if gender.lower() == "a" or gender.lower() == "b":
            break
        else:
            print("Invalid input, try again.")
            continue
    second_block = str(com.calc_second_block(gender))

    # third block
    third_block = com.calc_third_block(formatted_dob, com.extractYear(date_of_birth.split('/')[2]), second_block)

    return str(first_block) + "-" + str(second_block) + "." + str(third_block)


def calc_bis():
    # first block
    date_known = input("Is date of birth known? y/n")
    if date_known.lower == "y":
        date_of_birth = input("What's your date of birth? dd/mm/yyyy")
    else:
        random_year = str(random.randint(1900, 2023))
        date_of_birth = '00/00/' + random_year
    formatted_dob = com.formatDateOfBirth(date_of_birth)

    # second block
    gender_known = input("Is gender known? y/n")
    gender = ""
    if gender_known.lower() == "y":
        # month +40
        formatted_dob[1] = int(formatted_dob[1]) + 40

        while True:
            gender = input("Are you male or female? Type A if you are a male, B if you are female. ")
            if gender.lower() == "a" or gender.lower() == "b":
                break
            else:
                print("Invalid input, try again.")
                continue

    elif gender_known.lower() == "n":
        # month + 20
        formatted_dob[1] = int(formatted_dob[1]) + 20
        gender = random.choice(["a", "b"])

    second_block = str(com.calc_second_block(gender))

    # third block
    third_block = com.calc_third_block(formatted_dob, com.extractYear(date_of_birth.split('/')[2]), second_block)

    string_date = [str(i) for i in formatted_dob]
    first_block = ".".join(string_date)

    return str(first_block) + "-" + str(second_block) + "." + str(third_block)
