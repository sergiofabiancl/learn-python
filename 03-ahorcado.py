import random
import time


palabra_seleccionada = {}
guiones = {}


def definir_palabra(lista_palabras):
  palabra = random.choice(lista_palabras)
  largo = len(palabra)
  x = 1
  for letra in palabra:
    palabra_seleccionada[x] = letra.upper()
    guiones[x] = "_"
    x = x + 1
  return largo


def validar_letra(letra_preguntada):
  for posicion,letra in palabra_seleccionada.items():
    if letra_preguntada == letra:
      guiones[posicion] = letra


def solicitar_letra():
  while True:
    letra = input("Ingresa una letra: ")
    if letra.isalpha():
      if len(letra) > 1:
        print("Ingresaste mas de una letra")
      else:
        letra = letra.upper()
        return letra
    else:
      print("Ingresaste numeros")


def validar_avance():
  completa = traducir_dic(palabra_seleccionada)
  incognita = traducir_dic(guiones)
  if completa == incognita:
    print(f"Palabra -> {incognita}")
    return False
  else:
    print(f"Palabra -> {incognita}")
    return True


def traducir_dic(diccionario):
  lista_letras = list(diccionario.values())
  palabra_como_palabra = ''.join(lista_letras)
  return palabra_como_palabra


def main(*args):
  print("Bienvenido al juego del ahorcado")
  largo = definir_palabra(args)
  print(f"Tu palabra contiene {largo} letras")
  while validar_avance():
    letra = solicitar_letra()
    validar_letra(letra)
  print(f"Felicidades!")
  print(f"La palabra era {traducir_dic(guiones)}")






main("comprar","vender","arrendar","suprimir","conejo","auto","egipto","jordania","israel","argentina","brasil","chile","canada","peru")