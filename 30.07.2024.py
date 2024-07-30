my_list = [1,2,3,4,5]
my_tuple = tuple(my_list)
print("list:",my_list)
print("tuple:",my_tuple)

my_tuple = (5,6,3,8,9)
my_list = list[my_tuple]
print("list:",my_list)
print("tuple(n):",my_tuple)

def table(n):
  print("multiplacation table of {n}:")
  for i in range(1,11):
        print(f"{n} x {i} = {n * i}")
n=int(input("enter a number"))
table(n)

my_string ="234.9"
my_float =float(my_string)
print("float:",my_float)

my_string ="53"
my_int = int(my_string)
print("int:",my_int)

import math
def lcm(a ,b):
    return abs(a * b)
num1=int(input("enter a number"))
num2=int(input("enter a number"))
print(f"the lcm of {num1} and {num2} is {lcm(num1,num2)}")

def natural(n):
    total_sum = 0
    for i in range(1, n+1):
        total_sum += i
    print("Sum of the first", n, "natural numbers is:", total_sum)

n = 10
natural(n)

def remove_duplicates_with_set (my_list):
   return list(set(my_list))
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = removeduplicates_with_set(my_list)
print(unique_list)

