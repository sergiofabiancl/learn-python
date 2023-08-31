from random import shuffle


def lanzar_dados():
    valores = [1, 2, 3, 4, 5, 6]
    shuffle(valores)
    valor1 = valores[1]
    valor2 = valores[2]

    return valor1, valor2


def evaluar_jugada(valor01, valor02):
    suma_dados = valor01 + valor02
    if suma_dados <= 6:
        mensaje = "La suma de tus dados es " + str(suma_dados) + ". Lamentable"
    elif 6 < suma_dados < 10:
        mensaje = "La suma de tus dados es " + str(suma_dados) + ". Tienes buenas chances"
    else:
        mensaje = "La suma de tus dados es " + str(suma_dados) + ". Parece una jugada ganadora"
    return mensaje


lista_numeros = [1, 2, 15, 7, 2]


def reducir_lista(lista):
    lista2 = []
    maximo = max(lista_numeros)
    for n in lista:
        if n != maximo:
            if n in lista2:
                pass
            else:
                lista2.append(n)
        else:
            pass

    return lista2


def promedio(lista):
    contador = 0
    resultado = 0
    for n in lista:
        resultado = resultado + n
        contador = contador + 1
    resultado = resultado / contador

    return resultado
