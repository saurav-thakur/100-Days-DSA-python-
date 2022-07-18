def check_sorted(nums,i):
    if i == len(nums):
        return True

    if nums[i-1] > nums[i]: 
        return False

    return check_sorted(nums,i+1)

nums = [1,2,3,4,5,6,7]
print(check_sorted(nums,1))

