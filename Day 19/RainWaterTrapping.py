

def rain_water_trapping(nums):
    mxl = []
    mxr = []
    final_ans = 0

    maxNum0 = nums[0]
    maxNum1 = nums[len(nums)-1]

    for i in range(len(nums)):
        maxNum0 = max(maxNum0,nums[i])
        mxr.append(maxNum0)

    for i in range(len(nums)-1,-1,-1):
        maxNum1 = max(maxNum1,nums[i])
        mxl.append(maxNum1)

    
    for i in range(len(nums)):
        final_ans += min(mxl[i],mxr[i])-nums[i]


    return final_ans

nums = [3, 0, 0, 2, 0, 4]
print(rain_water_trapping(nums))
        



    

