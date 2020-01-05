arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

numrows = len(arr)
numcols = len(arr[0])

for i in range(numrows):
    for k in range(numcols):
        if i == k:
            print(arr[i][k], end=" ")

print()

for i in range(numrows):
    print(arr[numcols-1][i], end=" ")
    numcols -= 1