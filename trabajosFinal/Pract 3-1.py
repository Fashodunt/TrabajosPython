dicc = {"Miguel":"40","Manuel":"25","Gustavo":"30"}
list = ["Miguel","Martin","Ricardo","Gustavo"]
resultadoDicc = {}
rango = 0
def eliminarClaves(diccionario, listClave,x):
        aux = {}
        aux = diccionario
        [aux.pop(clave,None) for clave in listClave]
        rango2 = aux.keys()
        if x == len(rango2):
            print("No se elimino ninguna clave")
        else:
            print(aux)

rango = len(dicc)
resultadoDicc = eliminarClaves(dicc,list,rango)
