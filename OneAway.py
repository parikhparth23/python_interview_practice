# Determine whether the edit distance between two strings is less than 2.


def isEditDistanceOne(s1, s2):
    len1 = len(s1)
    len2 = len(s2)

    if abs(len1 - len2) > 1:
        return False

    count = 0

    i = 0
    k = 0

    while i < len1 and k < len2:
        if s1[i] != s2[k]:
            if count == 1:
                return False

            if len1 > len2:
                i += 1
            elif len1 < len2:
                k += 1
            else:
                i += 1
                k += 1

            count += 1
        else:
            i += 1
            k += 1

    if i < len1 or k < len2:
        count += 1

    return count == 1


s1 = "pale"
s2 = "bake"

if isEditDistanceOne(s1, s2):
    print("Yes")
else:
    print("No")
