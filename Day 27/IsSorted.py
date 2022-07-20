def is_sorted(nums,idx):
    if idx == len(nums):
        return True

    if nums[idx-1] > nums[idx]:
        return False

    return is_sorted(nums,idx+1)

nums = [1,2,3,8,4,5,7]
print(is_sorted(nums,1))
