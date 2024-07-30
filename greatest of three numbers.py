def grate():
    n1=int(input("enter the 1st number"))
    n2=int(input("enter the 2nd number"))
    n3=int(input("enter the 3rd number"))
    if n1>n2 and n1>n3:
        print("n1 is gratest")
    elif n2>n1 and n2>n3:
        print("n2 is gratest")
    else:
        print("n3 is gratest")
grate()
