import re

def isPalindrome(s):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    print(s)

    if s == s[::-1]:
        return True
    else:
        return False


s = "A man, a plan, a canal: Panama"
print(isPalindrome(s))