def findDuplicate(s):

    d = {}
    ans = []
    for i in range(len(s)):

        if s[i] == " ":
            continue
        elif s[i] not in d:
            d[s[i]] = 1

        else:
            d[s[i]] += 1
    for key,val in d.items():
        if val > 1:
            ans.append((key,val))

    return ans

s = "test string"
print(findDuplicate(s))