def suma(**kwargs):
    total = 0
    print(type(kwargs))
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total


print(suma(x=3, y=5, z=2))


def prueba(num1, num2, *args, **kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")

    for arg in args:
        print(f"arg = {arg}")

    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")


prueba(15,50,100,200,300,400,x='uno',y='dos',z='tres')


def lista_atributos(**kwargs):
    lista = []
    for clave,valor in kwargs.items():
        lista.append(clave)
    return lista

lista_atributos(x=1,y=2,z=3)