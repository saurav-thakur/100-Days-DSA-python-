import sys
sys.setrecursionlimit(1000000)

def factorial(N):
    if N == 0:
        return 1

    return N*factorial(N-1)

def digitsInFactorial(N):
    # code here
    
    fact = factorial(N)
    count = 0
    while fact != 0:
        fact = fact // 10
        count += 1
    return count
        

N = 12
print(digitsInFactorial(N))