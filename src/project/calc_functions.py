import random
import common as com


def calc_isnz():
    # first block
    date_of_birth = com.get_dob()

    formatted_dob = com.formatDateOfBirth(date_of_birth)
    first_block = ".".join(formatted_dob)

    # second block

    gender = com.get_gender()
    second_block = str(com.calc_second_block(gender))

    # third block
    third_block = com.calc_third_block(formatted_dob, com.extractYear(date_of_birth.split('/')[2]), second_block)

    return str(first_block) + "-" + str(second_block) + "." + str(third_block)


def calc_bis():
    # first block
    date_known = input("Is date of birth known? y/n")
    if date_known.lower() == "y":
        date_of_birth = com.get_dob()
    else:
        date_of_birth = com.generate_dob()

    formatted_dob = com.formatDateOfBirth(date_of_birth)

    # second block
    gender_known = input("Is gender known? y/n")
    gender = ""
    if gender_known.lower() == "y":
        # month +40
        formatted_dob[1] = int(formatted_dob[1]) + 40

        gender = com.get_gender()

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
