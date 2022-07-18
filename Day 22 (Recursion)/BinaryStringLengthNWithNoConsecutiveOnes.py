def binary_strings(n):
    if n == 1:
        return 2
    if n == 2:
        return 3

    return binary_strings(n-1) + binary_strings(n-2)

n = 4
print(binary_strings(n))