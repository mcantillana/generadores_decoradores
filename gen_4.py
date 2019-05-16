import random

def generador_ips(cantidad):
    for i in range(cantidad):
        a = random.randint(0,255)
        b = random.randint(0,255)
        c = random.randint(0,255)
        d = random.randint(0,255)
        
        yield '{0}.{1}.{2}.{3}' . format(a,b,c,d)


if __name__ == '__main__':
    
    # generar 5 ips
    ips =  generador_ips(5)
    print(list(ips))


