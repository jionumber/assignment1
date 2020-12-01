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