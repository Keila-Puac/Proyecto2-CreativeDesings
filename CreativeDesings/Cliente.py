class Cliente:
    def __init__(self, id_cliente, nombre, correo, telefono): #Inicializa un cliente con sus datos personales y un carrito vacío.
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.carrito = []

    def visualizar_producto(self, lista_productos): #Muestra todos los productos disponibles.
        print("--- Lista de productos ---")
        for p in lista_productos:
            print(p)
        print()

    def buscar_producto(self, lista_productos, nombre_buscar): #Busca productos por nombre (insensible a mayúsculas/minúsculas).
        encontrados = [p for p in lista_productos if nombre_buscar.lower() in p.nombre.lower()] # Busca si esta el producto en la lista
        if encontrados:
            print("Productos encontrados:")
            for p in encontrados:
                print(p)
        else:
            print("No se encontró el producto.")
        print()

    def agregar_al_carrito(self, producto, cantidad): #Agrega un producto al carrito si hay suficiente stock.
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.stock -= cantidad
            print(f"{cantidad}x {producto.nombre} agregado(s) al carrito.")
        else:
            print("No hay suficiente stock.")
        print()

    def mostrar_carrito(self,precio): #Muestra los productos en el carrito y calcula el total a pagar.
        if not self.carrito:
            print("El carrito está vacío.")
            return 0
        total = 0
        print(f"--- Carrito de {self.nombre} ---")
        for p, c in self.carrito:
            subtotal = p.precio * c
            print(f"{p.nombre} x{c} = Q{subtotal}")
            total += subtotal
        print(f"Total a pagar: Q{total}\n")
        return total

    def consultar_envio(self, direccion): #Muestra la dirección de envío del pedido
        print(f"El pedido será enviado a: {direccion}\n")
    
    