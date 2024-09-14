import math

# (a) tồn tại ít nhất một x thuộc Z, 0 <= x <= 100, x^2 = 15^2 + 16^2
for x in range(101):
    if x**2 == 15**2 + 16**2:
        print(f"(a) The given statement is correct when x equals to {x}")
        break
else:
    print("(a) The given statement is incorrect for all values x within the given domain.")


# (b) tồn tại ít nhất một x thuộc Z, 0 <= x <= 100, x^2=12^2 + 16^2
for x in range(101):
    if x**2 == 12**2 + 16**2:
        print(f"(b) The given statement is correct when x equals to {x}")
        break
else:
    print("(b) The given statement is incorrect for all values x within the given domain.")


# (c) tồn tại ít nhất một x thuộc Z, -50 <= x <= 50, x^2 >= 99x
for x in range(-50, 51):
    if x**2 >= 99*x:
        print(f"(c) The given statement is correct when x equals to {x}")
        break
else:
    print("(c) The given statement is incorrect for all values x within the given domain.")


# (d) tồn tại ít nhất một x thuộc Z, 50 <= x <= 100, x(x+1)(x+2)%6 khác 0
for x in range(50, 101):
    if x*(x+1)*(x+2) % 6 != 0:
        print(f"(d) The given statement is correct when x equals to {x}")
        break
else:
    print("(d) The given statement is incorrect for all values x within the given domain.")


# (e) tồn tại ít nhất một x, y thuộc Z, 0 <= x <= 100, (x+y)^(1/2) = x^(1/2) + y^(1/2)
for x in range(101):
    for y in range(101):
        if math.isclose(math.sqrt(x + y), math.sqrt(x) + math.sqrt(y)):
            print(f"(e) The given statement is correct when x equals to {x} and y equals to {y}")
            break
    else:
        continue
    break
else:
    print("(e) The given statement is incorrect for all values x and y within the given domain.")
