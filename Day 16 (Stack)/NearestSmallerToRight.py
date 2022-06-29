
# https://www.youtube.com/watch?v=nc1AYFyvOR4&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=6

def nearest_smaller_to_right(nums):

    ans = []
    stack = []

    for i in range(len(nums)-1,-1,-1):

        if len(stack) == 0:
            ans.append(-1)

        elif len(stack) > 0 and stack[-1] < nums[i]:
            ans.append(stack[-1])

        elif len(stack) > 0 and stack[-1] >= nums[i]:

            while len(stack) > 0 and stack[-1] >= nums[i]:
                stack.pop()
             
            if len(stack) == 0:
                ans.append(-1)

            else:
                ans.append(stack[-1])

        stack.append(nums[i])

    ans.reverse()
    return ans


nums = [4,5,2,10,8]
print(nearest_smaller_to_right(nums))
