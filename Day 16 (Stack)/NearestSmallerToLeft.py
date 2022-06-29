
# Nearest Smaller Element
# https://www.youtube.com/watch?v=85LWui3FlVk&list=PL_z_8CaSLPWdeOezg68SKkeLN4-T_jNHd&index=4

def nearest_smaller_to_left(nums):

    ans = []
    stack = []

    for i in range(len(nums)):

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

    return ans

nums = [4,5,2,10,8]
print(nearest_smaller_to_left(nums))