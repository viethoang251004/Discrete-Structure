"""
**1/ Number of thieves to send:**
"""

def calculate_thieves(day):
    if day == 1:
        return 1
    else:
        return day + calculate_thieves(day - 1)
def days_until_no_thieves(thieves):
    day = 1
    while True:
        if calculate_thieves(day) > thieves:
            return day - 1
        day += 1
num_thieves = 40
days = days_until_no_thieves(num_thieves)
print(f"Number of days until no more thieves can be sent: {days}")

"""
**2/ Find the richest person:**
"""

def richest(X, prev_richest=float('-inf')):
    if len(X) == 0:
        return prev_richest
    else:
        if X[0] > prev_richest:
            return richest(X[1:], X[0])
        else:
            return richest(X[1:], prev_richest)
# Example usage
wealth_list = [100, 200, 50, 300, 150]
richest_person = richest(wealth_list)
print(f"The richest person has a wealth of {richest_person}")

"""**3/ Find k closest to 1000 for the number of combinations:**"""

memo = {}
def waytochoose(n, k):
    if (n, k) in memo:
        return memo[(n, k)]
    if k == 0 or k == n:
        result = 1
    else:
        result = waytochoose(n - 1, k) + waytochoose(n - 1, k - 1)
    memo[(n, k)] = result
    return result
n = 50
min_diff = float('inf')
best_k = 0
for k in range(51):
    diff = abs(waytochoose(n, k) - 1000)
    if diff < min_diff:
        min_diff = diff
        best_k = k
print(f"The value of k closest to 1000 is: {best_k}")

"""**4/ Find k closest to 10000 for the number of permutations:**"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
def waytochooseP(n, k):
    return factorial(n) // factorial(n - k)
n = 50
min_diff = float('inf')
best_k = 0
for k in range(51):
    diff = abs(waytochooseP(n, k) - 10000)
    if diff < min_diff:
        min_diff = diff
        best_k = k
print(f"The value of k closest to 10000 is: {best_k}")

"""**5/ Calculate the total number of characters in the stories:**"""

def char_count(n):
    if n == 0:
        return 0
    else:
        return n**2 + char_count(n - 1)
num_stories = 547
total_chars = char_count(num_stories)
print(f"The total number of characters in Scheherazade's stories is: {total_chars}")

"""**6/ Calculate the nth Fibonacci number:**"""

def fibonacci(n):
    if n < 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
# Example usage
n = 10
fib_n = fibonacci(n)
print(f"The {n}th Fibonacci number is: {fib_n}")

"""**7/ Solve the Tower of Hanoi problem:**"""

def towerOfHanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    towerOfHanoi(n - 1, source, auxiliary, destination)
    print(f"Move disk {n} from {source} to {destination}")
    towerOfHanoi(n - 1, auxiliary, destination, source)
n = 5  # Number of disks
print("Steps to solve the Tower of Hanoi problem with 5 disks:")
towerOfHanoi(n, 'A', 'C', 'B')