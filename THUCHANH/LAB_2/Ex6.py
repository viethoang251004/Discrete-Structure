import itertools
# Define the boolean expressions
def expr1(p, q, r):
    return (p <= r) and (not p <= q) and (q <= r)

def expr2(p, q, r, s):
    return ((not q and p) or (q or p)) <= q and (p or s) and (r <= q) and not s

def expr3(p, q, r):
    return (p <= q) and ((p or q) <= r) == ((p <= r) and (q <= r))

def expr4(p, q, r, s, t):
    return (p and q) == (not p and not q) and (p or not q <= (not p)) == ((p or not q) <= (not p)) and (p or q) == (not p and not q) and (p or q <= (not r) or t) and (p or t <= q <= r <= t) and (p or q and r) == ((p or q and p or r) and t or not t)

# Generate the truth table
table = list(itertools.product([False, True], repeat=5))
# Check if the arguments are valid
print("Argument 1 is", "VALID" if all(expr1(p, q, r) for p, q, r, _, _ in table) else "INVALID")
print("Argument 2 is", "VALID" if all(expr2(p, q, r, s) for p, q, r, s, _ in table) else "INVALID")
print("Argument 3 is", "VALID" if all(expr3(p, q, r) for p, q, r, _, _ in table) else "INVALID")
print("Argument 4 is", "VALID" if all(expr4(p, q, r, s, t) for p, q, r, s, t in table) else "INVALID")
