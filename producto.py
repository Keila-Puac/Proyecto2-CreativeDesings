# producto/producto.py
from producto.hash_table import TablaHash

class ProductoManager:
    def __init__(self):
        self.productos = []
        self.hash_productos = TablaHash(13)

    def agregar(self, prod):
        self.productos.append(prod)
        self.hash_productos.insertar(prod["id"], prod)

    def eliminar(self, id_prod):
        self.hash_productos.eliminar(id_prod)
        self.productos = [p for p in self.productos if p["id"] != id_prod]

    def buscar_por_id(self, id_prod):
        return self.hash_productos.buscar(id_prod)

    def listar(self):
        return self.productos
