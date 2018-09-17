import math

# Enter a equation in the format of "x + 4 = 10", solve for x.
"""
eq = input("Enter the function: ")
def solve_eq(equ):
    x, operator, num1, equal, num2 = equ.split()
    num1, num2 = int(num1), int(num2)
    if operator == "+":
        x = num2 - num1
        return x
    elif operator == "-":
        x = num2 + num1
        return x
    elif operator == "*":
        if num1 > 0:
            x = num2 / num1
            return x
    elif operator == "/":
        x = num2 * num1
        return x
print("x = ", solve_eq(eq))
"""

# Passing a receiving multiple arguments to a function.
"""
num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
def multi(x, y):
    return (x * y), (x / y)
if num2 > 0:
    output1, output2 = multi(num1, num2)
print("multiplication: {}, division: {}".format(output1, output2))
"""

# Printing a list of prime numbers.
"""
def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True
def get_primes(max_number):
    list_of_primes = []
    for j in range(2, max_number):
        if is_prime(j):
            list_of_primes.append(j)
    return list_of_primes
maxNum = int(input("Enter the max prime you want: "))
listOfPrimes = get_primes(maxNum)
for k in listOfPrimes:
    print(k)
"""

# For unknown number of arguments being passed to a function
"""
def sum_all(*args):
    sum_of_num = 0
    for i in args:
        sum_of_num += i
    return sum_of_num
print("Sum : ", sum_all(0, 2, 4, 6, 8))
"""

# Find the area of various shapes
"""
def get_rect_area():
    lenght = float(input("Enter length of the rectangle: "))
    breadth = float(input("Enter breadth of the rectangle: "))
    print("Area of rectangle: ", (lenght * breadth))


def get_sq_area():
    lenght = float(input("Enter length of the square: "))
    print("Area of square: ", (lenght * lenght))


def get_circ_area():
    radius = float(input("Enter radius of the circle: "))
    print("Area of circle: ", (3.14 * pow(radius, 2)))


def get_tri_area():
    base = float(input("Enter base of the triangle: "))
    height = float(input("Enter height of the triangle: "))
    print("Area of triangle: ", (0.5 * base * height))


def get_area(shape):
    shape = shape.lower()
    if shape == "rectangle":
        get_rect_area()
    elif shape == "square":
        get_sq_area()
    elif shape == "circle":
        get_circ_area()
    elif shape == "triangle":
        get_tri_area()


def main():
    shape_type = input("What shape area do you want: ")
    get_area(shape_type)


main()
"""
