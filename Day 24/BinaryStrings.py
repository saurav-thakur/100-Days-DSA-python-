def binary_strings(s,n,idx,osf):
    if idx == n:
        print(f"{osf}")
        return

    binary_strings(s,n,idx+1,osf+"0")
    binary_strings(s,n,idx+1,osf+"1")
    

s = 4
n = s
binary_strings(s,n,0,"")