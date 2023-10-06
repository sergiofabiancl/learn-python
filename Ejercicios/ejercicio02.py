def cualquier_nombre(palabra):
    letras = palabra
    list(letras)
    letras_unicas = []
    for letra in letras:
        if letra not in letras_unicas:
            letras_unicas.append(letra)
    print(f"{letras_unicas}")
    letras_unicas.sort()
    print(f"{letras_unicas}")


cualquier_nombre("entretenido")