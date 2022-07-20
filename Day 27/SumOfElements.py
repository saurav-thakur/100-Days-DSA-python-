def sum_elements(nums,idx,sum_ele):
    if idx == len(nums):
        print(sum_ele)
        return 

    sum_ele+=nums[idx]

    sum_elements(nums,idx+1,sum_ele)

nums = [3,2,5,1,6]
sum_ele = 0
idx = 0
sum_elements(nums,idx,sum_ele)

    