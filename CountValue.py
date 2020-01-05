arr = [1, 2, 1, 3, 1, 3]

dict = {}

for i in arr:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for key, value in sorted(dict.items()):
    print(key, ":", value)