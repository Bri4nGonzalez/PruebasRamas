class Usuario:
    __edad = 0
    def __init__(self,nombre):
       self._nombre = nombre 

    def saludar(self, saludo):
        print(saludo + self.nombre)   

    @property
    def edad(self):
     return self.__edad

    @edad.setter
    def edad(self,valor):
        self.__edad = valor 

class Empleado(Usuario):
    __salario = 0

    def modificar_salario(self,salario):
        self.__salario = salario
    def ver_salario(self):
        print(self.__salario)
    def saludar(self):
        print("Mi nombre es: "+self._nombre+" y ganó: "+ str(self.__salario))
        


Empleado = Empleado ("Brian")
Empleado.edad = 23
print(Empleado.edad)