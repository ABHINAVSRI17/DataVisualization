print("abhinav")
# tup does not allow changes in the list unlike list
# [] for list
# () for tupels or tup
# {} for sets
# tup and list are similar but tup values cannot be changed
# in set it removes repetitive values and it will not follow the sequence
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
c = (6+5j)
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
print(list(range(2, 17,2)))
print(type(range(17)))
# dictionary
d = {'student1': 'python', 'student2': 'c++', 'student3': 'java'}
print(d)
print(d.keys())
print(d.values())
print(d['student1'])
print(d.get('student2'))
# swapping the values
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
a = a+b  # a=5+6=11
b = a-b  # b=11-6=5
a = a-b  # a=11-5=6
print(a, b)
# 3 BY USING XOR GATE LOGIC OPERATION









