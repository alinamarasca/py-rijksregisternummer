import random
import common as c


# def Number():
#     def __init__(self):
#         self.temp = ""
#         self.result = ""
#         self.current = ""
#         self.randomNumber = 0
#
#         self.date_of_birth = ""
#         self.gender = ""
#
#         self.year_of_birth = self.temp[2]
#         self.first_block = ""
#         self.secondBlock = ""
#         self.thirdBlock = ""

def calc_isnz():
    # FIRST BLOCK
    date_of_birth = input("What's your date of birth? dd/mm/yy")
    formatted_dob = c.formatDateOfBirth(date_of_birth)

    current = "".join(formatted_dob)
    first_block = ".".join(formatted_dob)

    # second block
    gender = input("Are you male or female? Type A if you are a male, B if you are female. ")
    second_block = str(c.calc_second_block(gender))

    current = current + second_block

    # third block
    third_block = c.calc_third_block(current, formatted_dob[0])

    print(f"Rijkerigsternummer is: {first_block}-{second_block}.{third_block}")


def calc_bis():
    # first block
    date_known = input("Is date of birth known? y/n")
    formatted_dob = []
    if date_known == "y" or date_known == "y".upper():
        date_of_birth = input("What's your date of birth? dd/mm/yy")
        formatted_dob = c.formatDateOfBirth(date_of_birth)
        year_of_birth = formatted_dob[2]
    else:
        year_of_birth = random.randint(10, 99)
        formatted_dob = ['00', '00', str(year_of_birth)]

    first_block = ".".join(formatted_dob)
    # second block
    # gender_known = input("Is gender known? y/n")
    gender_known = "y"
    # formatted_dob = formatted_dob

    if gender_known == "y" or gender_known == "y".upper():
        # month +40
        formatted_dob[1] = int(formatted_dob[1]) + 40
        gender = input("Are you male or female? Type A if you are a male, B if you are female. ")

    elif gender_known == "n" or gender_known == "n".upper():
        # month + 20
        formatted_dob[1] = int(formatted_dob[1]) + 20
        gender = random.choice(["a", "b"])

    second_block = str(c.calc_second_block(gender))

       # third block
    second_block=second_block
    third_block = c.calc_third_block(formatted_dob, second_block)

    print(f"BIS-nummer is: {first_block}-{second_block}.{third_block}")