import my_libraries.numero_primo as np

if __name__ == "__main__":
    for n in range(1, 100):
        if np.is_primo(n):
            print(n)
    print(np.get_primos(1000))