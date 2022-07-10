def reverse_stack(nums):

    if len(nums) == 0:
        return
    lastElement = nums.pop()
    reverse_stack(nums)

    reverse_recursively(nums,lastElement)

    return nums

def reverse_recursively(nums,lastElement):

    if len(nums) == 0:
        nums.append(lastElement)
        return

    poped_element = nums.pop()
    reverse_recursively(nums,lastElement)
    
    nums.append(poped_element)

    return nums
nums = [1,2,3,4,5]
print(reverse_stack(nums))