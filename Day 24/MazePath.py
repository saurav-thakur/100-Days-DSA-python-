# # 1. You are given a number n and a number m representing number of rows and columns in a maze.
# 2. You are standing in the top-left corner and have to reach the bottom-right corner. Only two moves are allowed 'h' (1-step horizontal) and 'v' (1-step vertical).
# 3. Complete the body of getMazePath function - without changing signature - to get the list of all paths that can be used to move from top-left to bottom-right.
# Use sample input and output to take idea about output.

# Sample Input ->3,3 -> m,n
# O/p - > [hhvv, hvhv, hvvh, vhhv, vhvh, vvhh]


countPath = 0
def mazePath(n,m,i,j,osf):
    global countPath
    if i == n-1 and j == m-1:
        countPath+=1
        print(f"{osf}")
        return

    if i >= n or j >= m:
        return

    mazePath(n,m,i+1,j,osf+"D") # Down
    mazePath(n,m,i,j+1,osf+"R") # Right
    mazePath(n,m,i+1,j+1,osf+"->") # diagonal
    

    

n = 3
m = 3
i = 0
j = 0
osf = ""
mazePath(n,m,i,j,osf)
print(countPath)