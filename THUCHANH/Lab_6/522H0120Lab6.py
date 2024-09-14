#Ex1
def nextPrime(n):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    next_num = n + 1
    while True:
        if isPrime(next_num):
            return next_num
        next_num += 1
print("Ex1:")
print(f"Number that is right next to n = 3 is: {nextPrime(3)}")
print(f"Number that is right next to n = 8 is: {nextPrime(8)}")

#Ex2
def primeFact(p):
    prime_factors = []
    #Divide by 2 until p is not divisible by 2
    while p % 2 == 0:
        prime_factors.append(2),
        p = p / 2
    #p must be odd at this point, thus skip the even numbers and iterate only for odd
    for i in range(3, int(p**0.5)+1, 2):
        while p % i== 0:
            prime_factors.append(i)
            p = p / i
    #This condition is to handle the case when p is a prime number greater than 2
    if p > 2:
        prime_factors.append(int(p))
    return prime_factors
print("Ex2:")
print(f"The prime factorization of p = 60 is: {primeFact(60)}")

#Ex3
def printPrime(N):
    def isPrime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    for num in range(2, N):
        if isPrime(num):
            print(num)
print("Ex3:")
printPrime(20)

#Ex4
def contestResult(n):
    if n < 2:
        return []
    else:
        O = [2]
        i = 3
        while True:
            flag = True
            j = 0
            while j < len(O):
                if i % O[j] == 0:
                    flag = False
                    break
                j += 1
            if flag:
                O.append(i)
            if i + 2 < n:
                i += 2
            else:
                return O
print("Ex4:")
print(f"The result with n = 10 is: {contestResult(10)}")
print(f"The result with n = 20 is: {contestResult(20)}")
print(f"The result with n = 5 is: {contestResult(5)}")

#Ex5
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
print("Ex5:")
# GCD is greatest common divisor
print(f"GCD of 24 and 36 is: {gcd(24, 36)}")  # Output: 12
print(f"GCD of 48 and 60 is: {gcd(48, 60)}")  # Output: 12
print(f"GCD of 17 and 23 is: {gcd(17, 23)}")  # Output: 1

#Ex6
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def lcm(a, b):
    return (a * b) // gcd(a, b)
print("Ex6:")
# LCM is least common multiple
print(f"LCM of 12 and 18 is: {lcm(12, 18)}") # Output: 36
print(f"LCM of 15 and 25 is: {lcm(15, 25)}") # Output: 75
print(f"LCM of 7 and 9 is: {lcm(7, 9)}") # Output: 63

#Ex7
def convertToBase2(n):
    binary = []
    while n > 0:
        binary.append(str(n % 2))
        n //= 2
    binary.reverse()
    return ''.join(binary)
print("Ex7:")
print(f"5 in binary is: {convertToBase2(5)}")# Output: 101
print(f"15 in binary is: {convertToBase2(15)}")# Output: 1111
print(f"6 in binary is: {convertToBase2(6)}")# Output: 110

#Ex8
def convertFractionToBinary(n):
    binary = "."
    while n > 0:
        n *= 2
        if n >= 1:
            binary += "1"
            n -= 1
        else:
            binary += "0"
    return binary
def convertToBinary(n):
    binary = bin(n)[2:]
    return binary
print("Ex8:")
print(f"5.5 in binary is: {convertToBinary(5) + convertFractionToBinary(0.5)}")
print(f"15.25 in binary is: {convertToBinary(15) + convertFractionToBinary(0.25)}")
print(f"6.75 in binary is: {convertToBinary(6) + convertFractionToBinary(0.75)}")

# Exercise 9
def base10ToBase16(n):
    hex_chars = "0123456789ABCDEF"
    hex_str = ""
    while n > 0:
        remainder = n % 16
        hex_str = hex_chars[remainder] + hex_str
        n //= 16
    return hex_str if hex_str else "0"

print("\nExercise 9:")
print(f"15 in hexadecimal is: {base10ToBase16(15)}")
print(f"100 in hexadecimal is: {base10ToBase16(100)}")

# Exercise 10
def convertBase(a, base1, base2):
    decimal = 0
    for i, digit in enumerate(reversed(a)):
        decimal += digit * (base1 ** i)
    
    result = []
    while decimal > 0:
        result.append(decimal % base2)
        decimal //= base2
    result.reverse()
    return result

print("\nExercise 10:")
print(f"Converting 111 from base 10 to base 16: {convertBase([1, 1, 1], 10, 16)}")
print(f"Converting 101 from base 2 to base 16: {convertBase([1, 0, 1], 2, 16)}")