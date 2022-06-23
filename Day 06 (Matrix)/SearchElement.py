# https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        r = len(matrix) 
        c = len(matrix[0]) - 1

        for i in range(r):

            if target == matrix[i][0] or target == matrix[i][c]:
                return True

            if target > matrix[i][0] and target < matrix[i][c]:

                start = 0
                end = c

                while start <= end:

                    mid = start + (end-start)//2

                    if matrix[i][mid] == target:
                        return True

                    if target > matrix[i][mid]:
                        start = mid + 1
                    else:
                        end = mid - 1

        return False
        