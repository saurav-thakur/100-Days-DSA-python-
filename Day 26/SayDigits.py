
def say_digits(num,mapNum):
    if num == 0:
        return
    digit = num % 10
    
    say_digits(num//10,mapNum)
    print(mapNum[digit],end=" ")
    


num = 413
mapNum = ["Zero","One","Two","Three","Four","Five","Six","Seven","Eight","Nine"]
say_digits(num,mapNum)