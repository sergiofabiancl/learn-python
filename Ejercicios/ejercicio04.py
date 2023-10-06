def contar_primos(numero):
    primos = []
    for i in range(2, numero):
        for n in range(2, i):
            if i % n == 0:
                continue
                #no es primo
            else:
                #es primo
                primos.append(i)
                continue
    print(f"{primos}")



contar_primos(74)