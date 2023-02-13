import random

# 1 date of birth 2 random m/f
result = ""
current = ""

firstBlock = ""

dayOfBirth = ""
monthOfBirth = ""
yearOfBirth = ""

secondBlock = ""
thirdBlock = ""



# date of birth
knownDateOfBirth = input("Is date of birth known? y/n")
if (knownDateOfBirth == "y"):
    dateOfBirth = input("Whats your date of birth? dd/mm/yy")
    temp = dateOfBirth.split('/')
    num = random.choice([20, 40])
    monthOfBirth = int(temp[1]) + num
    temp[1] = str(monthOfBirth)
    yearOfBirth = temp[2]
    temp.reverse()
    firstBlock = ".".join(temp)
    current = "".join(temp)
    print(current)
else:
    yearOfBirth = random.randint(10, 99)
    monthOfBirth = "00",
    dateOfBirth = "00"
    temp = [str(yearOfBirth), str(monthOfBirth), str(dateOfBirth)]
    firstBlock = ".".join(temp) 
    current = "".join(temp)
    print(current)




#is gender known
knownGender = input("Is gender known? y/n")
if(knownGender == "y"):
    temp[1] = int(monthOfBirth) + 40
    print(monthOfBirth)
    firstBlock = ".".join(temp) 
    current = "".join(temp)
else:
    temp[1] = int(monthOfBirth) + 20
    print(monthOfBirth)
    firstBlock = ".".join(temp) 
    current = "".join(temp)

# second block
gender = input("Are you male or female? Type A if you are a male, B if you are female. ")
randomNumber = ""

# male - odd
if gender == "A" or gender == "A".lower():
  randomNumber = random.choice(
    [i for i in range(1, 997) if i % 2 !=0]
  )
# female - even
elif gender == "B" or gender == "B".lower():
  randomNumber = int(random.choice(
    [i for i in range(2, 998) if i % 2 ==0]
  ))

secondBlock = str(randomNumber)
current =  current + secondBlock

# third block
temp3 = 0
if(int(yearOfBirth) >= 2000):
  temp3 = int("2" + current)
  thirdBlock = 97 - (temp3 % 97)
else:
  thirdBlock = 97 - (int(current) % 97)

print(f"Rijkerigsternummer is: {firstBlock}-{secondBlock}.{thirdBlock}")


