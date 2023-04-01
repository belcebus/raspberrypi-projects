# decorator

from functools import wraps


def gate(umbral):
    print("Umbral establecido a ", umbral)

    def measure(func):
        @wraps(func)
        def wrapper(*arg, **kwargs):
            resultado = func(*arg, **kwargs)
            if resultado > umbral:
                print("Resultado superior a ", umbral)
            return resultado

        return wrapper

    return measure


@gate(1)
def cubo(n):
    """Retorna el cubo del parámetro n"""
    return n ** 3


print(cubo(2))
print(cubo.__doc__)
