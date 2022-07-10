def reverse_stack(nums):

    stack = []

    for i in nums:
        stack.append(i)

    for i in range(len(stack)):
        nums[i] = stack.pop()

    return nums


nums = [1,2,3,4,5]
print(reverse_stack(nums))
 