class estudiante:    
    def __init__(self,nombre,apellido,edad,codigo,nacionalidad):
        self.nombre=nombre
        self.apellido=apellido
        self.edad=edad
        self.codigo=codigo
        self.nacionalidad=nacionalidad
    
    def MostrarNombre(self):
         print(f"El nombre del objeto es: {self.nombre}")


    def MostrarCodigo(self):
         print(f"El codigo del objeto es: {self.codigo}")

    def modificarCodigo(self,codigo):
        self.codigo = codigo     
         print(f"El nuevo codigo del objeto es: {self.codigo}")

est1 = estudiante('Alexander','Segovia','26','20110291','Peruano')
est2 = estudiante('Javier','Hilario','31','20140291','Peruano')
est3 = estudiante('Luis','Velasco','35','20122222','Argetino')
est4 = estudiante('Manuel','Escobar','28','20153432','Peruano')

print(est1.nombre)
print(est3.nombre)

est1.MostrarNombre()
est2.MostrarNombre()
est3.MostrarNombre()
est4.MostrarNombre()


print("modificacion del codigo para estudiantes 1")
est1.MostrarCodigo()
nuevoCodigo=input("ingrese el nuevo codigo para est1:")
est1.modificarCodigo(nuevoCodigo)