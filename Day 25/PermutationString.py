
def permutation(s,osf):
    if len(s) == 0:
        print(osf)
        return

    for i in range(len(s)):
        curr = s[i]

        permutation(s[0:i]+s[i+1:],osf+curr)

s = "ABC"
osf = ""
permutation(s,osf)