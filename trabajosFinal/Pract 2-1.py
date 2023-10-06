x = []
y = []
z = []

def cargarSets (a):
    cantNum = int(input("Ingrese la cantidad de elementos que vas a ingresar(NUMEROS ENTEROS): "))
    for i in range(cantNum):
        b = int(input("Ingrese un numero: "))
        a.append(b)
        

def main():
    cargarSets(x)
    cargarSets(y)
    cargarSets(z)
    a = set(x)
    b = set(y)
    c = set(z)

    elemComunes = a &  b & c
    elemDistintos = a ^ b ^ c
    print("Estos son los elementos comunes de las listas: ",elemComunes)
    print("Estos son los elementos distintos de las listas: ",elemDistintos)

main()