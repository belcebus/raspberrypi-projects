def fib(n: int):
    """ 
        Fibonacci:
        f(0)=0
        f(1)=1
        f(n)=f(n-1)+f(n-2)
    """

    fib_n_1 = 1
    fib_n_2 = 0
    fib_n = 1

    if n <= 0:
        return 0
    elif n == 1:
        return 1

    for n in range(2,n):
        fib_n = fib_n_1 + fib_n_2
        fib_n_2=fib_n_1
        fib_n_1=fib_n
    return fib_n
    