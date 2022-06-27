def longestCommonPrefix(strs):
    
    if len(strs) == 0:
        return ""

    if len(strs) == 1:
        return strs[0]

    initial = strs[0]
    ans = []
    
    for i in range(1,len(strs)):
        a = 0
        b = 0
        ans = []
        while a < len(initial) and b < len(strs[i]):
            if initial[a] == strs[i][b]:
                ans.append(strs[i][b])
                a+=1
                b+=1
            else:
                break

        initial = ans
        
    if len(ans) == 0:
        return ""

    return "".join(ans)

strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))