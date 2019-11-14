def firstRepeating(data):
    order = []
    dict = {}

    for i in data:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            order.append(i)

    for i in order:
        if dict[i] == 2:
            return i

    return None


data = "geeks for geeks"
print(firstRepeating(data))