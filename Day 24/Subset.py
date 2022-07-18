
def subset(arr,i,n,osf):
    if i == n:
        print(f"[{osf}]")
        return

    subset(arr,i+1,n,osf+arr[i])
    subset(arr,i+1,n,osf)

arr = "123"
subset(arr,0,len(arr),"")

