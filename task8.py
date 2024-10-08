# Functions in python 
def make_coffee():
    print("Boil water.")
    print("Add coffee grounds.")
    print("Pour hot water into a cup.")
    print()

make_coffee()
make_coffee()
make_coffee()


# class method vs static -method in Python
# class method()
class Car:
    manufacturer = "Tesla"  
    
    def show(self):
        print(f"The model is {self.model} and the manufacturer is {self.manufacturer}")
    
    def changeManufacturer(self, newManufacturer):
        self.manufacturer = newManufacturer  

car1 = Car()
car1.model = "Model X"
car1.show()  

# static method
class Calculator:
    @staticmethod
    def multiply(a, b):
        return a * b

result = Calculator.multiply(3, 4)  # Calling static method
print(result)

# Write an empty function in Python – pass statement
def my_function():
    pass  

mylist = []

print(mylist)

# Yield instead of Return
def oddNumberGenerator():
    yield 1
    yield 3
    yield 5

for num in oddNumberGenerator():
    print(num)

def fibonacciGenerator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for num in fibonacciGenerator():
    if num > 1000:
        break
    print(num)

# Return Multiple Values
def product_and_quotient(x, y):
    product = x * y
    quotient = x / y
    return product, quotient

result_product, result_quotient = product_and_quotient(50, 10)

print("Product:", result_product)
print("Quotient:", result_quotient)


# Partial Functions in Python
from functools import partial
def f(a,b,c,x):
    return 1000*a + 100*b + 10*c + x
g = partial(f,2,4,6)
print(g(8))


# First Class functions in Python
def multiply_by_two(number):
    return number * 2

def subtract_five(number):
    return number - 5

def add_ten(number):
    return number + 10

def divide_by_three(number):
    return number / 3

# Store the functions in a list
func_list = [multiply_by_two, subtract_five, add_ten, divide_by_three]

# Loop through the list and apply each function to the number 15
for func in func_list:
    print(func(15))

# Precision Handling
import math


b = 7.9235
print(math.trunc(b))     # Truncate decimal part
print(math.ceil(b))      # Round up to nearest integer
print(math.floor(b))     # Round down to nearest integer

b = 9.87654321
print('%.2f' % b)         # Format to 2 decimal places
print("{0:.4f}".format(b)) # Format to 4 decimal places

# *args and **kwargs
# *args Example
def multiply(*args):
    result = 1
    for arg in args:
        result *= arg
    return result

print(multiply(2, 3, 4))  # Output: 24


# **kwargs Example
def display_book_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key.capitalize()} : {value}")

display_book_details(title="Python Programming", author="John Doe", year=2021, pages=450)

# Python closures
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure = outer_func(10)
result = closure(4)
print(result)

# Function Decorators
import datetime
def log(func):
    def wrapper(args,*kwargs):
        with open("logs.txt", "a") as f:
            f.write("Called function with" + " ".join([str(arg) for arg in args]) + "at" + str(datetime.datetime.now())+ "\n")
        val = func(args,*kwargs)
        return val    
    return wrapper
@log
def run(a,b,c=9):
    print(a+b+c)
run(1,3,c=9) 

 # decorators in python
def decor(addition):
    def inner():
        result = addition()
        num3 = float(input("Enter third number:"))
        result = result+num3
        return result
    return inner
def addition():
    num1 = float(input("Enter first number:"))
    num2 = float(input("Enter second number:"))
    result = num1+num2 
    return result
addition = decor(addition)
print("addition is:" , addition()) 
# Decorators with parameters in Python
def decorator(*args, **kwargs):
    print("Hello World!")
    def inner(func):
        print("I am Mrs.Destroyer")
        print("I like" ,kwargs['like'])
        func()
    return inner 
@decorator(like='chocolates')
def my_func():
    print("I like chocolates too much") 
# Memoization using decorators in Python
from functools import wraps
from time import perf_counter
import sys
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper
@memoize
def fibonacci(n) -> int:
    if n < 2 :
        return n 
    return fibonacci(n-1)+fibonacci(n-2)
if _name== 'main_':
    sys.setrecursionlimit(10_000)
    start = perf_counter()
    f = fibonacci(1000)
    end = perf_counter()
    print(f)
    print(f'Time:{end - start} seconds')


# Help function in Python
def multiply(x, y):
   print(x * y)

help(multiply)

# Python | range() does not return an iterator
r = range(2, 20, 3)

print(r)  

# Accessing the start, step, and stop attributes
print(r.start) 
print(r.step)  
print(r.stop)   

print(r.index(17)) 


#Python bit functions on int (bit_length, to_bytes and from_bytes)
# int.bit_length
num1 = 10
print(num1.bit_length())  

num2 = -10
print(num2.bit_length())  

# int.to_bytes
print((500).to_bytes(2, byteorder='little'))  

# int.from_bytes
print(int.from_bytes(b'\x03\xe8', byteorder='big')) 
