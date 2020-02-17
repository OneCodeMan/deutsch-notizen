'''
Deutsch Practice
'''

# this is an import statement. it imports a library
import math

# this is a variable. variables are assigned to values.
# the variable x has the value of an integer 5
x = 5
y = 10
print(x + y) # this statement prints x + y
print(x - y) # this statement prints x - y
print(x * y) # this statement prints x * y
print(x / y) # this statement prints x / y

a = "hallo" # this variable a has value 'hallo'
animals = ['Hund', 'Katze'] # this variable is a list of animals, each element is a string
zahlen = [2, 4, 6, 8, 10, 12] # this is a list of numbers, goes up by 2

# this is a for loop
# calculates the sum of all numbers in the list zahlen
total = 0
for zahl in zahlen:
    total = total + zahl

# This is a function, parameters
# Makes a negative
def make_negative(zahlen):
    lst = []
    for z in zahlen:
        lst.append(-1 * z)
    return lst

print(make_negative([5,2,12,2,92]))

def cube(x):
    return x * x * x

# if statement
max_zahl = 29
if (cube(5) > max_zahl):
    print("lower")
elif (cube(5) == max_zahl):
    print("equal")
else:
    print("higher")
