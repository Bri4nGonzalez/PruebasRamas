from abc import ABC, abstractmethod

#clases absrtract

class EstructuraAbstracta(ABC):
    @abstractmethod
    def obtener():
        pass

    @abstractmethod
    def agregar():
        pass

class hash(EstructuraAbstracta):
    datos = {}

    def obtener(self,llave):
        datos[llave]

    def Queue(self,llave,valor):
        datos[llave]= valor
    
class Queue(EstructuraAbstracta):
    datos = []

    def obtener(self):
        datos[0]

    def agregar(self,llave,valor):
        datos[len(datos)-1] = valor   

class Filabanco:
    def __init__(self,almacen_usuarios):
        if not isinstance(almacen_usuarios, EstructuraAbstracta):
            raise ValueError('Store is not supported')
        self.usuarios = almacen_usuarios
    
    def siguiente_usuario(self,numero):
        # Implementacion
        return self.usuarios.obtener(numero)
    
    def formar_usuario(self,numero,usuario):
        self.usuarios.agregar(numero,usuario)
Filabanco([])



