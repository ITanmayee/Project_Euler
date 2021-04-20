# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    s = str(n)
    if s == s[::-1] :
        return True
    return False 

def get_largest_palindrome(digit) :
    prod = [i * j for i in range((10 ** digit) -1) for j in range((10 ** digit) -1) if is_palindrome(i * j) ]
    return max(prod)
print(get_largest_palindrome(3))
