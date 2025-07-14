
#Task1

n=int(input("enter a number : "))

def factorial(n):

    if n<2:

        return 1

    else:

        return n * factorial(n - 1)

result=factorial(n)

print(f"The factorial of {n} is {result}")

#Task2

import math

n=int(input("Enter a number : "))

square_root=math.sqrt(n)

print(f"The square root of the  number {n} is {square_root}")

log1=math.log(n)

print(f"The logarithom of {n} is {log1}")

sine=math.sin(n)

print(f"The Sine of {n} is {sine}")

