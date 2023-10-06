import numpy as np
# implementar la clase Auto
# asumiremos que la hora es un entero exacto 1, 2, 8, etc.
class Auto:
    def __init__(self,patente,horaIngreso):
        self.__patente=patente
        self.__horaIngreso = horaIngreso
        self.__horaEgreso = 0

    def __str__(self):
        return f"Patente: {self.__patente} Hora ingreso: {self.__horaIngreso}\n"

    def getPatente(self):
        return self.__patente
    def getIngreso(self):
        return self.__horaIngreso
    def getEgreso(self):
        return self.__horaEgreso
    
    def setEgreso(self,egre):
        self.__horaEgreso = egre
    def setPatente(self,panti):
        self.__patente = panti
    

class Sector:
    def __init__(self, denominacion,capacidad, valorHora):
        self.__denominacion=denominacion
        self.__capacidad = capacidad
        self.__valorHora = valorHora
        self.__autos = np.zeros(self.__capacidad, Auto)
        #indice que nos permite saber cuantos autos hay actualmente 
        #en el estacionamiento
        self.__actual=0
        #atributo que nos permite tener la recaudacion diaria
        #se usuara en el metodo egresarAuto
        self.__recaudacionDia=0

    #lista los datos de los autos estacionados
    def __str__(self):
        ret = ""
        for i in range(self.__actual):
            if self.__autos[i] != 0:
                ret += str(self.__autos[i])
        return ret
    #implementar los metodos get/set
    def getDenominacion(self):
        return self.__denominacion
    def getCapacidad(self):
        return self.__capacidad
    def getValor(self):
        return self.__valorHora
    def getActual(self):
        return self.__actual
    def getRecaudacion(self):
        return self.__recaudacionDia
    def setActual(self,act):
        self.__actual = self.__actual-act
    
    
    #El metodo hayLugar verifica si hay disponiblidad
    #para ingresar un auto en el sector, esto sera cuando la posicion es igual a 0
    def hayLugar(self):
        for i in range(self.__capacidad):
           if self.__autos[i]==0:
               return True
        return False
    #El metodo lugarLibre nos retorna la primera posicion 
    #libre, que usaremos para agregar un Auto en el sector.
    #se usa si previamente se consulto si hayLuagar disponible
    def __lugarLibre(self):
        for i in range(self.__capacidad):
            if self.__autos[i] == 0:
                return i
     #ingresa auto si hayLugar en el primer lugarLibre que encuentra           
    def ingresarAuto(self, auto):
        self.__autos[self.__lugarLibre()] = auto
        self.__actual+=1
    
    def buscarAuto(self, patente):
        for i in range(self.__capacidad):
            if self.__autos[i] != 0:
                if self.__autos[i].getPatente() == patente:
                    return True
        return False
    #implementar el metodo darPosicion, recibe la patente
    #realiza la busqueda y devuelve el indice. Para poder 
    #usar este metodo previamente debemos saber si el Auto
    #se encuentra en el sector, para ellos usamos el metodo buscarAuto()
    def darPosicion(self, patente):
        for i in range(self.__capacidad):
            if self.__autos[i] != 0:
                if self.__autos[i].getPatente() == patente:
                    return i

    #implementar el metodo egresarAuto
    #debemos cambiar la hora de salida al egresar un auto
    #calcular el costo, con el metodo calcularPlata 
    #liberar el espacio, utilizar 0 para indicar que el lugar quedo libre
    #acumular lo que devuelve calcularPlata en el atributo recaudacionDia
    def egresarAuto(self, patente, horaSalida):
        var = 0
        if self.buscarAuto(patente):
            i = self.darPosicion(patente)
            self.__autos[i].setEgreso(horaSalida)
            recaudacionAuto = ((self.__autos[i].getEgreso() - self.__autos[i].getIngreso()) * self.getValor())
            self.__recaudacionDia = self.__recaudacionDia + recaudacionAuto
            self.__autos[i].setPatente(var)
            self.setActual(1)
            
    

    #metodo que recorre todo el sector calculando lo recaudado
    #def calcularPlata(self):

