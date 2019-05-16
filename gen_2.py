def pares():
    index = 1
    # En este caso definimos un bucle infinito
    while True:
        # Devolvemos un valor
        yield index*2
        index = index + 1


if __name__ == '__main__':
    
    # un bucle
    for par in pares():
        print(par)

        # cortamos el bucle para ejemplificar
        if par >= 50:
            break


