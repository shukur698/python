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
