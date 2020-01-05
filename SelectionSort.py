arr = [12, 11, 13, 5, 6]


for i in range (0, len(arr) - 1):
    minIndex = i
    for k in range (i+1, len(arr)):
        if arr[minIndex] > arr[k]:
            minIndex = k

    arr[i], arr[minIndex] = arr[minIndex], arr[i]
    # arr[i] = arr[minIndex]
    # arr[minIndex] = arr[i]


for i in range(len(arr)):
    print("%d" %arr[i], end=" ")
