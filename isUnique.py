#  Implement an algorithm to determine if a string has all unique characters.

def isUniqueChars(str):
    if (len(str)) > 256:
        return False

    char_Set = [False] * 128

    for i in range(len(str)):
        # ord = return an integer representing the Unicode code point of the character
        val = ord(str[i])

        if char_Set[val]:
            return False

        char_Set[val] = True

    return True


str = "geeks for geeks"
print(isUniqueChars(str))
