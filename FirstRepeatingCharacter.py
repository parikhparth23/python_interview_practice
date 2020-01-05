def firstRepeating(data):
    order = []
    dict = {}
    count = 0

    for i in data:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            order.append(i)

    # print(order)
    # print(dict)
    # for i in order:
    #     if dict[i] >= 2:
    #         count += 1
    #         if count == 2:
    #             return i

    for i in order:
        if dict[i] > 1:
            return i

    return None


data = "geeks for geeks"
print(firstRepeating(data))