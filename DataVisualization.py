print("abhinav")

# PRINT WITHOUT NEW LINE
print("abhinav", end=" ")
print('srivastava')

a = ['abhi','abhinav','abhinav1']
print(type(a))
for item in a :
    print(item, end=" ")

# we can use \to ignore the (') mark between the sentence
a='abhinav\'s laptop'
print(a)

# tup does not allow changes in the list unlike list
# [] for list
# () for tupels or tup
# {} for sets
# tup and list are similar but tup values cannot be changed
# in set it removes repetitive values and it will not follow the sequence

c=[15,45,46,46,74,46]
c.append(46)
print(c)
print(c.count(46))

# for tracking the address of the values use id(val)
num = 5
print(id(num))
# assigning the same values to the different variable will make both the variables pointing at the same address
a = 5
b = a
print(a)
print(b)
print(id(a))
print(id(b))
# (therefore python is more memory efficient)

# we cannot make constant in python but can only show intention of making constant
PI = 3.14
print(PI)
# we can know the data type of variable by using type() command
print(type(PI))
# numeric data types : int float complex bool(boolean)
a = 4
print(type(a))
b = 3.5
print(type(b))
c = (6 + 5j)
print(type(c))
# we can change the type of data into another type of data
print(int(b))
bool = b > a
print(bool)
bool = 11 > a
print(bool)

z = "abhinav"
print(type(z))
# range
print(range(17))
# listing of range
print(list(range(17)))
# printing the even no. between 2-17 (2,17,2) [2=starting no.],[10=ending no.],[2= difference between no.]
print(list(range(2, 17, 2)))
print(type(range(17)))
# dictionary
d = {'student1': 'python', 'student2': 'c++', 'student3': 'java'}
print(d)
print(d.keys())
print(d.values())
print(d['student1'])
print(d.get('student2'))

# SWAPPING THE VALUES
# 1 USING THIRD VARIABLE
a = 5
b = 6
s = a
a = b
b = s
print(a, b)
# 2 WITHOUT USING THIRD VARIABLE
a = 5
b = 6
a = a + b  # a=5+6=11
b = a - b  # b=11-6=5
a = a - b  # a=11-5=6
print(a, b)
# 3 BY USING XOR GATE LOGIC OPERATION

#IMPORT MODULE
import math

x = math.sqrt(16)  # square root
print(x)
y = math.pow(2, 5)  # power
print(y)
z = math.ceil(4.6)  # round-off of a number
print(z)
u = math.pi  # value of pi
print(u)
v = math.e  # value of exponential
print(v)
# we can also use short form of word math as m
import math as m
b = m.cos(0)
print(b)

# if we want to import only a particular operations
from math import pow
g = pow(2, 5)
print(g)


# INPUT FUNCTION
name = input("Enter your name:")
print("hello ", name)

a = input("enter the first number")
b = input('enter the second number')
c = a+b
print('answer is :', c)
# here we are getting the output for values (a=5 b=4) is 54 instead of 9 because the type of a is STRING not INTEGER

a = (int(input("enter the first number:")))
b = (int(input("enter the second number:")))
c = a+b
print("the answer is :", c)

# we can also enter the equation in output section through evaluate function(eval)
result = eval(input("enter the equation"))
print(result)

# CONDITION
a= int(input('enter the number:'))
if (a>12):
    print("number is good")
elif(a>25):
    print("number is poor")
else:
    print("the number is great")

# python program to illustrate nested If statement
# !/usr/bin/python
i = 10
if i == 10:
    # First if statement
    if i < 15:
        print("i is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")
else:
    print("i is not equal to 10 ")


age=int(input("Enter your age"))
if age>18 and age<=100 :
    print("you are eligible for driving")
elif age==18:
    print("come for physical test")
elif age<18 :
    print("you cannot drive")
else :
    print("invalid age")

# LOOP
i=1
while i<=5 :
    print("abhinav" ,end="  ")
    j=1
    while j<=5:
            print("well done",end=",  ")
            j=j+1
    i=i+1
    print()
