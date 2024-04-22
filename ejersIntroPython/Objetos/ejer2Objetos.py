class Persona():
    def __init__(self,nombre="",edad=0,dni=""):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter 
    def nombre(self,nombre):
        self.__nombre = nombre
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter 
    def edad(self,edad):
        self.__edad = edad

    @property
    def dni(self):
        return self.__dni
    
    @dni.setter 
    def dni(self,dni):
        self.__dni = dni
        
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Dni: {self.dni}")
    
    def mayorDeEdad(self):
        return self.edad>=18

class Cuenta(): 
    def __init__(self, titular,cantidad=0):
        self.titular=titular
        self.__cantidad=cantidad
    
    @property    
    def titular(self):
        return self.__titular
    
    @titular.setter
    def titular(self,titular):
        if isinstance(titular,Persona):
            self.__titular=titular
    
    @property
    def cantidad(self):
        return self.__cantidad
    @cantidad.setter
    def cantidad(self,cantidad):
        self.__cantidad,cantidad
    
    def ingresar(self,cantidad):
        if(cantidad>0):
            self.__cantidad+=cantidad
    def retirar(self,cantidad):
        if(cantidad>0):
            self.__cantidad-=cantidad
            
    def mostrar(self):
        print("Datos de la cuenta: ")
        print(f"Titular cuenta:")
        self.titular.mostrar()
        print(f"Cantidad en la cuenta : {self.cantidad}")

persona1 = Persona("Nando", 45, "12345678")
cuenta1 = Cuenta(persona1,1000)
cuenta1.ingresar(330)

cuenta1.mostrar()
