def sort(a):
    # a.sort()
    # for i in range(len(a)):
    #     print(a[i], end = ' ')
    for j in range(1, len(a)):
        key = a[j]
        i = j - 1
        while i>=0 and a[i]>key:
            a[i+1] = a[i]
            i = i - 1
        a[i+1] = key

    for i in range(len(a)):
        print(a[i], end = " ")

a = [10, 12, 5]
sort(a)