# Given a matrix, zero out every row and column that contains a zero.

def zero_out_row_col(mat1):
    rows = len(mat1)
    columns = len(mat1[0])

    ipositions = {}
    jpositions = {}

    for i in range(0, rows):
        for j in range(0, columns):
            if mat1[i][j] == 0:
                ipositions[i] = 9
                jpositions[j] = 6

    # print(ipositions)
    # print(jpositions)
    for i in ipositions.keys():
        for j in range(0, columns):
            mat1[i][j] = 0

    for j in jpositions.keys():
        for i in range(0, rows):
            mat1[i][j] = 0


mat1 = [[1, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1]]
mat2 = [[1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [1, 0, 1, 0, 1], [0, 0, 0, 0, 0]]
zero_out_row_col(mat1)

if mat1 == mat2:
    print(True)
else:
    print(False)