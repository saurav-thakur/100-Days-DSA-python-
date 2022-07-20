def is_palindrome(nums,left,right):
    if left >= right:
        return True
    
    if nums[left] != nums[right]:
        return False

    return is_palindrome(nums,left+1,right-1)


nums = ["a","b","c","b","a"]
nums = ["a","b","c","d","c","b","a"]
left = 0
right = len(nums)-1
print(is_palindrome(nums,left,right))
