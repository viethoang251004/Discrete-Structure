def lLImplies(P, Q):
    return [not p or q for p, q in zip(P, Q)]


def lLAnd(P, Q):
    return [p and q for p, q in zip(P, Q)]


def lLOr(P, Q):
    return [p or q for p, q in zip(P, Q)]


def lLXor(P, Q):
    return [(p and not q) or (not p and q) for p, q in zip(P, Q)]


def lLNot(P):
    return [not p for p in P]


def lLEquivalent(P, Q):
    return [p == q for p, q in zip(P, Q)]


P = [True, True, False, False]
Q = [True, False, True, False]

R_implies = lLImplies(P, Q)
R_and = lLAnd(P, Q)
R_or = lLOr(P, Q)
R_xor = lLXor(P, Q)
R_not = lLNot(P)
R_equiv = lLEquivalent(P, Q)

print("P   Q   lLImplies   lLAnd   lLOr   lLXor   lLNot   lLEquivalent")
print("-" * 57)
for p, q, implies, _and, _or, xor, _not, equiv in zip(P, Q, R_implies, R_and, R_or, R_xor, R_not, R_equiv):
    print(f"{p}     {q}     {implies}       {_and}      {_or}       {xor}       {_not}      {equiv}")


def lLImplies(P, Q):
    return [not p or q for p, q in zip(P, Q)]

def lLAnd(P, Q):
    return [p and q for p, q in zip(P, Q)]

def lLOr(P, Q):
    return [p or q for p, q in zip(P, Q)]

def lLXor(P, Q):
    return [p != q for p, q in zip(P, Q)]

def lLNot(P):
    return [not p for p in P]

def lLEquivalent(P, Q):
    return [p == q for p, q in zip(P, Q)]

# Example lists
P = [True, True, False, False]
Q = [True, False, True, False]

# Performing the calculations
R_lLImplies = lLImplies(P, Q)
R_lLAnd = lLAnd(P, Q)
R_lLOr = lLOr(P, Q)
R_lLXor = lLXor(P, Q)
R_lLNot = lLNot(P)
R_lLEquivalent = lLEquivalent(P, Q)

# Printing the results in a tabulated form
print("P Q lLImplies lLAnd lLOr lLXor lLNot lLEquivalent")
for i in range(len(P)):
    print(f"{P[i]} {Q[i]} {R_lLImplies[i]} {R_lLAnd[i]} {R_lLOr[i]} {R_lLXor[i]} {R_lLNot[i]} {R_lLEquivalent[i]}")