def firstNonRepeating(data):
    count = {}
    order = []

    for i in data:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            order.append(i)

    for x in order:
        if count[x] == 1:
            return x

    return None


data = "geeks for geeks"
print(firstNonRepeating(data))
