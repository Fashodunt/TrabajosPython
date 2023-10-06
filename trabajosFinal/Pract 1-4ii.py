
cantAptas = 0
cantPiezas=int(input("Ingrese la cantidad de piezas a procesar:  "))
if cantPiezas>0:
    for i in range(cantPiezas):
        onePiz = float(input("Ingrese la longitud de la pieza:  "))
        if (onePiz>=1.20) & (onePiz <= 1.30):
            cantAptas = cantAptas+1
    print("Las cantidas de piezas apatas que hay en el lote son: ",cantAptas)