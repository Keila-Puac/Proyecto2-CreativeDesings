# main.py
from producto.producto import ProductoManager
from producto.busquedas import busqueda_secuencial, busqueda_binaria
from producto.ordenamientos import ordenar_automaticamente
from administrador import seguridad
from cliente.pedido import Pedido
import getpass

pm = ProductoManager()
contador_pedidos = 1
pedidos = []

def menu_cliente():
    global contador_pedidos
    while True:
        print("\n=== CLIENTE ===")
        print("1. Ver productos")
        print("2. Buscar producto")
        print("3. Hacer pedido")
        print("4. Salir")
        op = input("> ")
        if op == "1":
            for p in pm.listar():
                print(f"{p['id']} | {p['nombre']} | Q{p['precio']}")
        elif op == "2":
            nombre = input("Nombre producto: ")
            idx, pasos = busqueda_secuencial(pm.listar(), nombre)
            print("Resultado:", pm.listar()[idx] if idx >= 0 else "No encontrado", "pasos:", pasos)
        elif op == "3":
            cli = input("Nombre cliente: ")
            items = []
            while True:
                pid = int(input("ID producto (0 salir): "))
                if pid == 0: break
                cant = int(input("Cantidad: "))
                items.append((pid, cant))
            pedido = Pedido(contador_pedidos, cli, items, pm.buscar_por_id)
            print(pedido.generar_factura())
            pedidos.append(pedido)
            contador_pedidos += 1
        elif op == "4":
            break

def menu_admin():
    if not seguridad.leer_hash():
        print("Primera vez: crea contraseña admin.")
        seguridad.crear_o_cambiar()
    else:
        if not seguridad.verificar(getpass.getpass("Contraseña: ")):
            print("Acceso denegado.")
            return
    while True:
        print("\n=== ADMIN ===")
        print("1. Agregar producto")
        print("2. Eliminar producto")
        print("3. Ordenar productos automáticamente")
        print("4. Cambiar contraseña")
        print("5. Salir")
        op = input("> ")
        if op == "1":
            nid = int(input("ID: "))
            nombre = input("Nombre: ")
            precio = float(input("Precio: "))
            cat = input("Categoría: ")
            pm.agregar({"id": nid, "nombre": nombre, "precio": precio, "categoria": cat})
            print("Agregado.")
        elif op == "2":
            pm.eliminar(int(input("ID a eliminar: ")))
            print("Eliminado.")
        elif op == "3":
            metodo, lista_ordenada = ordenar_automaticamente(pm.listar())
            print(f"Ordenado con {metodo}:")
            for p in lista_ordenada:
                print(p)
        elif op == "4":
            seguridad.crear_o_cambiar()
        elif op == "5":
            break

def main():
    while True:
        print("\n=== SISTEMA CREATIVE DESIGNS ===")
        print("1. Cliente")
        print("2. Administrador")
        print("3. Salir")
        op = input("> ")
        if op == "1":
            menu_cliente()
        elif op == "2":
            menu_admin()
        elif op == "3":
            print("Fin del programa.")
            break

if __name__ == "__main__":
    main()
