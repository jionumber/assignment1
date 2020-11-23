# question 1
# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
def qns1():
    import datetime
    now = datetime.datetime.now()
    x = input("enter your name dear visitor:")
    y = int(input("enter your age:"))
    z = now.year - y
    a = z + 100
    print(a)
qns1()

# question 2
# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
def qns2():
    x = int(input("enter any number :"))
    if (x == 0):
        print("wrong input")
    elif (x % 2 == 0):
        print("it is an even number.....")
    else:
        print("it is an odd number....")
qns2()

def qns3():
    # question 6
    x = str(input("enter any word :"))
    rvs = x[::-1]
    print(rvs)
    if rvs == x:
        print("it is a palindrome number")
    else:
        print("it is a non palindrome number")
qns3()
# # question 7# question 7
#
# a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# b = [number for number in a if number % 2 == 0]
# print(b)
#
# # question 9
# import random
#
# a = random.randint(1, 9)
# x = int(input("guess some number :"))
# print(a)
# if (x > a):
#     print("your number is too greater")
# elif (a == x):
#     print("you guessed right")
# else:
#     print("your number is too small")
#
# # question 11
# x = int(input("enter any number :"))
# for i in range(2, x):
#     if (x % i == 0):
#         print("it is not a prime number")
#         break
# else:
#     print("it is a prime number")
#
# # question 12
# a = [5, 10, 15, 20, 25]
# print(a[0], a[-1])
#
# '''




