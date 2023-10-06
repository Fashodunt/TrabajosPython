dicc = [{'nombre':'Juan', 'edad':28},
        {'nombre':'Manuel', 'edad':36},
        {'nombre':'Ricardo', 'edad':31},
        {'nombre':'Fernando', 'edad':26},
        {'nombre':'Gregorio', 'edad':30},
        {'nombre':'Miguel', 'edad':56},
        {'nombre':'Julieta', 'edad':33}]

nomJoven = None
edadMinima = float('inf')  

def masJoven(nombre, edad):
        global nomJoven, edadMinima
        if edad < edadMinima:
                edadMinima = edad
                nomJoven = nombre

for persona in dicc:
        masJoven(persona['nombre'], persona['edad'])

if nomJoven:
        print("La persona más joven es:", nomJoven)
else:
        print("No se encontró ninguna persona en el diccionario.")
