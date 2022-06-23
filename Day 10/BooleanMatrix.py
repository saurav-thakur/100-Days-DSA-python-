# https://practice.geeksforgeeks.org/problems/boolean-matrix-problem-1587115620/0/?track=md-matrix&batchId=144
# https://www.youtube.com/watch?v=TBTNZXzwpP8


#Function to modify the matrix such that if a matrix cell matrix[i][j]
#is 1 then all the cells in its ith row and jth column will become 1.
def booleanMatrix(matrix):
    # code here 
    
    r = len(matrix)
    c = len(matrix[0])
    
    arr_row = [0 for i in range(r)]
    arr_col = [0 for i in range(c)]
    
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 1:
                arr_row[i] = 1
                arr_col[j] = 1
    
    for i in range(r):
        if arr_row[i] == 1:
            for j in range(c):
                matrix[i][j] = 1
                
    for i in range(c):
        if arr_col[i] == 1:
            for j in range(r):
                matrix[j][i] = 1

###-------------------------------- My Approach ----------------------
### O(N) Space 
def booleanMatrix(mat):
    r = len(mat)
    c = len(mat[0])

    new_mat = [[0 for i in range(c)] for i in range(r)]

    for i in range(len(mat)):
        for j in range(len(mat[0])):

            if mat[i][j] == 1:

                # The downward column and row from that place
                row = i
                col = j

                while col < c:
                    new_mat[row][col] = 1
                    col+=1
                col = j
                while row < r:
                    new_mat[row][col] = 1
                    row+=1

                #  The upward column and row from that place
                row = i
                col = j

                while col >= 0:
                    new_mat[row][col] = 1
                    col-=1
                col = j
                while row >= 0:
                    new_mat[row][col] = 1
                    row-=1


    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] = new_mat[i][j]

    return mat

mat = [[1,0],
        [0,0]]
# mat = [[ 1, 0, 0],
#               [ 1, 0, 0],
#               [ 1, 0, 0],
#               [ 0, 0, 0]]
# print(mat)
print(booleanMatrix(mat))


            