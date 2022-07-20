def reverse_string(string,left,right):
    if left >= right:
        return

    string[left],string[right] = string[right],string[left]

    reverse_string(string,left+1,right-1)


def rev(string,idx,ans):
    if idx == len(string):
        return
    
    rev(string,idx+1,ans)
    ans.append(string[idx])


string = ["a","b","c","e","d"]
left = 0
right = len(string) - 1
reverse_string(string,left,right)
print(string)
# idx = 0
# ans = []
# rev(string,idx,ans)
# print(ans)