def insertionSort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i>=0 and arr[i]>key:
            arr[i+1] = arr[i]
            i = i-1
        arr[i+1] = key


def insertionSortNonIncreasing(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j-1
        while i>=0 and arr[i]<key:
            arr[i+1] = arr[i] 
            i = i-1
        arr[i+1] = key

arr = [5,2,4,6,1,3]
# insertionSort(arr)
insertionSortNonIncreasing(arr)
print("sorted array is:")
for i in range(len(arr)):
    print(arr[i], end = '')
    print(" ", end = '')
print()

