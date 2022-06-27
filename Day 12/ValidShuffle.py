def valid_shuffle(s1,s2,res):
    if len(s1) + len(s2) != len(res):
        return False

    i = 0
    j = 0
    k = 0

    while k < len(res):

        if i < len(s1) and s1[i] == res[k]:
            i+=1
        elif j < len(s2) and s2[j] == res[k]:
            j+=1

        k+=1

    if i < len(s1) or j < len(s2):
        return False
    return True


s1 = "xy"
s2 = "12"
res = "x1y2"

print(valid_shuffle(s1,s2,res))