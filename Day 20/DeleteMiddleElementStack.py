def delete_middle(nums):
    n = len(nums) - 1
    count = 0
    delete_recursive(nums,count,n)
    return nums

def delete_recursive(nums,count,n):
    if count == n//2:
        nums.pop()
        return

    num = nums.pop()
    delete_recursive(nums,count+1,n)

    nums.append(num)
    return nums


nums = [1,2,3,4,5,6,7,8]
print(delete_middle(nums))
    

