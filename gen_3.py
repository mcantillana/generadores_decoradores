def multiplos_de(n):
    index = 1
    while True:
        yield index*n
        index = index + 1


if __name__ == '__main__':

    # un bucle
    for multiplo in multiplos_de(3):
        print(multiplo)

        # cortamos el bucle para ejemplificar
        if multiplo >= 30:
            break
