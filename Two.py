print("LP Programming Challenge If Statement")

# NameOne = str(input("What is your name: "))
#
# print("Welcome Mr.", NameOne)
#
# AgeOne = int(input("What is your Age? "))
# print(NameOne, " your Age is ", AgeOne)
#
# if 18 <= AgeOne < 31:
#     print("Welcome to The holiday")
# else:
#     print("Sorry You cant enter the holiday")

# name = input("Please enter your name: ")
# age = int(input("How old are you: "))
#
# if 18 <= age < 31:
#     print("Welcome to club 18-30 holidays, {0}".format(name))
# else:
#     print("I'm sorry, our holiday are only for cool people: ")

#
# name = input("Please enter your name: ")
# age = int(input("How old are you: "))
#
# if 18 <= age < 31:
#     print("Welcome to club 18-30 holidays, {0}".format(name))
# else:
#     print("I'm sorry, our holiday are only for cool people: ")

name = input("What is your name? ")
age = int(input("What is your age: "))

if 18 <= age < 31:
    print("Welcome to the club 18-30 holidays {0}".format(name))
else:
    print("I'm sorry, our holiday are only for cool people: ")