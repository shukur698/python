n=int(input("enter the value of n"))
temp=n
sum=0
while n!=0:
    r=n%10
    sum=sum+r*r*r
    n=n//10
if sum==temp:
    print("armstrong number")
else:
    print("not armstrong")


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


n=131
rev=0
originalnum=0
originalnum=n
while n>0:
    t=n%10
    rev=rev*10+t
    n=n//10
if originalnum==rev:
    print("it is a palindrome")
else:
    print("it is not a palindrome")


    a=int(input("enter value:"))
if(a%4==0):
    print("leap year")
else:
    print("not leap year")


    def fact():
    n=int(input("enter the value of n"))
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
fact()
     
