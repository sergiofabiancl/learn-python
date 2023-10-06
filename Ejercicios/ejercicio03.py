def busca_ceros(*args):
    previo = False
    for arg in args:
        if arg == 0:
            if previo:
                return True
            else:
                previo = True
        else:
            previo = False

    return False

print(busca_ceros(6,0,5,1,0,3,0,1))