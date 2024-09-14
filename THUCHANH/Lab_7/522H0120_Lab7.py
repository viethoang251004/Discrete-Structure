#Exercise 1
def calculateThieves(day):
    if day == 1:
        return 1
    else:
        return day + calculateThieves(day - 1)

def calculateMaxDays(totalThieves):
    day = 1
    while calculateThieves(day) <= totalThieves:
        day += 1
    return day - 1

print(calculateThieves(5))
print(calculateMaxDays(40))
print(calculateMaxDays(100))

#Exercise 2
def richest(X):
    if len(X) == 1:
        return X[0]  # If there is only one man, he is the richest
    else:
        current_richest = X[-1]  # Assume the last man is the current richest
        previous_richest = richest(X[:-1])  # Recursively find the previous richest
        if current_richest > previous_richest:
            return current_richest
        else:
            return previous_richest
wealth = [10, 15, 5, 20, 25]
print(richest(wealth))

# Exercise 3
def find_k(n, target):
    # Create a 2D table to store the number of ways to choose k from n
    ways = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Base cases: if k = 0 or k = n, there is only 1 way to choose
    for i in range(n+1):
        ways[i][0] = 1
        ways[i][i] = 1
    
    # Fill in the table using the recursive formula
    for i in range(1, n + 1):
        for k in range(1, i + 1):
            ways[i][k] = ways[i-1][k] + ways[i-1][k-1]
    
    # Find the value of k that gives the number of ways closest to the target
    closest_k = None
    closest_diff = float('inf')
    for k in range(n + 1):
        diff = abs(ways[n][k] - target)
        if diff < closest_diff:
            closest_k = k
            closest_diff = diff
    
    return closest_k

n = 50
target = 1000
k = find_k(n, target)
print(k)  # Output: 7