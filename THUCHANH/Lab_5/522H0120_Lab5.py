import math
# Exercise 1
P = "You get good grade in the midterm exam"
Q = "You understand how to solve all the exercises in the book"
# Propositional form of the statements
a = f"{Q} -> {P} and {P} -> {Q}"
b = f"{Q} and not {P}"
c = f"{Q} -> {P}"
print(f"(a) {a}")
print(f"(b) {b}")
print(f"(c) {c}")

# Exercise 2
# Natural language form of the statements
a_natural = f"If {Q}, then {P}, and if {P}, then {Q}."
b_natural = f"{Q}, but not {P}."
c_natural = f"If {Q}, then {P}."
print(f"(a) {a_natural}")
print(f"(b) {b_natural}")
print(f"(c) {c_natural}")

# Exercise 3
# Negation, converse and contrapositive of the "if ... then ..." statements
a_negation = f"not ({Q} -> {P}) or not ({P} -> {Q})"
b_negation = f"not ({Q} and not {P})"
c_negation = f"not ({Q} -> {P})"
a_converse = f"{P} -> {Q} and {Q} -> {P}"
b_converse = f"not {P} and {Q}"
c_converse = f"{P} -> {Q}"
a_contrapositive = f"not {P} -> not {Q} and not {Q} -> not {P}"
b_contrapositive = f"{P} or not {Q}"
c_contrapositive = f"not {P} -> not {Q}"
print(f"(a) Negation: {a_negation}, Converse: {a_converse}, Contrapositive: {a_contrapositive}")
print(f"(b) Negation: {b_negation}, Converse: {b_converse}, Contrapositive: {b_contrapositive}")
print(f"(c) Negation: {c_negation}, Converse: {c_converse}, Contrapositive: {c_contrapositive}")

# Exercise 4
# (a) Argument: Phong goes to America
p = "Phong has Visa"
q = "Phong can fly"
r = "Phong can speak English"
t = "Phong goes to America"
given = [
    f"P = {p}",
    f"S1: If {q}, then {t}",
    f"S2: If {p}, then {t}",
    f"S3: If {r}, then {t}",
    f"Conclusion: C = {t}"
]
print("Argument (a): Phong goes to America")
for statement in given:
    print(statement)
# (b) Argument: An is late for school
p = "An wakes up late"
q = "The traffic is flowing smooth"
q_ = "The traffic is heavy"
r = "school day"
s = "An has to go to school"
v = "An is late for school"
given = [
    f"P = {p}",
    f"Q = {q}",
    f"Q' = {q_}",
    f"R = {r}",
    f"S = {s}",
    f"S1: The traffic is always heavy on {r}",
    f"S2: If {p}, he will be {v} on {r}",
    f"S3: {s} only on {r}",
    f"S4: If {s} doesn't happen, {v} can't happen",
    f"Conclusion: C = {v}"
]

print("\nArgument (b): An is late for school")
for statement in given:
    print(statement)

# Exercise 5
# Truth Table
import itertools
truth_values = [True, False]
# Generate all possible combinations of truth values for p, q, and r
combinations = list(itertools.product(truth_values, repeat=3))
# Evaluate the expressions for each combination and print the truth table header
print("\nTruth Table:")
print(" p | q | r | q -> r | p -> q | p -> r ")
print("------------------------------------")
# Evaluate the expressions for each combination and print the truth table rows
for combination in combinations:
    p, q, r = combination

    q_implies_r = q and (not q or r)
    p_implies_q = p and (not p or q)
    p_implies_r = p and (not p or r)

    print(f" {p} | {q} | {r} |    {q_implies_r}    |    {p_implies_q}    |    {p_implies_r} ")
