def formalConvert(S):
    parts = S.split(',')
    D = parts[0].split(' ')[-1]
    P = parts[1].strip()
    if S.startswith('For all'):
        F = f'For all x in {D}, {P}(x)'
    else:
        F = f'There exists an x in {D} such that {P}(x)'

    return D, P, F


S = '(a) For all fishes, they need water to survive.'
D, P, F = formalConvert(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Formal form: {F}')

S = '(b) Exist a person, who is left handed.'
D, P, F = formalConvert(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Formal form: {F}')

S = '(c) Exist an employee in the company, who is late to work everyday.'
D, P, F = formalConvert(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Formal form: {F}')

S = '(d) For all fishes in this pond, they are Koi fish.'
D, P, F = formalConvert(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Formal form: {F}')

S = '(e) There is at least one creature in the ocean, it can live on land.'
D, P, F = formalConvert(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Formal form: {F}')

S = '(f) Every students in class A did not pass the test.'
D, P, F = formalConvert(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Formal form: {F}')