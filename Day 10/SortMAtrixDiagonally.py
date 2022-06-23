# https://leetcode.com/problems/sort-the-matrix-diagonally/
# https://youtu.be/JBqUl7avtG8

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        
        for col in range(n):
            self.sort_matrix(mat,0,col,m,n)
            
        for row in range(1,m):
            self.sort_matrix(mat,row,0,m,n)
            
        return mat
    
    def sort_matrix(self,mat,row,col,m,n):
        ans = []
        r = row
        c = col
        
        while r < m and c < n:
            ans.append(mat[r][c])
            r+=1
            c+=1
            
        ans.sort()
        
        r = row
        c = col
        ind = 0
        
        while r < m and c < n:
            mat[r][c] = ans[ind]
            ind+=1
            r+=1
            c+=1
            