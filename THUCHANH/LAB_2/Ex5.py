import itertools
# Define the boolean expressions
def expr1(p):
    return p == (not (not p))

def expr2(p, q):
    return not ((not q) and p) and (q or p) == q

def expr4(p, q, r):
    return (p or q) <= r == (p <= r) and (q <= r)

def expr3(p, q):
    return not (p or q) == (not p or not q)

def expr5(p, q):
    return not (p and q) == (not p and not q)

def expr6(p, q):
    return (p or not q) <= (not p) == ((p or (not q)) <= (not p))

def expr7(p, q):
    return not (p or q) == (not p and not q)

# Generate the truth table
table = list(itertools.product([False, True], repeat=2))
# Check if the expressions are equivalent
print("Expression 1 is", "equivalent" if all(expr1(p) for p, q in table) else "inequivalent")
print("Expression 2 is", "equivalent" if all(expr2(p, q) for p, q in table) else "inequivalent")
table = list(itertools.product([False, True], repeat=3))
print("Expression 3 is", "equivalent" if all(expr4(p, q, r) for p, q, r in table) else "inequivalent")
table = list(itertools.product([False, True], repeat=2))
print("Expression 4 is", "equivalent" if all(expr3(p, q) for p, q in table) else "inequivalent")
print("Expression 5 is", "equivalent" if all(expr5(p, q) for p, q in table) else "inequivalent")
print("Expression 6 is", "equivalent" if all(expr6(p, q) for p, q in table) else "inequivalent")
print("Expression 7 is", "equivalent" if all(expr7(p, q) for p, q in table) else "inequivalent")

