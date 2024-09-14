def nega(A):
    parts = A.split(',')
    # The domain D is the part after 'For all ', 'Exist ' or 'There is at least one ' and before the comma
    D = parts[0].split(' ')[-1]
    # The predicate P is the part after the comma
    P = parts[1].strip()
    # The negation N is 'Exist x in D, not P(x)' if the statement starts with 'For all' and 'For all x in D, not P(x)' if the statement starts with 'Exist' or 'There is at least one'
    if A.startswith('For all'):
        N = f'Exist {D}, not {P}'
    else:
        N = f'For all {D}, not {P}'
    return N

A = 'For all fishes, they need water to survive'
N = nega(A)
print(f'Negation of the statement is: {N}')