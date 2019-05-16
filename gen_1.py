def gen_basico():
    yield "uno"   
    yield "dos"
    yield "tres"


if __name__ == '__main__':
    
    # un bucle
    for g in gen_basico():
        print(g)

    # convertir la generacion en una lista
    print(list(g))
