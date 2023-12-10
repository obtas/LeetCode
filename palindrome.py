""" Given a string s, return true if it is a palindrome, false otherwise"""

s = "racecar"
t = "palindrome"

# print(len(s))

def check_palindrome(s):
    left = 0
    right = len(s)-1

    while left < right:
        if s[left] != s[right]:
            return False
        left +=1
        right -=1
    return True

# print(check_palindrome(t))