#Ingresar ventas hasta ingresar un -1, calcular el total de las ventas realizadas, cuando finaliza, mostrar el total.
#PROGRAMA PRINCIPAL
"""
totalVentas=0
monto=0
while monto>=0:
    monto=int(input("Ingrese el monto de una ventan(-1 para finalizar):  "))
    if (monto >= 0):
        totalVentas = totalVentas + monto
    elif (monto == -1):
        print("El total de ventas es: ", totalVentas)
    else:
        print("Error, ingreso un valor negativo")
        print("El total de ventas es: ", totalVentas)
"""

totalVentas = 0
monto = 0
for i in 