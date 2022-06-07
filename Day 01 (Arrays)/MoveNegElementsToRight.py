# https://practice.geeksforgeeks.org/problems/move-all-negative-elements-to-end1813/1#
# https://www.youtube.com/watch?v=Jc6vv-m8oWw

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        
        ans = []
        
        for i in arr:
            if i >= 0:
                ans.append(i)
                
        for j in arr:
            if j < 0:
                ans.append(j)
        
        for k in range(len(arr)):
            arr[k] = ans[k]