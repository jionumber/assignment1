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
    #Ask the user for a string and print out whether this string is a palindrome or not.
    x = str(input("enter any word :"))
    rvs = x[::-1]
    print(rvs)
    if rvs == x:
        print("it is a palindrome number")
    else:
        print("it is a non palindrome number")
qns3()
def qns4():
    # question 7
    #Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
    a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    b = [number for number in a if number % 2 == 0]
    print("even numbers of list a are : ",b)
qns4()
def qns5():
    # question 9
    # Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very
    import random
    a = random.randint(1, 9)
    x = int(input("guess some number between 1 to 9:"))
    print(a)
    if (x > a):
        print("your number is too greater")
    elif (a == x):
        print("you guessed right")
    else:
        print("your number is too small")
qns5()
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




