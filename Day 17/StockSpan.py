def stock_span(nums):
    ans = []
    stack = []
    idx = []

    for i in range(len(nums)):

        if len(stack) == 0:
            ans.append(-1)

        elif len(stack) > 0 and stack[-1][0] > nums[i]:
            ans.append(stack[-1][1])
            
        elif len(stack) > 0 and stack[-1][0] <= nums[i]:
            while len(stack) > 0 and stack[-1][0] <= nums[i]:
                stack.pop()

            if len(stack) == 0:
                ans.append(-1)

            else:
                ans.append(stack[-1][1])

        stack.append((nums[i],i))
    
    for i in range(len(nums)):
        idx.append(i-ans[i])

    return idx



nums = [100 ,80 ,60, 70, 60 ,75 ,85]
print(stock_span(nums))
