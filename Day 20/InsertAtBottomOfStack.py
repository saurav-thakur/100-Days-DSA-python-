def insert_at_bottom(nums,element):

    insert_recursively(nums,element)

    return nums

def insert_recursively(nums,element):

    if len(nums) == 0:
        nums.append(element)
        return
    
    poped_num = nums.pop()

    insert_recursively(nums,element)

    nums.append(poped_num)
    return nums

nums = [7,4,1,5,321,3,12,3]
element = 102
print(insert_at_bottom(nums,element))