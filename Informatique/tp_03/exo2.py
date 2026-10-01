def syracus(n):
    print(n)
    while n != 1:
        r = n%2
        if r == 0:
            n = n / 2
            print(n)
        else:
            n = (n*3)+1
            print(n)
    return n
print(syracus(1243))