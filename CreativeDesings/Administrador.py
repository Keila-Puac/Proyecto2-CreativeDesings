#Administrador
#Agregar Productos
#Modificar Productos
#Eliminar Productos
#Ver cotización 
#Ver lista de pedidos
#Crear roles dentro del sistema
#Reporte ventas 

productos_disponibles = {}

class Administrador:
    def __init__(self):
        pass

    def agregar_producto():
        print("---------- Agregar Productos ----------")
        while True:
            nombre = input("Nombre del producto (o 'salir' para terminar): ")
            if nombre.lower() == "salir":
                break
            precio = float(input("Precio del producto: Q"))
            productos_disponibles[nombre] = precio
            print("Producto agregado \n")

        print("Productos registrados:", productos_disponibles)

