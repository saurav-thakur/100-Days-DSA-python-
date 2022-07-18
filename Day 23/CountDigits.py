# ans = 0
# def countDigits(n):
#     global ans
#     if n == 0:
#         return 
#     ans += 1
#     countDigits(n//10)
#     return ans

# print(countDigits(99))


def count_digits(num):
    if num == 0:
        return 0

    return 1 + count_digits(num//10)

num = 245323
print(count_digits(num))