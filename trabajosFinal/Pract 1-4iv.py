import numpy as np
Max = 10
vector = np.zeros(Max , int)
def cargarList(x):
    for i in range(Max):
        x[i]=int(input("Ingrese un numero entero: "))

def sumaList(y):
    sum = 0
    for i in range(Max):
        sum = y[i]+sum
    print("La suma de todos los elementos de la lista es de: ",sum)

def numeroMayor(u):
    mayo = 0
    for i in range(Max):
        if u[i]>mayo:
            mayo = u[i]
    print("El numero mas grande de la lista es: ", mayo)

def numeroMenor(z):
    meno = 0
    for i in range(Max):
        if z[i]<0:
            meno = z[i]
    print("El numero mas chico de la lista es: ", meno)

def main():
    cargarList(vector)
    sumaList(vector)
    numeroMayor(vector)
    numeroMenor(vector)

main()