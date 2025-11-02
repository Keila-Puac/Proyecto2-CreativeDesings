class Producto:
    def __init__(self, id_producto=None, nombre="", precio=0.0, medida="", especificaciones="", categoria_id=None):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.medida = medida
        self.especificaciones = especificaciones
        self.categoria_id = categoria_id
    
    def __str__(self):
        return f"Id-{self.id_producto} - {self.nombre} - Q{self.precio:.2f}"
    
    def to_dict(self):
        """Convierte el objeto a diccionario"""
        return {
            'id_producto': self.id_producto,
            'nombre': self.nombre,
            'precio': self.precio,
            'medida': self.medida,
            'especificaciones': self.especificaciones,
            'categoria_id': self.categoria_id
        }

# Función de ordenamiento por inserción
def ordenar_productos_por_nombre(lista_productos):
    """Ordena productos alfabéticamente por nombre usando insertion sort"""
    for i in range(1, len(lista_productos)):
        producto = lista_productos[i]
        j = i - 1
        while j >= 0 and producto.nombre.lower() < lista_productos[j].nombre.lower():
            lista_productos[j + 1] = lista_productos[j]
            j -= 1
        lista_productos[j + 1] = producto
    return lista_productos

def ordenar_productos_por_precio(lista_productos):
    """Ordena productos por precio de menor a mayor"""
    for i in range(1, len(lista_productos)):
        producto = lista_productos[i]
        j = i - 1
        while j >= 0 and producto.precio < lista_productos[j].precio:
            lista_productos[j + 1] = lista_productos[j]
            j -= 1
        lista_productos[j + 1] = producto
    return lista_productos