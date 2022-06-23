# https://practice.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1#
# https://www.youtube.com/watch?v=tFdBRcHLSGQ

class Solution:
    def median(self, matrix, r, c):
    #code here 
    
        start = 0
        end = 2000 ## Given Constraint
        
        while start <= end:
            
            mid = (start + end) // 2
            count = 0
            
            for i in range(r):
                l = 0
                h = c-1
                
                while l <= h:
                
                    m = (l+h)//2
                    
                    if matrix[i][m] <= mid:
                        l = m + 1
                    else:
                        h = m - 1
                    
                count += l
            
            if count <= (r*c)//2:
                start = mid + 1
            
            else:
                end = mid - 1
        
        return start