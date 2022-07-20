def bubble_sort(nums,idx):

    if idx == len(nums):
        return
    print(nums)
    for j in range(idx+1,len(nums)):
        if nums[j] < nums[idx]:
            nums[j],nums[idx] = nums[idx],nums[j]
    bubble_sort(nums,idx+1)

nums = [10,4,2,3,6,5,1,9,7,8,15,23,15,16]
bubble_sort(nums,0)
print(nums)