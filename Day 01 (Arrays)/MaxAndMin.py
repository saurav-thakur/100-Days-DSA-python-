# https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1

def max_min(nums):
    maxNum = nums[0]
    minNum = nums[0]

    for i in range(len(nums)):
        if nums[i] < minNum:
            minNum = nums[i]
        
        elif nums[i] > maxNum:
            maxNum = nums[i]

    return minNum,maxNum


nums = [-1,2,3,-5,3,7,1,33,-32,]
print(max_min(nums))
