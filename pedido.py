# cliente/pedido.py
from datetime import datetime

class Pedido:
    def __init__(self, id_pedido, cliente_nombre, items, buscar_producto):
        self.id_pedido = id_pedido
        self.cliente = cliente_nombre
        self.items = items
        self.estado = "creado"
        self.fecha = datetime.now().isoformat(timespec='seconds')
        self.buscar_producto = buscar_producto

    def total(self):
        return sum(self.buscar_producto(pid)["precio"] * qty for pid, qty in self.items)

    def generar_factura(self):
        lines = [f"Factura #{self.id_pedido}", f"Cliente: {self.cliente}", f"Fecha: {self.fecha}", "-"*40]
        for pid, qty in self.items:
            prod = self.buscar_producto(pid)
            lines.append(f"{prod['nombre']} x{qty} - Q{prod['precio']:.2f}")
        lines.append("-"*40)
        lines.append(f"Total: Q{self.total():.2f}")
        return "\n".join(lines)
