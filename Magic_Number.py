import random, time

# Produces random number between 1 and 10
Magic_number = random.randint(1, 10)
print(Magic_number)


# IF statements for the magic number game with time and real answer

# if User_number == Magic_number:
#     print('WELL DONE YOU SMASHED IT')
# elif User_number < Magic_number:
#     print('Too low my friend')
#     time.sleep(0.5)
#     print('Real Answer: ', Magic_number)
# elif User_number > Magic_number:
#     print('Too high ol chum')
#     time.sleep(0.5)
#     print('Real Answer: ', Magic_number)

# WHILE loop for magic number game so can keep guessing


def usernum():
    return int(input('Pick a number between 1 and 10: '))

while True:
    usernumber = usernum()
    if usernumber == Magic_number:
        print('WELL DONE YOU SMASHED IT')
        break
    elif usernumber < Magic_number:
        print('Too low my friend')
    elif usernumber > Magic_number:
        print('Too high ol chum')