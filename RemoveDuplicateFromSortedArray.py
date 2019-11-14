
def removeDuplicate(arr):
    if len(arr) == 0 or len(arr) == 1:
        return len(arr)

    temp = list(range(len(arr)))
    k = 0

    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            temp[k] = arr[i]
            k += 1
            print("value is:"+k)

    temp[k] = arr[len(arr) - 1]
    k += 1

    for i in range(0, k):
        arr[i] = temp[i]

    return k


# arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
arr = [1, 1, 1, 1]

n = removeDuplicate(arr)

for i in range(n):
    print ("%d"%(arr[i]), end = " ")
