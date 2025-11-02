# Diccionario global para guardar los productos
productos_disponibles = {}

def agregar_producto():
    print("---------- Agregar Producto ----------")
    nombre_producto = input("Ingrese el nombre del nuevo producto: ")
    precio = float(input("Ingrese el precio del producto: Q"))
    
    # Agrega al diccionario
    productos_disponibles[nombre_producto] = precio
    
    print("\nProducto agregado correctamente.")
    print("Productos actualizados:", productos_disponibles)

# Llamada a la función
agregar_producto()
