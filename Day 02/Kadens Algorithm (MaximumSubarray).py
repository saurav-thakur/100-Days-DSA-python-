# https://leetcode.com/problems/maximum-subarray/
# https://practice.geeksforgeeks.org/problems/kadanes-algorithm-1587115620/1

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        maxsum = 0
        cumsum = 0
        maxNeg = float('-inf')
        count = 0
        
        for i in range(len(nums)):
            
            if nums[i] < 0:
                if nums[i] > maxNeg:
                    maxNeg  = nums[i]
                    
                count+=1
            
            
            cumsum+=nums[i]
            
            if cumsum < 0:
                cumsum = 0
            
            if cumsum > maxsum:
                maxsum = cumsum
                
        if len(nums) == count:
            return maxNeg
                
        return maxsum
                