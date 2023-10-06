
def devolver_distintos(num1,num2,num3):
    numero = 0
    suma = num1+num2+num3
    lista = [num1,num2,num3]
    if suma > 15:
        numero = max(lista)
    elif suma < 10:
        numero = min(lista)
    else:
        for n in lista:
            if (n != max(lista)) and (n != min(lista)):
                numero = n
    print(f"{numero}")
    return numero

devolver_distintos(3,4,5)
