def strStr(haystack, needle):
    if needle in haystack:
        return haystack.index(needle)
    return -1


haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))

