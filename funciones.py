def saludar(nombre):
    return "Hola {} bienvenidos al juego de Cody".format(nombre)


print("Ingrese tu nombre")
nombre = input()
print(saludar(nombre))