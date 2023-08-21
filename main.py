from random import *

contador = 8
exito = False

# Preguntar nombre al usuario
nombre = input('Indica tu nombre: ')
print(f'Hola {nombre}, un gusto saludarte')

while exito == False:
    # Generar un numero entre 1 y 100
    print("Voy a generar un numero secreto entre 1 y 100")
    print("Tienes 8 intentos para adivinarlo")
    secreto = randint(1,100)
    #print(f'El numero es {secreto}')

# Responder si esta fuera de rango, si es mayor, si es menor o si tuvo exito
    while contador > 0 and exito == False:
        respuesta = int(input('Ingresa una respuesta '))
        if respuesta < 1:
            print('Ups! Tu respuesta esta fuera de rango')
            contador = contador - 1
            print(f'Te quedan {contador} intentos')
        elif respuesta > 100:
            print('Ups! Tu respuesta esta fuera de rango')
            contador = contador - 1
            print(f'Te quedan {contador} intentos')
        else:
            if respuesta > secreto:
                print(f'Error! el numero secreto es menor que {respuesta}')
                contador = contador - 1
                print(f'Te quedan {contador} intentos')
            elif respuesta < secreto:
                print(f'Error! el numero secreto es mayor que {respuesta}')
                contador = contador - 1
                print(f'Te quedan {contador} intentos')
            elif respuesta == secreto:
                print(f'Adivinaste!, el numero secreto era {respuesta}')
                exito = True
    if contador == 0:
        print('Lamentablemente se acabaron los intentos, mas suerte en la siguiente!')
        contador = 8
if exito:
    print(f'Felicitaciones {nombre}!')





# Cuando acierta debe indicar la cantidad de intentos o iniciar nuevamente