class Estacionamiento:
  def __init__(self, nombre,docente, alumno, general):
    self.__nombre=nombre
    self.__sectorDocente = docente
    self.__sectorAlumno = alumno
    self.__sectorGeneral = general

  #terminar de implementar el metodo STR
  def __str__(self):
    return f"{self.__autos}"

  def getNombre(self):
    return self.__nombre

  def ingresarAuto(self, sector, auto):
    
    if sector == "Docente":
      self.__sectorDocente.ingresarAuto(auto)
    elif sector == "Alumno":
      self.__sectorAlumno.ingresarAuto(auto)
    else:
      self.__sectorGeneral.ingresarAuto(auto)

  def egresarAuto(self, sector, patente, horaSalida):
    if sector == "Docente":
      self.__sectorDocente.egresarAuto(patente,horaSalida)
    elif sector == "Alumno":
      self.__sectorAlumno.egresarAuto(patente,horaSalida)
    else:
      self.__sectorGeneral.egresarAuto(patente,horaSalida)
  
  def buscarAuto(self, patente):

    if self.__sectorDocente.buscarAuto(patente):
      return True
    if self.__sectorAlumno.buscarAuto(patente):
      return True
    if self.__sectorGeneral.buscarAuto(patente):
      return True

    return False

  def hayLugar(self, sector):
    if sector == "Docente":
      return self.__sectorDocente.hayLugar()
    elif sector == "Alumno":
      return self.__sectorAlumno.hayLugar()
    else:
      return self.__sectorGeneral.hayLugar()


  def calcularPlata(self):
    ret = 0
    ret += self.__sectorDocente.getRecaudacion()
    ret += self.__sectorAlumno.getRecaudacion()
    ret += self.__sectorGeneral.getRecaudacion()
    return ret

    
  def listarPorSector(self):

    if (self.__sectorAlumno.getActual() != 0):
      print("Autos en el Sector Alumno")
      print(self.__sectorAlumno)
    else:
      print("En el Sector Alumno no hay Autos")

    if (self.__sectorDocente.getActual() != 0):
      print("Autos en el Sector Docente")
      print(self.__sectorDocente)
    else:
      print("En el Sector Docente no hay Autos")

    if (self.__sectorGeneral.getActual() != 0):
      print("Autos en el Sector General")
      print(self.__sectorGeneral)
    else:
      print("En el Sector General no hay Autos")

# La prueba se debe realizar sobre la siguiente funcion main que no puede modificarse.

def main():
  secDocente=Sector('Docente',50,10)
  secAlumno=Sector('Alumno',50,5)
  secGeneral=Sector('General',100,20)
  unahur = Estacionamiento('unahur',secDocente,secAlumno,secGeneral)
  unahur.ingresarAuto('Docente',Auto('AAA123',10))
  unahur.ingresarAuto('Alumno', Auto('ABB123',1))
  unahur.ingresarAuto('General',Auto('ABC321',23))
  unahur.listarPorSector()
  unahur.ingresarAuto('Docente', Auto('ZZZ123', 8))
  unahur.ingresarAuto('Alumno', Auto('XXX123', 4))
  if unahur.hayLugar('General'):
    unahur.ingresarAuto('General', Auto('YYY321', 2))
  unahur.ingresarAuto('Docente', Auto('JJJ123', 5))
  unahur.ingresarAuto('Alumno', Auto('HHH123', 6))
  unahur.ingresarAuto('General', Auto('FFF321', 23))
  #deberia solo mandar la pantente si lo encuentra recien lo egresa
  if unahur.buscarAuto('YYY321'):
    unahur.egresarAuto('General','YYY321',13)
  if unahur.buscarAuto('KKK345'):
    unahur.egresarAuto('Docente','KKK345',2)
  else:
    print(f"El auto no se encuentra en el estacionamiento")
  unahur.egresarAuto('Docente', 'JJJ123', 21)
  unahur.egresarAuto('Alumno', 'HHH123', 8)
  unahur.egresarAuto('General', 'FFF321', 24)
  print(f"Total recaudado {unahur.calcularPlata()}")


main()