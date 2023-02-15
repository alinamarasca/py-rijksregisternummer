import random


class Number:
    def __init__(self):
        self.temp = ""
        self.result = ""
        self.current = ""
        self.randomNumber = 0

        self.date_of_birth = ""
        self.gender = ""

        self.year_of_birth = self.temp[2]
        self.first_block = ""
        self.secondBlock = ""
        self.thirdBlock = ""

    @classmethod
    def calc_isnz(cls):
        date_of_birth = input("Whats your date of birth? dd/mm/yy")
        # first block
        temp = date_of_birth.split('/')
        year_of_birth = temp[2]
        temp.reverse()
        first_block = ".".join(temp)
        current = "".join(temp)

        # second block
        gender = input("Are you male or female? Type A if you are a male, B if you are female. ")
        # male - odd
        if gender == "A" or gender == "A".lower():
            randomNumber = random.choice(
                [i for i in range(1, 997) if i % 2 != 0]
            )
        # female - even
        elif gender == "B" or gender == "B".lower():
            randomNumber = int(random.choice(
                [i for i in range(2, 998) if i % 2 == 0]
            ))

        secondBlock = str(randomNumber)
        current = current + secondBlock

        # # third block
        temp3 = 0
        if (int(year_of_birth) >= 2000):
            temp3 = int("2" + current)
            third_block = 97 - (temp3 % 97)
        else:
            third_block = 97 - (int(current) % 97)

        print(f"Rijkerigsternummer is: {first_block}-{secondBlock}.{third_block}")

    @classmethod
    def calc_bis(cls):

        # first block
        date_known = input("Is date of birth known? y/n")
        if date_known == "y" or date_known == "y".upper():
            date_of_birth = input("Whats your date of birth? dd/mm/yy")
            temp = date_of_birth.split('/')
            year_of_birth = temp[2]

        else:
            year_of_birth = random.randint(10, 99)
            temp = ['00', '00', str(year_of_birth)]

        #
        # second block
        gender_known = input("Is gender known? y/n")
        if gender_known == "y" or gender_known == "y".upper():
            # month +40
            temp[1] = int(temp[1]) + 40
            gender = input("Are you male or female? Type A if you are a male, B if you are female. ")

            # male - odd
            if gender == "A" or gender == "A".lower():
                random_number = random.choice(
                    [i for i in range(1, 997) if i % 2 != 0]
                )
            # female - even
            elif gender == "B" or gender == "B".lower():
                random_number = int(random.choice(
                    [i for i in range(2, 998) if i % 2 == 0]
                ))
            second_block = str(random_number)
            temp = [str(i) for i in temp]
            current = "".join(temp)
            current = current + second_block

        elif gender_known == "n" or gender_known == "n".upper():
            # month + 20
            temp[1] = int(temp[1]) + 20

        #
        temp.reverse()
        temp = [str(i) for i in temp]
        first_block = ".".join(temp)
        # current = "".join(temp)

        # third block
        temp3 = 0
        if (int(year_of_birth) >= 2000):
            temp3 = int("2" + current)
            third_block = 97 - (temp3 % 97)
        else:
            third_block = 97 - (int(current) % 97)

        print(temp)
        print(current)

        print(f"BIS-nummer is: {first_block}-{second_block}.{third_block}")

