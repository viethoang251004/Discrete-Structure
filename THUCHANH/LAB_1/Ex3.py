def sumN(n):
    if n >= 0:
        return sum(range(n + 1))
    else:
        return sum(range(n, 1))
# Test cases
result1 = sumN(2)
print(f"sumN(2) = {result1}")  # Output: 0 + 1 + 2 = 3

result2 = sumN(-5)
print(f"sumN(-5) = {result2}")  # Output: 0 + (-1) + (-2) + (-3) + (-4) + (-5) = -15
