from sympy import symbols
from sympy.logic.boolalg import Implies, Not, Or, And
from sympy.logic.inference import satisfiable

# Define the variables
p, q, r, s, t = symbols('p q r s t')

# Check the arguments
arguments = [
    # (a)
    (Implies(p, r), Implies(Not(p), q), Implies(q, r), Implies(Not(r), s)),
    # (b)
    (Implies(p, Implies(q, r)), Or(p, s), Implies(t, q), Not(s), Implies(Not(r), Not(t))),
    # (c)
    (Implies(p, q), Or(Not(r), s), Or(p, r), Implies(Not(q), s)),
    # (d)
    (p, Implies(p, r), Implies(p, Or(q, Not(r))), Or(Not(q), Not(s)), s)
]

for i, argument in enumerate(arguments, start=1):
    premises = argument[:-1]
    conclusion = argument[-1]
    # The argument is valid if it's impossible for all the premises to be true and the conclusion to be false at the same time
    if not satisfiable(And(*premises, Not(conclusion))):
        print(f"(a{i}) is valid")
    else:
        print(f"(a{i}) is not valid")
