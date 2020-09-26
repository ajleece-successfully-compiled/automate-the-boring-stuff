#!/usr/bin/python3.8

print("Welcome to Chapter 1")

#Covered Python Basics. I know most of these but I'm working through the content like this as a refresher

name = input("Gimmie a name: ")

print("Good to meet you " + name)

#convert int length to string and print
print("Your name is " + str(len(name)) + " letters long")


age = input("Can I see some ID? (enter your age): ")
age = int(age) - 1

#A little bit of flattery (very little)
print("You don't look a day over " + str(age) + " and a half")


print("Welcome to Chapter 2")
#Control flow functionality with a twist
print("Here we're going to validate some of your info you provided. ")

answer = input("Would you like to change your name? (Y/N): ")

if answer.lower() == "y":
    name = input("What would you like it to be?: ")
    print("Ok, your new name is " + name)
else:
    print("Ok, your name is still " + name)

checking = input("Did you check under your toilet this morning? (Y/N):")
if (checking.lower() != "y"):
    print("That's a shame")
    count = 5
    while count > 0:
        print(str(count) + "..." )
        count = count -1
        if count == 0:
            print("Boom!!")
else:
    print("Good thing you did!")

