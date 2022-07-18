def lexicographical_order(n,i):
    if i > n:
        return

    print(i)
    if i == 0:
        for j in range(1,10):
            lexicographical_order(n,10*i+j)

    else:
        for j in range(10):
            lexicographical_order(n,10*i+j)

        


lexicographical_order(13,0)