class Cliente:
    def __init__(self, id_cliente, nombre, correo, telefono):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f"Cliente: {self.nombre} - {self.correo} - {self.telefono}"
