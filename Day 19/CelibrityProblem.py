# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1/

def celibrity_problem(M):
    stack = []
    n = len(M)
  
    for i in range(n):
        stack.append(i)
        
    while (len(stack) > 1):
        
        a = stack.pop()
        
        b = stack.pop()
        
        if M[a][b] == 1:
            stack.append(b)
        else:
            stack.append(a)
            
    rowans = stack.pop()
    print(rowans)
    # rowcheck
    rowCheck = False
    zeroCount = 0
    for j in range(len(M[0])):
        if M[rowans][j] == 0:
            zeroCount += 1

        if zeroCount == n:
            rowCheck = True

        # colcheck
    colCheck = False
    oneCount = 0
    for i in range(len(M)):
        if M[i][rowans] == 1:
            oneCount += 1

        if oneCount == n-1:
            colCheck = True
    if colCheck and rowCheck:
        return rowans
    return -1 
    




mat = [[0,1,0],
        [0,0,0],
        [0,1,0]]
# mat = [[0,0,0],
#         [0,0,0],
#         [0,0,0]]

# mat = [[0, 1, 1, 0], 
# [0 ,0 ,0 ,1],
# [1 ,1 ,0 ,1], 
# [1, 1 ,1 ,0]]
            
print(celibrity_problem(mat))