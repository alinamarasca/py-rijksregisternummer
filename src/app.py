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
dateOfBirth = input("Whats your date of birth?")
temp = dateOfBirth.split('/')
yearOfBirth = temp[2]
temp.reverse()
firstBlock = ".".join(temp)
current = "".join(temp)

# second block
gender = input("Are you A: male or B: female?")
min = 0
max = 997
randomNumber = ""

# male - odd
if (gender == "A"):
  randomNumber = random.choice(
    [i for i in range(1, 997) if i % 2 !=0]
  )
# female - even
elif (gender == "B"):
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

result = str(firstBlock) + "-" + str(secondBlock) + "." + str(thirdBlock)
print("HERE:", result)
# print(firstBlock, secondBlock, thirdBlock)


