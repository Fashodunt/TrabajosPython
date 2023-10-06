import numpy as np
class Pelicula:
    def __init__(self,titulo,duracion,categoria,premiada,anio) :
        self.__titulo=titulo
        self.__duracion=duracion
        self.__categoria=categoria
        self.__premiada=premiada
        self.__anio=anio
    def __str__(self) :
        return f"Titulo: {self.__titulo} Duracion: {self.__duracion} Categoria: {self.__categoria} Premiada: {self.__premiada} Año: {self.__anio}"

    def getTitulo(self) :
        return self.__titulo
    def getCategoria (self):
        return self.__categoria
    def getPremiadas (self):
        return self.__premiada
    def getAnio (self):
        return self.__anio

class Catalogo:
    def __init__(self, peliculas, capacidad):
        self.__capacidad = 20
        self.__peliculas = np.zeros(self.__capacidad, Pelicula)
        self.__contador = 0
        
    def agregarPelicula(self, pelicula):
        self.__peliculas[self.__contador] = pelicula
        self.__contador = self.__contador + 1
    
    def estaVacio(self):
        return self.__contador>0

    def estaLleno(self):
        return self.__contador<self.__capacidad
    
    def listarPorCategoria(self,cat):
        for i in range(self.__contador):
            if self.__peliculas[i].getCategoria()== cat :
                print (self.__peliculas[i])
    

    def listarPremiadasPorAnio(self,anio):
        for i in range(self.__contador) :
            if self.__peliculas[i].getPremiadas()==True :
                if self.__peliculas[i].getAnio()==anio :
                    print(self.__peliculas[i])
    
    def listarDatosPelicula(self,titulo):
        for i in range(self.__contador):
            if self.__peliculas[i].getTitulo() == titulo :
                print(self.__peliculas[i])
    
def main():
    miCatalogo=Catalogo()
    while (True):
        print("1: Agregar Pelicula")
        print("2: Mostrar Por Titulo")
        print("3: Mostrar por Categoria")
        print("4: Mostrar Premiadas Por Año")
        op = int(input("Ingrese una opción:"))
        if op == 1:
            if not miCatalogo.estaLleno():
                titulo=input("Ingrese Titulo de la Pelicula")
                duracion=input("Ingrese duracion en minutos")
                categoria=input("Ingrese la categoria, terror, policial, drama, comedia.")
                while(True):
                    premiada = input("La pelicula fue premiada S|N")
                    premiada=premiada.lower()
                    if premiada == 's' :
                        premiada = True
                        break
                    if premiada == 'n':
                        premiada=False
                        break
                anio = input("Ingrese el año de la pelicula")
                miCatalogo.agregarPelicula(Pelicula(titulo,duracion,categoria,premiada,anio))
            else:
                print("ups, el catalogo esta lleno")
        elif op == 2:
            if not miCatalogo.estaVacio():
                titulo = input("Ingrese Titulo de la Pelicula")
                miCatalogo.listarDatosPelicula(titulo)
            else:
                print("No hay peliculas cargadas en el catalogo")
        elif op == 3:
            if not miCatalogo.estaVacio():
                categoria = input("Ingrese la Categoria para listar")
                miCatalogo.listarPorCategoria(categoria)
            else:
                print("No hay peliculas cargadas en el catalogo")
        elif op == 4:
            if not miCatalogo.estaVacio():
                anio = input("Ingrese Año para listar las peliculas premiadas")
                miCatalogo.listarPremiadasPorAnio(anio)
            else:
                print("No hay peliculas cargadas en el catalogo")
        else:
            print("Parece no ser una opcion ")
            cont = input("Desea continuar? S|N:")
            if (cont == 's' or cont == 'S'):
                continue
            else:
                break
        print("Hasta Luego")

main()