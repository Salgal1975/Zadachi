def fibo(n):
    a = 0
    b = 1
    print(a, b, end=' ')
    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
        print(c, end=' ')

n = 10
fibo(n) # 0 1 1 2 3 5 8 13 21 34 55