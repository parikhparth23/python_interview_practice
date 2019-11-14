# Compress a string made up of letters by replacing each substring containing
# a single type of letter by that letter followed by the count if the result
# is shorter than the original.


def stringCompression(stra):
    str2 = ""
    count = 1
    stra = stra + ' '
    for i in range(0, len(stra)-1):
        if stra[i] != stra[i+1]:
            str2 = str2 + stra[i] + str(count)
            count = 1
        else:
            count += 1

    if len(stra) > len(str2):
        return str2
    else:
        return stra


stra = "aabcccccaaa"
print(stringCompression(stra))