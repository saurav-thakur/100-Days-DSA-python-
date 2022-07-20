def stairs(n):
    if n < 0:
        return 0

    if n == 0:
        return 1

    return stairs(n-1) + stairs(n-2)

print(stairs(3))