def linear_search(nums,idx,key):
    if idx == len(nums):
        return False

    if nums[idx] == key:
        return True

    return linear_search(nums,idx+1,key)


nums = [3,5,6,7,9,1,4,90,34]
key = 34
idx = 0
print(linear_search(nums,idx,key))