print("My name is - DEVANSH")
print("First three leters of my name in blocks are :")

for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
            print("D",end="")
        else:
            print(end=" ")
    print()

for row in range(7):
    for col in range(5):
        if (col==0) or (row==0) or (row==6) or (row==3 and (col)):
            print("E",end="")
        else:
            print(end=" ")

    print()

for row in range(7):
    for col in range(5):
        if (col==0 and row<5) or (col==4 and row<5) or (row==5 and (col==1 or col ==3)) or (row==6 and (col==2)):
            print("V",end="")
        else:
            print(end=" ")

    print()print("My name is - DEVANSH")
print("First three leters of my name in blocks are :")

for row in range(7):
    for col in range(5):
        if (col==0) or (col==4 and (row!=0 and row!=6)) or ((row==0 or row==6) and (col>0 and col<4)):
            print("D",end="")
        else:
            print(end=" ")
    print()

for row in range(7):
    for col in range(5):
        if (col==0) or (row==0) or (row==6) or (row==3 and (col)):
            print("E",end="")
        else:
            print(end=" ")

    print()

for row in range(7):
    for col in range(5):
        if (col==0 and row<5) or (col==4 and row<5) or (row==5 and (col==1 or col ==3)) or (row==6 and (col==2)):
            print("V",end="")
        else:
            print(end=" ")

    print()

