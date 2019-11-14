# Given two string, write a method to decide if one string is a permutation of the other.


def arePermutatoin(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    if len1 != len2:
        return False

    # str1 = sorted(str1)
    # print(str1)
    a = sorted(str1)
    str1 = "".join(a)

    b = sorted(str2)
    str2 = "".join(b)

    for i in range(len1):
        if str1[i] != str2[i]:
            return False

    return True


str1 = "test"
str2 = "ttes"
ans = arePermutatoin(str1, str2)
if ans:
    print("Are Permutation")
else:
    print("Not permutation")