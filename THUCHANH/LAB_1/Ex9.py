# (a)
def ithCombine(p, q):
    result = "if {}, then {}".format(p, q)
    return result
# Example usage
p = "it is sunny"
q = "I go camping"
combined = ithCombine(p, q)
print(combined)

# (b)
def panqCombine(p, q):
    result = "{} and not {}".format(p, q)
    return result
# Example usage
p = "it is sunny"
q = "I go camping"
combined = panqCombine(p, q)
print(combined)

# (c)
def npoqCombine(p, q):
    result = "not {} or {}".format(p, q)
    return result
# Example usage
p = "it is sunny"
q = "I go camping"
combined = npoqCombine(p, q)
print(combined)