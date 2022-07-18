# There are n cells arranged in linear fashion
# You are standing at 0th cell and want to reach n-1 cell
# How many ways to reach n-1 th cell.
# dice has 1 to 6th cell

def dice_path(n,idx,osf):
    if idx >=n:
        return

    if idx == n-1:
        print(f"{osf}",end=" ")
        print("reached")
        return
    for j in range(1,n):
        dice_path(n,idx+j,osf+str(j)+"->")


n = 6
idx = 0
osf = ""
dice_path(n,idx,osf)