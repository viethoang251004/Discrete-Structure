def extended_gcd(a, b):
    """Extended Euclidean Algorithm that returns gcd of a and b, and coefficients x and y
    such that ax + by = gcd(a, b)"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def modular_inverse(a, n):
    """Function to find the modular inverse of a under modulo n using Extended Euclidean Algorithm"""
    gcd, x, y = extended_gcd(a, n)
    if gcd != 1:
        return None  # No modular inverse exists if gcd is not 1
    return x % n


# Tests
test_cases = [(10, 17), (5, 12), (6, 9)]
results = {(a, n): modular_inverse(a, n) for a, n in test_cases}

for (a, n), inverse in results.items():
    if inverse is not None:
        print(f"The modular inverse of {a} modulo {n} is {inverse}")
    else:
        print(f"No modular inverse exists for {a} modulo {n}")
