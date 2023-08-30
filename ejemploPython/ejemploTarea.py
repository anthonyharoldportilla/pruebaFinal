class producto:
    def __init__(self,nombre,codigo):
        self.nombreProducto=nombre
        self.codigoProducto=codigo
        self.precioProducto=''

    def ingresarPrecio(self, precioProducto):
        self.precioProducto=precioProducto

if __name__=='__main__':
    productoSistema = []
    comandosSistema= ['R','P','M','X']
    while True:
        comandoInformacion = input("Ingrese un comando : ")
        print(f"El comando ingresado es {comandoInformacion}")
        if comandoInformacion in comandosSistema:
            if comandoInformacion=='R':
                print("se registrara un nuevo producto:")
                nombreProducto=input("ingrese el nombre del producto :")
                codigoProducto=input("Ingrese codigo del producto")
                objProducto=producto(nombreProducto,codigoProducto)
                productosSistema.append(objProducto)
            elif  comandoInformacion=='P':
                print("se actualizaran los precios")
                for productoInfo in productosSistema:
                    if productoInfo.precioProducto=='';
                        precioProducto=input(f"INgrese el precio del producto {productoInfo.nombreProducto}")
                        productoInfo.ingresarPrecio(precioProducto)

            elif comandoInformacion=='M':
                 print("Se mostrara la informacion de los productos")
                 i=0
                 for productoInfo in productosSistema:
                    print(f"mostrando informacion del producto {i}")
                    print(f"Nombre del producto :  {productoInfo.nombreProducto}")
                    print(f"codigo del producto :  {productoInfo.codigoProducto}")
                    print(f"precio del producto :  {productoInfo.precioProducto}")
                    print(f"Precio del producto : {productoInfo.precioProducto}")
                    i = i + 1
                    print("\n")
            else:
                print("comando de finalizacion")
                break
        else:
            print('Comando incorrecto, vuelva a ingresarlo')