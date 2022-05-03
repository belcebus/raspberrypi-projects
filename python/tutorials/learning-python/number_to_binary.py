
from my_libraries import binary_operations as bo

if __name__ == "__main__":

    for number in range(0,100):
        bo.print_binary_representation(number)
    for number in range(0,10):
        print(bo.num_to_binary(number))