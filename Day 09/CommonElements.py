
from sympy import li


def find_common(mat):
    d = {}
    new_mat = set()
    ans = []

    for i in mat:
        for j in i:
            new_mat.add(j)

    new_mat = list(new_mat)

    for i in range(len(mat)):
        row = i

        for j in range(len(mat[0])):
            
            if mat[i][j] not in d:
                d[new_mat[i][j]] = i
                

            elif mat[i][j] in d and d[mat[i][j]] == i:

            
mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]

find_common(mat)


    # for key,value in d.items():
    #     if value == len(mat):
    #         ans.append(key)

    
