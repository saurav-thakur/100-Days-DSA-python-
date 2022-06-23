

# reversing and then transposing the matrix
def rotate_matrix(mat): 

    new_mat = [[None for i in range(len(mat[0]))] for i in range(len(mat))]

    up = 0
    down = len(mat) -  1

    while up <= down: # Reverse the matrix
        mat[up],mat[down] = mat[down],mat[up]
        up+=1
        down -= 1

    # for i in range(len(mat)): # Transpose the matrix in O(N) space
    #     for j in range(len(mat[0])):
    #          new_mat[j][i] = mat[i][j]

    # print(new_mat)

    for i in range(len(mat[0])): # Transpose the matrix in O(1) space
        for j in range(i+1,len(mat)):
            mat[i][j],mat[j][i] = mat[j][i],mat[i][j]

    return mat




arr = [ [ 1, 2, 3, 4 ],
          [ 5, 6, 7, 8 ],
          [ 9, 10, 11, 12 ],
          [ 13, 14, 15, 16 ] ]


rotate_matrix(arr)