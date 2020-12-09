import re

def is_palindrome(str):
    """ Identify if a string is a palidrome """
    str = str.lower()
    ltrs = re.findall('[a-z]',str)
    l = 0
    r = len(ltrs)-1
    while l<=r:
        if ltrs[l] != ltrs[r]: return False
        l = l + 1
        r = r - 1
    return True

def is_palindrome_ans(str):
    """ Could solve in three lines """
    # join the findall of a-z into a string
    fwd = ''.join(re.findall('[a-z]',str.lower()))
    bwd = fwd[::-1]
    return fwd == bwd

print(is_palindrome_ans("Go hang a salami - I'm a lasagna hog."))
print(is_palindrome_ans("A man a plan, a canal panama"))
print(is_palindrome_ans("Get the money"))
