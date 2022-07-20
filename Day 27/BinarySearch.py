def binary_search(nums,target,start,end):

    if start > end:
        return False

    mid = (start+end) // 2

    if nums[mid] == target:
        return True

    elif target > nums[mid]:
        return binary_search(nums,target,mid+1,end)

    else:
        return binary_search(nums,target,start,mid-1)

nums = [2,4,6,7,9,10,20,25]
target = 20
print(binary_search(nums,target,0,len(nums)))