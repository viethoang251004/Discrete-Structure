# (a)
from sympy import isprime

valid = False
for x in range(101):
    if x**3 < x:
        valid = True
        break

if valid:
    print("The negated statement is correct. There exists an x =", x, "such that x^3 < x.")
else:
    print("The negated statement is incorrect. For all values of x within the given domain, x^3 >= x.")

# (b)
valid = False
for x in range(0, 101, 2):
    if not isprime(x * 3 + 1):
        valid = True
        break

if valid:
    print("The negated statement is correct. There exists an even x =", x, "such that x * 3 + 1 is not a prime number.")
else:
    print("The negated statement is incorrect. For all even values of x within the given domain, x * 3 + 1 is a prime number.")

# (c)
valid = False
for x in range(2, 101, 2):
    if not isprime(x * 5 + 3):
        valid = True
        break

if valid:
    print("The negated statement is correct. There exists an even x =", x, "such that x * 5 + 3 is not a prime number.")
else:
    print("The negated statement is incorrect. For all even values of x within the given domain, x * 5 + 3 is a prime number.")

# (d)
valid = True
for c in range(1, 101):
    if c % 4 == 0:
        valid = False
        for a in range(1, int(c**0.5) + 1):
            b = (c**2 - a**2)**0.5
            if b.is_integer():
                valid = True
                break
        if not valid:
            break

if valid:
    print("The negated statement is correct. For all c belonging to Z, 0 < c <= 100, c % 4 = 0, there does not exist any a, b belonging to Z+ such that c^2 = a^2 + b^2.")
else:
    print("The negated statement is incorrect. There exists a c belonging to Z, 0 < c <= 100, c % 4 = 0, such that there is at least one a, b belonging to Z+ satisfying c^2 = a^2 + b^2.")

# (e)
valid = True
for c in range(1, 101):
    if c % 5 == 0:
        valid = False
        for a in range(1, int(c**0.5) + 1):
            b = (c**2 - a**2)**0.5
            if b.is_integer():
                valid = True
                break
        if not valid:
            break

if valid:
    print("The negated statement is correct. For all c belonging to Z, 0 < c <= 100, c % 5 = 0, there does not exist any a, b belonging to Z+ such that c^2 = a^2 + b^2.")
else:
    print("The negated statement is incorrect. There exists a c belonging to Z, 0 < c <= 100, c % 5 = 0, such that there is at least one a, bbelonging to Z+ satisfying c^2 = a^2 + b^2.")

# (f)
valid = True
for c in range(1, 101):
    if c**2 <= c:
        valid = False
        break

if valid:
    print("The negated statement is correct. For all c belonging to Z, 0 < c <= 100, c^2 > c.")
else:
    print("The negated statement is incorrect. There exists a c belonging to Z, 0 < c <= 100, such that c^2 <= c.")
