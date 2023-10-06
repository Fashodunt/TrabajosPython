import numpy as np
Max = 5
vector = np.zeros(Max, int)
def cargarList(x):
    for i in range(Max):
        x[i]=int(input("Ingrese un numero entero: "))
def mostrarMayorTen(y):
    for i in range(Max):
        if y[i] > 10:
            print(y[i])
def main():
    cargarList(vector)
    mostrarMayorTen(vector)

main()