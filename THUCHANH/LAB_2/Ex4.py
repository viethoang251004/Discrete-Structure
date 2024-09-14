from itertools import product
# Define the boolean expressions
def expr1(p, q, r):
    return (p or q) <= (p and q) <= (not p or not q)


def expr2(p, q, r):
    return not p or (q and r) <= r


def expr3(p, q, r):
    return (p <= q) and (q <= r)


def expr4(p, q, r):
    return (p or (q and r)) == ((p or q) and (p or r))


def expr5(p, q, r, t):
    return (p or q) <= (not r or t)


def expr6(p, q, r, t):
    return (p or t) <= q <= (r == t)


def expr7(p, q, r, t):
    return (p or (q and r)) == (((p or q) and (p or r)) and (t == t))


# Define the variables
variables = ['p', 'q', 'r', 't']
# Generate all combinations of True and False for the variables
combinations = list(product([False, True], repeat=len(variables)))
# Print the header
print('p', 'q', 'r', 't', 'p ∨ q → p ∧ q → ¬p ∨ ¬q', '¬p ∨ (q ∧ r) → r', '(p → q) ∧ (q → r)', '(p ∨ (q ∧ r)) ↔ ((p ∨ q) ∧ (p ∨ r))',
      'p ∨ q → ¬r ∨ t', 'p ∨ t → q → (r ↔ t)', '(p ∨ (q ∧ r)) ↔ (((p ∨ q) ∧ (p ∨ r)) ∧ (t ↔ t))', sep='\t')
# Calculate and print the truth table
for combination in combinations:
    p, q, r, t = combination
    print(p, q, r, t, expr1(p, q, r), expr2(p, q, r), expr3(p, q, r), expr4(
        p, q, r), expr5(p, q, r, t), expr6(p, q, r, t), expr7(p, q, r, t), sep='\t')
