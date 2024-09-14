# Exercise 3
print("Exercise 3:")
statements = {
    'a': {"D": "people", "P": "is blond", "Q": "is westerner"},
    'b': {"D": "person", "P": "has black hair", "Q": "is westerner"},
    'c': {"D": "students", "P": "studies correctly", "Q": "has high score"},
    'd': {"D": "mammals", "P": "lives in the sea", "Q": "is a dolphin or a whale"},
    'e': {"D": "birds", "P": "doesn't have wings and can swim", "Q": "is a penguin"},
    'f': {"D": "bird", "P": "has wings but can't fly", "Q": "exists"}
}
for key, value in statements.items():
    print(f"For ({key}) D is \"{value['D']}\", P is \"{value['P']}\", Q is \"{value['Q']}\". Formal statement: for all x in D, P(x) then Q(x).")

# Exercise 6
print("\nExercise 6:")
for key, value in statements.items():
    print(f"For ({key}):")
    print(f"Negation: There exists a {value['D']} who {value['P']} but is not {value['Q']}.")
    print(f"Contrapositive: For all {value['D']}, if they are not {value['Q']} then they are not {value['P']}.")
    print(f"Converse: For all {value['D']}, if they are {value['Q']}, they are {value['P']}.")
    print(f"Inverse: For all {value['D']}, if they are not {value['P']}, they are not {value['Q']}.")
