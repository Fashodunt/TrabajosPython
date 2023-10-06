
def borrarPuntosComas(x):
    x.discard('.')
    x.discard(',')
    x.discard('¡')
    x.discard('!')
    x.discard(':')
    x.discard('"')
    x.discard(' ')

def pangrama(texto):
    texList = list(texto)
    setTex = set(texList)    
    borrarPuntosComas(setTex)
    print(setTex)
    print(len(setTex))
    if len(setTex) >= 27:
        print("Tu texto es un pangrama")
    else:
        print("Tu texto no es un pangrama")

def main():
    cant = int(input("Cuantos textos queres ingresar: "))
    for i in range(cant):
        text = str(input("Ingrese el texto: "))
        pangrama(text)

main()


