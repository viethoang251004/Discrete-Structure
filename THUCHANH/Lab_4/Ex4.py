from sympy import *

# Define the variables
x, y, a, b, c = symbols('x y a b c')

# Define the prime check function
def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Check the negated statements
for x in range(11):
    for y in range(11):
        # (a)
        if sum((x + y)**2 for x in range(11) for y in range(11)) < sum((x**2 + 2*x*y) for x in range(11) for y in range(11)):
            print(f"(a) is true for x = {x}, y = {y}")
        # (b)
        if 20 < sum(factorial(x) for x in range(11)):
            print(f"(b) is true for x = {x}")

# Define the variables
r = symbols('r')

# Check the statements
# (c)
if sum(3*r**2 for r in range(11)) == 10**3:
    print("(c) is true")
else:
    print("(c) is false")

# (d)
if sum((4*r**3 + 6*r**2 + 2*r) for r in range(5, 11)) == factorial(10) + 2 * 10**8:  # The rest of the terms are not clear in the image
    print("(d) is true")
else:
    print("(d) is false")
