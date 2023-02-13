import random

# 1 date of birth 2 random m/f


temp = ""
current = ""

firstBlock = ""
dateOfBirth = ""
yearOfBirth = ""
secondBlock = ""
thirdBlock = ""

# first block
print("We are calculating BIS")
dateKnown = input("Is date of birth known? y/n")
if dateKnown == "y" or dateKnown == "y".upper():
    dateOfBirth = input("Whats your date of birth? dd/mm/yy")
    temp = dateOfBirth.split('/')
    yearOfBirth = temp[2]

else:
    yearOfBirth = random.randint(10, 99)
    temp = ['00', '00', str(yearOfBirth)]

#
# second block
genderKnown = input("Is gender known? y/n")
if genderKnown == "y" or genderKnown == "y".upper():
    # month +40
    temp[1] = int(temp[1]) + 40
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
    temp = [str(i) for i in temp]
    current = "".join(temp)
    print(current)
    current = current + secondBlock
    print(current)

elif genderKnown == "n" or genderKnown == "n".upper():
    # month + 20
    temp[1] = int(temp[1]) + 20


#
temp.reverse()
temp = [str(i) for i in temp]
firstBlock = ".".join(temp)
# current = "".join(temp)

# third block
temp3 = 0
if (int(yearOfBirth) >= 2000):
    temp3 = int("2" + current)
    thirdBlock = 97 - (temp3 % 97)
else:
    thirdBlock = 97 - (int(current) % 97)

print(temp)
print(current)


print(f"BIS-nummer is: {firstBlock}-{secondBlock}.{thirdBlock}")
