def pattern1(n,count):
    if n == 1:
        print("*")
        return

    if count < n:
        print("*",end=" ")
        pattern1(n,count+1)
    else:
        print()
        pattern1(n-1,0)

def pattern2(n,count):
    if n == 0:
        
        return

    if count < n:
        pattern2(n,count+1)
        print("*",end=" ")
    else:
        pattern2(n-1,0) 
        print()
 

    

pattern2(5,0)