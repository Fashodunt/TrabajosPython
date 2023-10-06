tupli = ()
def splito(x):
    cad1 = x.split("@")
    cad2 = cad1[1].split(".")
    cad3 = cad1 + cad2
    cad3.pop(1)
    return(cad3)

def ingreso ():
    y = str(input("Ingrese el mail: "))
    return (y)

def main ():
    cant = int(input("Cuantos mails queres ingresar, solo divertite: "))
    for i in range(cant):
        mail = ingreso()
        tupli = (tuple (splito(mail)))
        print(tupli)

main()