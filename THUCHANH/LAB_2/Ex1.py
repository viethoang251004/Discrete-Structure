# cau (a)
def lImplies(p, q):
    return not p or q


# cau (b)
def lAnd(p, q):
    return p and q


# cau (c)
def lOr(p, q):
    return p or q

# cau (d)
def lXor(p, q):
    return (p and not q) or (not p and q)

# cau (e)
def lNot(p):
    return not p

# cau (f)
def lEquivalent(p, q):
    return p == q

p = True
q = False

print("Logical Implies:")
print(f"p Implies q: {lImplies(p, q)}")

print("\nLogical AND:")
print(f"p AND q: {lAnd(p, q)}")

print("\nLogical OR:")
print(f"p OR q: {lOr(p, q)}")

print("\nLogical XOR:")
print(f"p XOR q: {lXor(p, q)}")

print("\nLogical NOT:")
print(f"NOT p: {lNot(p)}")

print("\nLogical Equivalent:")
print(f"p Equivalent q: {lEquivalent(p, q)}")