# Proof Techniques
print("\nProof Techniques:")
# (a) Prove using Transitive
S1 = "q -> r"
S2 = "p -> q"
C = "S1 + S2 -> C = p -> r, Transitive"
print("Proof for (a): Phong goes to America")
print(f"S1: {S1}")
print(f"S2: {S2}")
print(f"C: {C}")
# (b) Prove using Modus Ponens
S1 = "Q -> R"
S2 = "P -> Q"
C = "S1 + S2 -> C = P -> R, Modus Ponens"
print("\nProof for (b): An is late for school")
print(f"S1: {S1}")
print(f"S2: {S2}")
print(f"C: {C}")

# Exercise 6
# Given matrix
A = [
    [2, 0, 5, 0, 3, 0],
    [3, 0, 0, 0, 0, 0],
    [0, 6, 2, 0, 5, 0],
    [3, 0, 9, 0, 25, 0],
    [0, 0, 2, 4, 5, 0],
    [0, 0, 0, 0, 0, 5]
]
# Definitions
def isOdd(a):
    return a % 2 != 0
def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True
def isSquare(a):
    return int(a ** 0.5) ** 2 == a
def isGreater(a, b):
    if isinstance(a, str) or isinstance(b, str):
        # If either a or b is a string, compare their lexicographic order
        return str(a) > str(b)
    else:
        # Otherwise, compare them as numbers
        return a > b
def isEqual(a, b):
    return a == b
def isAbove(a, b):
    row_a, col_a = find_element_coordinates(a)
    row_b, col_b = find_element_coordinates(b)
    return row_a < row_b
def isLeftOf(a, b):
    row_a, col_a = find_element_coordinates(a)
    row_b, col_b = find_element_coordinates(b)
    return col_a < col_b
def find_element_coordinates(element):
    for row_idx, row in enumerate(A):
        if element in row:
            return row_idx, row.index(element)
# Checking the statements
# (a) At least one a belongs to A, also (isOdd(a)) and isPrime(a)
result_a = any(isOdd(a) and isPrime(a) for row in A for a in row)
print(f"Statement (a) is {result_a}")
# (b) For every a belongs to A, isOdd(a) implies isSquare(a)
result_b = all(not isOdd(a) or isSquare(a) for row in A for a in row)
print(f"Statement (b) is {result_b}")
# (c) For every a belongs to A, isOdd(a) implies isGreater(a^2)
result_c = all(not isOdd(a) or isGreater(a**2, a) for row in A for a in row)
print(f"Statement (c) is {result_c}")
# (d) At least one a belongs to A, isPrime(a) implies also (isGreater(a, 3) or isEqual(a, 3))
result_d = any(isPrime(a) and (isGreater(a, 3) or isEqual(a, 3)) for row in A for a in row)
print(f"Statement (d) is {result_d}")
# (e) At least one a belongs to A, for every b belongs to A, isLeftOf(a, b)
result_e = any(all(isLeftOf(a, b) for b in row) for row in A for a in row)
print(f"Statement (e) is {result_e}")
# (f) At least one a belongs to A, for every b belongs to A, isGreater(a, b) implies also (isAbove(a, b))
result_f = any(all(isGreater(a, b) for b in row) for row in A for a in row) or any(
    all(isGreater(a, b) for b in [row[i] for row in A]) for i in range(len(A[0]))
)
print(f"Statement (f) is {result_f}")
# (g) For every a belongs to A, at least one b belongs to A, isPrime(a) and also (isOdd(a)) and isOdd(b) implies isAbove(a, b)
result_g = all(
    any(isPrime(a) and isOdd(a) and isOdd(b) and isAbove(a, b) for b in row) for row in A for a in row
)
print(f"Statement (g) is {result_g}")
# (h) For every a, b belongs to A, isSquare(a) and isEven(a) and isEven(b) and also (isEqual(a, b)) implies isLeftOf(b, a)
result_h = all(
    all(
        isSquare(a) and math.isEven(a) and math.isEven(b) and isEqual(a, b) and isLeftOf(b, a)
        for b in row
    )
    for row in A
    for a in row
)
print(f"Statement (h) is {result_h}")