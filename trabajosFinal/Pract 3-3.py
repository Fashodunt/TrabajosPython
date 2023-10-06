def contar_letras(lista_palabras):
    diccionario_resultado = {}
    for palabra in lista_palabras:
        for letra in palabra:
            if letra.isalpha():  # Ignorar caracteres no alfabéticos
                letra = letra.lower()  # Convertir a minúsculas para evitar diferencias entre mayúsculas y minúsculas
                if letra in diccionario_resultado:
                    diccionario_resultado[letra] += 1
                else:
                    diccionario_resultado[letra] = 1
    return diccionario_resultado

# Ejemplo de uso:
lista1 = ["hola", "mundo", "python"]
lista2 = ["Esto", "me hizo", "renegar"]

resultado1 = contar_letras(lista1)
resultado2 = contar_letras(lista2)

print("Resultado 1:", resultado1)
print("Resultado 2:", resultado2)