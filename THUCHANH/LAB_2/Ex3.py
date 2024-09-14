import itertools
# Define the boolean expressions
def expr1(p, q, r):
    return (p and q) <= r

def expr2(p, q, r):
    return r <= (p and q)

# Generate the truth table
table = list(itertools.product([False, True], repeat=3))
# Print the truth table
print("p\tq\tr\tp ∧ q → r\tr → p ∧ q")
for row in table:
    p, q, r = row
    print(f"{p}\t{q}\t{r}\t{expr1(p, q, r)}\t\t{expr2(p, q, r)}")
