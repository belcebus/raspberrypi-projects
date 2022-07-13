import my_libraries.numero_primo as np
import my_libraries.fibonacci as fib

""" Busca los numeros en un rango en los que coincidan que la tanto
    la sucesión de Fibonacci como el propio numero sean primos

"""


for n in range(2,10):
    fib_n = fib.fib(n)
    if np.is_primo(n) and np.is_primo(fib_n):
        print("fib({}): {}".format(n,fib_n))

print([ ("fib({})".format(n),fib.fib(n)) for n in range(2,10) if np.is_primo(n) and np.is_primo(fib.fib(n))])
