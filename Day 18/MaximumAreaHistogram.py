def max_area_hist(nums):

    nsl = nearest_smaller_left_index(nums)
    nsr = nearest_smaller_right_index(nums)

    width = []
    for i in range(len(nums)):
        width.append(nsr[i]-nsl[i]-1)
    
    max_area = 0
    for i in range(len(nums)):
        area = width[i] * nums[i]
        max_area = max(area,max_area)
    return max_area


def nearest_smaller_left_index(nums):
    ans = []
    stack = []
    left_idx = -1

    for i in range(len(nums)):
        if len(stack) == 0:
            ans.append(left_idx)

        elif len(stack) > 0 and stack[-1][0] < nums[i]:
            ans.append(stack[-1][1])

        elif len(stack) > 0 and stack[-1][0] >= nums[i]:
            while len(stack) > 0 and stack[-1][0] >= nums[i]:
                stack.pop()
            
            if len(stack) == 0:
                ans.append(left_idx)

            else:
                ans.append(stack[-1][1])

        stack.append((nums[i],i))

    return ans

def nearest_smaller_right_index(nums):
    ans = []
    stack = []
    right_idx = 7

    for i in range(len(nums)-1,-1,-1):
        if len(stack) == 0:
            ans.append(right_idx)

        elif len(stack) > 0 and stack[-1][0] < nums[i]:
            ans.append(stack[-1][1])

        elif len(stack) > 0 and stack[-1][0] >= nums[i]:
            while len(stack) > 0 and stack[-1][0] >= nums[i]:
                stack.pop()
            
            if len(stack) == 0:
                ans.append(right_idx)

            else:
                ans.append(stack[-1][1])

        stack.append((nums[i],i))

    ans.reverse()

    return ans



nums = [6,2,5,4,5,1,6]
print(max_area_hist(nums))
