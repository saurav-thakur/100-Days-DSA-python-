
# https://www.youtube.com/watch?v=T5s96ynzArg&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=3

def nearest_greater_to_left(nums):

    stack = []
    ans = []

    for i in range(len(nums)):

        if len(stack) == 0:
            ans.append(-1)

        elif len(stack) > 0 and stack[-1] > nums[i]:
            ans.append(stack[-1])

        elif len(stack) > 0 and stack[-1] <= nums[i]:
            
            while len(stack) > 0 and stack[-1] <= nums[i]:
                stack.pop()

            if len(stack) == 0:
                ans.append(-1)

            else:
                ans.append(stack[-1])

        stack.append(nums[i])

    return ans

nums = [1,3,2,4]
print(nearest_greater_to_left(nums))