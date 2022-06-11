# https://leetcode.com/problems/find-the-duplicate-number/
# https://www.youtube.com/watch?v=pavdSf5f5pw

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break
                
        fast = nums[0]
        
        while slow!=fast:
            slow = nums[slow]
            fast = nums[fast]
            
        return slow