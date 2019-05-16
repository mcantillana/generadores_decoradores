def mi_decorador(funcion):
    def nueva(*args):
        print("Llamada a la funcion", funcion.__name__)
        retorno = funcion(*args)
        return retorno
    return nueva 

@mi_decorador
def mi_fn():
    print(" Hola Mundo ")


if __name__ == '__main__':
    mi_fn()