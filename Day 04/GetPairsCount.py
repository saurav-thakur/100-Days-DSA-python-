# https://practice.geeksforgeeks.org/problems/count-pairs-with-given-sum5022/1

class Solution:
    def getPairsCount(self, arr, n, k):
        # code here
        count = 0
        d = {}
        
        for i in range(len(arr)):
            diff = k - arr[i]
            
            if diff in d:
                count += d[diff]
            
            
            if arr[i] not in d:
                d[arr[i]] = 1
                
            else:
                d[arr[i]] += 1
                
        return count