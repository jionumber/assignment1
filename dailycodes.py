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