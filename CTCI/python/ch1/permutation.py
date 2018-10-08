"""
Given two strings, write a method to decided if one is a permutaion of the other
"""
def check_perumutation(a, b):
    ascii_count = {}

    for ch in a:
        if ch in ascii_count:
            ascii_count[ch] += 1
        else:
            ascii_count[ch] = 1
    
    for ch in b:
        if ch in ascii_count:
            ascii_count[ch] -= 1
        else:
            return False
        
    return sum(ascii_count.values()) == 0

print check_perumutation("aaba", "baaa")
print check_perumutation("no", "yes")