def formalConvertPQ(S):
    parts = S.split(',')
    D = parts[0].split(' ')[-1]
    P = parts[1].split(' if ')[-1].split(' then ')[0]
    Q = parts[1].split(' then ')[-1]
    if S.startswith('For all'):
        F = f'For all x in {D}, if {P}(x) then {Q}(x)'
    else:
        F = f'There exists an x in {D} such that {P}(x) and {Q}(x)'
    return D, P, Q, F

S = 'For all people, if they are blond then they are westerners.'
D, P, Q, F = formalConvertPQ(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Q is {Q}')
print(f'Formal form: {F}')

S = 'Exist a person, whose hair is black but is a westerner.'
D, P, Q, F = formalConvertPQ(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Q is {Q}')
print(f'Formal form: {F}')

S = 'For all students, if they study correctly then they have high score.'
D, P, Q, F = formalConvertPQ(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Q is {Q}')
print(f'Formal form: {F}')

S = 'For every mammal, if they live in the sea, they are either dolphins or whales.'
D, P, Q, F = formalConvertPQ(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Q is {Q}')
print(f'Formal form: {F}')

S = 'For every bird, if they dont have wings and can swim then they are penguins.'
D, P, Q, F = formalConvertPQ(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Q is {Q}')
print(f'Formal form: {F}')

S = 'Exist a bird, who have wing but cant fly.'
D, P, Q, F = formalConvertPQ(S)
print(f'D is {D}')
print(f'P is {P}')
print(f'Q is {Q}')
print(f'Formal form: {F}')