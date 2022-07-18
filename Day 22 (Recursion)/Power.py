def power(a,b):
    if  a == 0 and b == 0:
        return "undefined"
    if b == 0:
        return 1

    if a == 0:
        return 0

    return a*power(a,b-1)

def power1(a,b):
    if b == 0:
        return 1

    if a == 0:
        return 0
    temp = power1(a,b//2)

    if b % 2 == 0:
        return b * temp

    else:
        return a * temp * temp


print(power1(2,4))