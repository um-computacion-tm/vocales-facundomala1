def contador_vocales(texto):
    vocales = ("a", "e", "i", "o", "u")
    resultado = {}
    texto = texto.lower()
    for letra in texto:
        if letra in vocales:
            if letra not in resultado:
                resultado[letra] = 1
            else:
                resultado[letra] += 1
    return resultado