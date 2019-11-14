# Write a method to replace all the spaces in a string with ‘%20’.
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the “true” length of the string.


def replaceSpaces(str1, str_size):
    str1 = str1.strip()
    new_str = str1.replace(' ', '%20')
    print(new_str)


str1 = "  Mr John Smith  "
str_size = 13
replaceSpaces(str1, str_size)
