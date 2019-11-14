# Reverse a String

def reverse(str):
    rev_str = ""
    for i in str:
        print(i)
        rev_str = i + rev_str
    return rev_str


str = "Heli Parikh"

print("The original string is: ")
print(str)

print("The reversed string is: ")
print(reverse(str))
