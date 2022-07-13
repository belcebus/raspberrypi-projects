from math import sqrt

def is_primo(number):
    if number <= 0:
        raise ValueError("{} must be integer greater than 0".format(number))
    else:
        for n in range(2, int(sqrt(number))+1):
            if number % n == 0:
                return False
        return True
                
def get_primos(fin):
    primos = []
    for n in range(1,fin):
        if is_primo(n):
            primos.append(n)
    return primos
