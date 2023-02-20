import random

# 1 date of birth 2 random m/f
result = ""
current = ""

firstBlock = ""
dateOfBirth = ""
yearOfBirth = ""
secondBlock = ""
thirdBlock = ""

# first block
print("We are calculating ISNZ")
dateOfBirth = input("Whats your date of birth? dd/mm/yy")
temp = dateOfBirth.split('/')
yearOfBirth = temp[2]
temp.reverse()
firstBlock = ".".join(temp)
current = "".join(temp)

# second block
gender = input("Are you male or female? Type A if you are a male, B if you are female. ")
randomNumber = ""

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

# third block
temp3 = 0
if (int(yearOfBirth) >= 2000):
    temp3 = int("2" + current)
    thirdBlock = 97 - (temp3 % 97)
else:
    thirdBlock = 97 - (int(current) % 97)

print(f"Rijkerigsternummer is: {firstBlock}-{secondBlock}.{thirdBlock}")
