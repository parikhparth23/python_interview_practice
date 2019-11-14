# Determine whether or not a given string is a rotation of another string.


def isRotation(str1, str2):
    tmp = str1 + str1
    len1 = len(str1)
    len2 = len(str2)

    if len1 != len2:
        return False

    if tmp.count(str2) > 0:
        return True
    else:
        return False


str1 = "waterbottle"
str2 = "erbottlewat"
print(isRotation(str1, str2))
