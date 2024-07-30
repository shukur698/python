n = 10
for num in range(1,n,1):
    count = 0
    for i in range(1,num+1,1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print(num)
