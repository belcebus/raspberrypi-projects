
""" Imprime un binarios de 8 bits """
def print_binary_representation (number):
    print(f'{num_to_binary(number):0>8}')

""" Retorna una cadena binaria """
def num_to_binary(number):
    cadena_binaria = ""
    if number == 0:
        cadena_binaria = cadena_binaria + str(number%2)
    else:
        while number > 0:
            cadena_binaria = cadena_binaria + str(number%2)
            number = number // 2
    return cadena_binaria[::-1]