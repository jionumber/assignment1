def my_func1():
#ques1 WAP to enter few numbers then count the all even numbers entered.
    a = int(input("enter the 1st number :"))
    b = int(input("enter the 2st number :"))
    c = int(input("enter the 3rd number :"))
    list = [a,b,c]
    for x in list:
        if (x%2==0):
            print(x)
my_func1()

def my_func2():
#WAP to find sum of digits of an entered number.
    def getSum(n):
        sum = 0
        for digit in str(n):
            sum += int(digit)
        return sum
    n = int(input("enter any number :"))
    print(getSum(n))
my_func2()
def my_func3():
    # ques print febbiconi series
    nterms = int(input("How many terms? "))
    n1, n2 = 0, 1
    count = 0
    if nterms <= 0:
       print("Please enter a positive integer")
    elif nterms == 1:
       print("Fibonacci sequence upto",nterms,":")
       print(n1)
    else:
       print("Fibonacci sequence:")
       while count < nterms:
           print(n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
my_func3()
def my_func4():
    #ques   print 12345 as a triangle shape.
    for row in range(5):
       for col in range(row+1):
           if(row==0):
               print(1,end="")
           elif(row==1):
               print(2,end="")
           elif(row==2):
               print(3,end="")
           elif(row==3):
               print(4,end="")
           elif (row == 4):
               print(5, end="")
    print()
my_func4()
def my_func5():
# question print the following shape.
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
    for row in range(9):
        for col in range(5):
            if (col == 0 or (col == 1 and row != 0 and row != 8) or (col == 2 and row > 1 and row < 7) or (
                    col == 3 and row > 2 and row < 6) or (col == 4 and row > 3 and row < 5)):
                print("*", end="")
        print()
    my_func5()
def my_func6():
# question print the following shape.
# answer :
    for col in range(5):
        for row in range(10):
            if (row == 0) or (row == 1 and col != 0) or (row == 2 and col > 1) or (row == 3 and col > 2) or (
                    row == 4 and col > 3) or (col == 4) or (col == 3 and row != 4 and row != 5) or (
                    col == 2 and row != 3 and row != 4 and row != 5 and row != 6) or (col == 1 and row > 7) or (
                    col == 0 and row == 9):
                print("* ", end="")
            else:
                print(" ", end=" ")
        print()
my_func6()
def my_func7():
#ques shape ques no. 3
    for col in range(5):
        for row in range(10):
            if (col == 0) or (col == 1 and row != 4 and row != 5) or (
                    col == 2 and row != 4 and row != 5 and row != 3 and row != 6) or (
                    col == 3 and row != 4 and row != 5 and row != 3 and row != 6 and row != 2 and row != 7) or (
                    col == 4 and row == 0) or (col == 4 and row == 9):
                print("* ", end="")
            else:
                print(" ", end=" ")
        print()
my_func7()
# palindrome question.
def my_func8():
    a = input("enter any number :")
    if a == str(a)[::-1]:
        print("number is palindrome..")
    else:
        print("number is not palindrome..")
my_func8()
def my_func9():
    #removing vowels ques.
    string = input("Enter any string: ")
    if string == 'x':
        exit();
    else:
        newstr = string;
        print("\nRemoving vowels from the given string");
        vowels = ('a', 'e', 'i', 'o', 'u');
        for x in string.lower():
            if x in vowels:
                newstr = newstr.replace(x, "");
        print("New string after successfully removed all the vowels:");
        print(newstr);
my_func9()
def my_func10():
# wap to count words in a string.
    x = str(input("enter any sentence :"))
    y = len(x)
    print(y)
my_func10()
def my_func11():
#wap to reverse a word entered by the user.
    x = input("enter any word :")
    y = str(x)[::-1]
    print(y)
my_func11()
def my_func11():
#to find ascii value of a given character.
    x = input("enter any character :")
    for y in x:
        print("ascii value of the character is", ord(y))
my_func11()
def my_func12():
    # WAP to display unique and duplicate value of a given list.
    list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 5, 7, 3]
    unique_list = []
    for x in list1:
        if x not in unique_list:
            unique_list.append(x)
    print("unique values are :", unique_list)
my_func12()
def my_func13():
    # question - WAP a string and count the number of words in the string (not aplhabets.)
    x = str(input("enter any string (NOTE - please dont enter any extra space in between the string):"))
    y = x.count(" ")
    z = y + 1
    print("words in your string = ", z)
my_func13()
def my_func14():
    # QUES - WAP to shift a value forward to each value in a list.
    x = [10, 20, 30, 40]
    x.remove(40)
    x.insert(0, 40)
    print(x)
my_func14()
def my_func15():
    #WAP to print 3rd largest and smallest number.
    my_list = [10, 18, 9, 7, 82, 80]
    my_list.sort()
    print(my_list)
    print("third largest number :", my_list[2])
    print("third smallest largest :", my_list[-3])
my_func15()