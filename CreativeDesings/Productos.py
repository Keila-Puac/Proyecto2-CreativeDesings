class Producto:
    def __init__(self, id_producto, nombre, precio):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - Q{self.precio}"
