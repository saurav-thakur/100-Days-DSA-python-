def natural_numbers_increasing(n):
    if n == 0:
        return
    
    natural_numbers_increasing(n-1)
    print(n)

def natural_numbers_decreasing(n):
    if n == 0:
        return
    
    print(n)
    natural_numbers_decreasing(n-1)

def natural_numbers_dec_inc(n):
    if n == 1:
        print(1)
        return
    
    print(n)
    natural_numbers_dec_inc(n-1)
    print(n)


natural_numbers_dec_inc(5)
    