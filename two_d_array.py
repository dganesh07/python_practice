
def print_matrix(m):
    print()
    for l in m:
        for x in l:
            print(x , "\t")
        print()

matrix = [
    [1, 5, 45, 0, 81],
    [6, 7, 2, 82, 8],
    [20, 22, 49, 5, 5],
    [0, 23, 50, 4, 92],
]
def zero_matrix(matrix):
    if not matrix:
        return 
    
    zero_col = set()
    zero_row = set()

    rows = len(matrix)
    cols = len(matrix[0])

    # this loop is to keep track of the index of rows or cols that has zeros
    for i in range(0, rows):
        for j in range(0, cols):
            if matrix[i][j] == 0:
                if i not in zero_row:
                    zero_row.add(i)
                if j not in zero_col:
                    zero_col.add(j)

    #zero_row is the index of row where zero exists 
    #zero_col is the index of column where zero exists 

    for r in zero_row:
        for c in range(0, cols):
            matrix[r][c] = 0

    for c in zero_col:
        for r in range(0, rows):
            matrix[r][c] = 0

    print_matrix(matrix)

zero_matrix(matrix)

