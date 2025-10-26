# Clase Producto
class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Id-{self.id_producto} -{self.nombre} - Q{self.precio}"


# Lista de productos 
productos = [
    Producto(1, "Sticker Vinilo de Corte 15x15cm", 20),
    Producto(2, "Sticker Holográfico Corte Electrónico", 40),
    Producto(3, "Sticker Holográfico Hoja Impresa", 30),
    Producto(4, "Sticker en Papel Adhesivo con Corte Electrónico", 30),
    Producto(5, "Sticker en Papel Adhesivo sin Corte", 35),
    Producto(6, "Vinilo Especial Dorado Espejo", 30),
    Producto(7, "Vinilo Especial Cromo Espejo", 30),
    Producto(8, "Vinilo Tornasol", 30),
    Producto(9, "Vinilo Reflectivo Amarillo/Rojo/Blanco", 40),
]

def ordenar_productos_por_categoria(lista_productos):
    for i in range(1, len(lista_productos)):
        producto = lista_productos[i]
        j = i - 1
        while j >= 0 and producto.categoria.lower() < lista_productos[j].categoria.lower():
            lista_productos[j + 1] = lista_productos[j]
            j -= 1
        lista_productos[j + 1] = producto

    print("Productos ordenados por categoría:")
    for p in lista_productos:
        print(p)
    print()
