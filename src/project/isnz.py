
import common as com

def isnz_generate():
    # first block
    date_of_birth = com.get_dob()

    formatted_dob = com.formatDateOfBirth(date_of_birth)
    first_block = ".".join(formatted_dob)

    # second block
    gender = com.get_gender()
    second_block = str(com.calc_second_block(gender))

    # third block
    year = date_of_birth.split('/')[2]
    third_block = com.calc_third_block(formatted_dob, com.extractYear(year), second_block)

    return str(first_block) + "-" + str(second_block) + "." + str(third_block)

