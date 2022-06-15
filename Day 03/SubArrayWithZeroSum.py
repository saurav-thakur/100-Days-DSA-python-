# https://practice.geeksforgeeks.org/problems/subarray-with-0-sum-1587115621/1
# https://www.youtube.com/watch?v=8inhayLCCHs&t=582s

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        d = {}
        
        cumsum = 0
        
        for i in range(len(arr)):
            
            if arr[i] == 0:
                return True
            
            cumsum += arr[i]
            
            if cumsum == 0:
                return True
            
            if cumsum not in d:
                d[cumsum] = i
                
            else:
                return True
                
        return False
        