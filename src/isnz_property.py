from project import common as c


class Rijkregisternummer:

    @property
    def first_block(self):
        return
def calc_isnz():
    # FIRST BLOCK
    date_of_birth = input("What's your date of birth? dd/mm/yy")
    formatted_dob = c.formatDateOfBirth(date_of_birth)

    first_block = ".".join(formatted_dob)

    # second block
    gender = input("Are you male or female? Type A if you are a male, B if you are female. ")
    second_block = str(c.calc_second_block(gender))

    # third block
    third_block = c.calc_third_block(formatted_dob, c.extractYear(date_of_birth.split('/')[2]), second_block)

    return str(first_block) + "-" + str(second_block) + "." + str(third_block)
