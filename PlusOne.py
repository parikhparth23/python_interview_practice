def plusOne(digits):
    sum = 0
    length = len(digits)

    for i in range(0, length):
        sum *= 10
        sum = sum + int(digits[i])

    sum +=1

    itoa = str(sum)

    return list(itoa)


print(plusOne([4, 3, 2, 1]))
