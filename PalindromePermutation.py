# Determine whether or not a string is a permutation of a palindrome,


def palindromePermutation(str):
    str = str.lower()
    str = str.replace(" ", "")
    list = {}

    for i in range(len(str)):
        if str[i] in list:
            list[str[i]] += 1
        else:
            list[str[i]] = 1

    add = 0
    for i in list.values():
        # print(i, "->", list[i])
        if i%2 > 0:
            add += 1
            if add > 1:
                return False
    return True


str = "Tact Coa"
print(palindromePermutation(str))