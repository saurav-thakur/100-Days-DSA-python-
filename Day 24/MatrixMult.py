def multiply_mat(mat1,mat2):
    r1 = len(mat1) - 1
    c1 = len(mat1[0]) - 1

    r2 = len(mat2) - 1
    c2 = len(mat2[0]) - 1

    ans = []

    if (c1!=r2):
        return ans

    for i in range(len(mat1)):
        for j in range(len(mat2)):
            res = 0
            for k in range(len(mat2)):
                res+=mat1[i][j]*mat2[k][j]
                ans.append(res)

    return ans
                
                

    

    


mat1 = [
  [0, 0,  0],
  [0, 0, 20],
]


mat2 = [[0, 10, 0],
  [0,  0, 0],
  [0,  0, 4],
]
print(multiply_mat(mat1,mat2))