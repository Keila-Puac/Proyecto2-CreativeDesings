"""
SISTEMA DE GESTIÓN CREATIVE DESIGNS
Sistema completo implementando todas las estructuras de datos requeridas

Autor: Creative Designs Team
Fecha: 2025
Descripción: Sistema principal con manejo robusto de errores
"""

import sys
import os
import logging
from datetime import datetime
from typing import Optional, List

# Importar modelos
try:
    from Cliente import Cliente
    from Productos import Producto
    from Administrador import Administrador
except ImportError as e:
    print(f"Error al importar modelos: {e}")
    sys.exit(1)

# Importar DAOs
try:
    from Data.clienteDAO import ClienteDAO
    from Data.productoDAO import ProductoDAO
    from RegistroUsuario import RegistroUsuario
except ImportError as e:
    print(f"Error al importar DAOs: {e}")
    sys.exit(1)

# Importar estructuras y algoritmos
try:
    from EstructurasDatos import Pila, Cola, ListaEnlazada, TablaHash, MatrizVentas
    from Ordenamiento import (AlgoritmosOrdenamiento, ordenar_productos_por_precio, 
                              ordenar_productos_por_nombre, ordenar_clientes_por_nombre)
    from Busqueda import (AlgoritmosBusqueda, buscar_producto_por_id, 
                         buscar_productos_por_nombre, CacheBusqueda)
except ImportError as e:
    print(f"Error al importar estructuras/algoritmos: {e}")
    sys.exit(1)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('creative_designs.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class SistemaCreativeDesigns:
    """
    Sistema principal que integra todas las estructuras de datos
    """
    def __init__(self):
        """Inicializa el sistema con todas las estructuras"""
        try:
            # DAOs para base de datos
            self.cliente_dao = ClienteDAO()
            self.producto_dao = ProductoDAO()
            self.registro_usuario = RegistroUsuario()
            
            # Usuario actual
            self.usuario_actual = None
            
            # ESTRUCTURAS DE DATOS
            self.historial_acciones = Pila()
            self.cola_pedidos = Cola()
            self.carrito = ListaEnlazada()
            self.cache_productos = TablaHash(tamano=100)
            self.cache_busqueda = CacheBusqueda()
            self.matriz_ventas = MatrizVentas(num_productos=20, num_meses=12)
            
            # Contadores
            self.contador_busquedas = 0
            self.contador_ordenamientos = 0
            
            logger.info("Sistema Creative Designs inicializado correctamente")
            
        except Exception as e:
            logger.error(f"Error al inicializar sistema: {e}")
            print(f"Error crítico al inicializar el sistema: {e}")
            sys.exit(1)
    
    def limpiar_pantalla(self):
        """Limpia la consola"""
        try:
            os.system('cls' if os.name == 'nt' else 'clear')
        except Exception as e:
            logger.error(f"Error al limpiar pantalla: {e}")
    
    def pausar(self):
        """Pausa la ejecución"""
        try:
            input("\nPresione Enter para continuar...")
        except Exception as e:
            logger.error(f"Error en pausa: {e}")
    
    def registrar_accion(self, accion: str):
        """Registra acción en la pila de historial"""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.historial_acciones.apilar(f"[{timestamp}] {accion}")
            logger.info(f"Acción registrada: {accion}")
        except Exception as e:
            logger.error(f"Error al registrar acción: {e}")
    
    # ==================== MENÚ PRINCIPAL ====================
    
    def menu_principal(self):
        """Menú principal del sistema"""
        while True:
            try:
                self.limpiar_pantalla()
                print("="*70)
                print("     CREATIVE DESIGNS - Sistema de Gestión de Ventas")
                print("="*70)
                print("\nSistema implementando estructuras de datos avanzadas")
                print("\n1. Ingresar como Cliente")
                print("2. Ingresar como Administrador")
                print("3. Registrar nuevo administrador")
                print("4. Ver estadísticas del sistema")
                print("5. Salir")
                
                opcion = input("\nSeleccione una opción: ")
                
                if opcion == '1':
                    self.menu_cliente()
                elif opcion == '2':
                    self.login_administrador()
                elif opcion == '3':
                    self.registrar_usuario()
                elif opcion == '4':
                    self.mostrar_estadisticas_sistema()
                elif opcion == '5':
                    print("\nGracias por usar Creative Designs!")
                    logger.info("Sistema cerrado correctamente")
                    sys.exit()
                else:
                    print("\nOpción inválida")
                    self.pausar()
                    
            except KeyboardInterrupt:
                print("\n\nSaliendo del sistema...")
                logger.info("Sistema interrumpido por usuario")
                sys.exit()
            except Exception as e:
                logger.error(f"Error en menú principal: {e}")
                print(f"\nError inesperado: {e}")
                self.pausar()
    
    # ==================== CLIENTE ====================
    
    def menu_cliente(self):
        """Menú para clientes"""
        while True:
            try:
                self.limpiar_pantalla()
                print("="*70)
                print("                    MENÚ CLIENTE")
                print("="*70)
                print("\nCATÁLOGO Y COMPRAS")
                print("1. Ver todos los productos (ordenados)")
                print("2. Buscar productos por nombre")
                print("3. Buscar por rango de precios")
                print("4. Ver productos por categoría")
                print("\nCARRITO Y PEDIDOS")
                print("5. Agregar producto al carrito")
                print("6. Ver mi carrito")
                print("7. Finalizar compra")
                print("8. Ver mis pedidos pendientes")
                print("\nOTRAS OPCIONES")
                print("9. Ver historial de acciones")
                print("10. Comparar algoritmos de ordenamiento")
                print("11. Volver al menú principal")
                
                opcion = input("\nSeleccione una opción: ")
                
                if opcion == '1':
                    self.ver_productos_ordenados()
                elif opcion == '2':
                    self.buscar_productos()
                elif opcion == '3':
                    self.buscar_por_rango_precios()
                elif opcion == '4':
                    self.ver_productos_por_categoria()
                elif opcion == '5':
                    self.agregar_al_carrito()
                elif opcion == '6':
                    self.ver_carrito()
                elif opcion == '7':
                    self.finalizar_compra()
                elif opcion == '8':
                    self.ver_pedidos_pendientes()
                elif opcion == '9':
                    self.ver_historial()
                elif opcion == '10':
                    self.comparar_algoritmos()
                elif opcion == '11':
                    break
                else:
                    print("\nOpción inválida")
                    self.pausar()
                    
            except KeyboardInterrupt:
                print("\n\nVolviendo al menú principal...")
                break
            except Exception as e:
                logger.error(f"Error en menú cliente: {e}")
                print(f"\nError: {e}")
                self.pausar()
    
    def ver_productos_ordenados(self):
        """Muestra productos con diferentes ordenamientos"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("              CATÁLOGO DE PRODUCTOS")
            print("="*70)
            
            print("\nComo desea ordenar los productos?")
            print("1. Por nombre (A-Z)")
            print("2. Por nombre (Z-A)")
            print("3. Por precio (menor a mayor)")
            print("4. Por precio (mayor a menor)")
            print("5. Sin ordenar")
            
            opcion = input("\nOpción: ")
            
            productos = self.producto_dao.listar()
            
            if not productos:
                print("\nNo hay productos disponibles")
                self.pausar()
                return
            
            # Aplicar ordenamiento según opción
            if opcion == '1':
                productos = ordenar_productos_por_nombre(productos, algoritmo='quick')
                algoritmo_usado = "Quick Sort (por nombre A-Z)"
            elif opcion == '2':
                productos = ordenar_productos_por_nombre(productos, algoritmo='quick', reverso=True)
                algoritmo_usado = "Quick Sort (por nombre Z-A)"
            elif opcion == '3':
                productos = ordenar_productos_por_precio(productos, algoritmo='quick')
                algoritmo_usado = "Quick Sort (por precio ascendente)"
            elif opcion == '4':
                productos = ordenar_productos_por_precio(productos, algoritmo='quick', reverso=True)
                algoritmo_usado = "Quick Sort (por precio descendente)"
            else:
                algoritmo_usado = "Sin ordenamiento"
            
            self.contador_ordenamientos += 1
            self.registrar_accion(f"Ordenamiento aplicado: {algoritmo_usado}")
            
            print(f"\nAlgoritmo usado: {algoritmo_usado}")
            print(f"\n{'ID':<5} {'Nombre':<45} {'Precio':<10} {'Medida':<15}")
            print("-"*75)
            for p in productos:
                print(f"{p.id_producto:<5} {p.nombre:<45} Q{p.precio:<9.2f} {p.medida:<15}")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al ver productos ordenados: {e}")
            print(f"\nError al mostrar productos: {e}")
            self.pausar()
    
    def buscar_productos(self):
        """Búsqueda de productos por nombre"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("              BUSCAR PRODUCTOS")
            print("="*70)
            
            nombre = input("\nIngrese el nombre del producto: ")
            
            if not nombre:
                print("\nDebe ingresar un nombre")
                self.pausar()
                return
            
            # Primero buscar en caché
            productos_cache = self.cache_busqueda.buscar(nombre.lower())
            
            if productos_cache:
                print("\nEncontrado en caché (Búsqueda O(1))")
                productos = productos_cache
            else:
                # Búsqueda secuencial en base de datos
                productos = buscar_productos_por_nombre(
                    self.producto_dao.listar(), 
                    nombre
                )
                # Guardar en caché
                self.cache_busqueda.agregar(nombre.lower(), productos)
                print("\nBúsqueda secuencial completada")
            
            self.contador_busquedas += 1
            self.registrar_accion(f"Búsqueda: '{nombre}'")
            
            if productos:
                print(f"\n{'ID':<5} {'Nombre':<45} {'Precio':<10}")
                print("-"*60)
                for p in productos:
                    print(f"{p.id_producto:<5} {p.nombre:<45} Q{p.precio:<9.2f}")
                print(f"\nEncontrados: {len(productos)} productos")
            else:
                print(f"\nNo se encontraron productos con '{nombre}'")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al buscar productos: {e}")
            print(f"\nError en búsqueda: {e}")
            self.pausar()
    
    def buscar_por_rango_precios(self):
        """Búsqueda por rango de precios"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("          BUSCAR POR RANGO DE PRECIOS")
            print("="*70)
            
            precio_min = float(input("\nPrecio mínimo: Q"))
            precio_max = float(input("Precio máximo: Q"))
            
            if precio_min > precio_max:
                print("\nEl precio mínimo no puede ser mayor al máximo")
                self.pausar()
                return
            
            productos = self.producto_dao.listar()
            productos_ordenados = ordenar_productos_por_precio(productos, algoritmo='shell')
            
            resultados = []
            for p in productos_ordenados:
                if precio_min <= p.precio <= precio_max:
                    resultados.append(p)
                elif p.precio > precio_max:
                    break
            
            self.registrar_accion(f"Búsqueda por rango: Q{precio_min} - Q{precio_max}")
            
            if resultados:
                print(f"\nProductos encontrados en el rango Q{precio_min} - Q{precio_max}:")
                print(f"\n{'ID':<5} {'Nombre':<40} {'Precio':<10}")
                print("-"*55)
                for p in resultados:
                    print(f"{p.id_producto:<5} {p.nombre:<40} Q{p.precio:<9.2f}")
            else:
                print(f"\nNo hay productos en ese rango de precios")
            
            self.pausar()
            
        except ValueError:
            print("\nIngrese valores numéricos válidos")
            self.pausar()
        except Exception as e:
            logger.error(f"Error en búsqueda por rango: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def ver_productos_por_categoria(self):
        """Ver productos por categoría"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           PRODUCTOS POR CATEGORÍA")
            print("="*70)
            
            categorias = self.producto_dao.listar_categorias()
            
            if not categorias:
                print("\nNo hay categorías disponibles")
                self.pausar()
                return
            
            print("\nCategorías disponibles:")
            for cat in categorias:
                print(f"\n{cat['id']}. {cat['nombre']}")
                print(f"   {cat['descripcion']}")
            
            cat_id = int(input("\nSeleccione categoría (0 para volver): "))
            
            if cat_id == 0:
                return
            
            productos = self.producto_dao.listar_por_categoria(cat_id)
            
            if productos:
                categoria_nombre = next((c['nombre'] for c in categorias if c['id'] == cat_id), "")
                self.limpiar_pantalla()
                print("="*70)
                print(f"              {categoria_nombre.upper()}")
                print("="*70)
                print(f"\n{'ID':<5} {'Nombre':<40} {'Precio':<10} {'Medida':<15}")
                print("-"*70)
                for p in productos:
                    print(f"{p.id_producto:<5} {p.nombre:<40} Q{p.precio:<9.2f} {p.medida:<15}")
                
                self.registrar_accion(f"Visualizó categoría: {categoria_nombre}")
            else:
                print("\nNo hay productos en esta categoría")
            
            self.pausar()
            
        except ValueError:
            print("\nIngrese un número válido")
            self.pausar()
        except Exception as e:
            logger.error(f"Error al ver productos por categoría: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def agregar_al_carrito(self):
        """Agrega producto al carrito (Lista Enlazada)"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           AGREGAR AL CARRITO")
            print("="*70)
            
            id_producto = int(input("\nID del producto: "))
            cantidad = int(input("Cantidad: "))
            
            if cantidad <= 0:
                print("\nLa cantidad debe ser mayor a 0")
                self.pausar()
                return
            
            # Buscar producto
            producto = buscar_producto_por_id(
                self.producto_dao.listar(), 
                id_producto
            )
            
            if producto:
                item_carrito = {
                    'producto': producto,
                    'cantidad': cantidad,
                    'subtotal': producto.precio * cantidad
                }
                self.carrito.agregar_final(item_carrito)
                
                print(f"\n{producto.nombre} agregado al carrito")
                print(f"   Cantidad: {cantidad} | Subtotal: Q{item_carrito['subtotal']:.2f}")
                
                self.registrar_accion(f"Agregó al carrito: {producto.nombre} x{cantidad}")
            else:
                print("\nProducto no encontrado")
            
            self.pausar()
            
        except ValueError:
            print("\nIngrese valores numéricos válidos")
            self.pausar()
        except Exception as e:
            logger.error(f"Error al agregar al carrito: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def ver_carrito(self):
        """Muestra el carrito (Lista Enlazada)"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("              MI CARRITO DE COMPRAS")
            print("="*70)
            
            items = self.carrito.obtener_lista()
            
            if not items:
                print("\nEl carrito está vacío")
            else:
                print(f"\n{'Producto':<40} {'Cant':<6} {'P. Unit':<10} {'Subtotal':<10}")
                print("-"*66)
                total = 0
                for item in items:
                    nombre = item['producto'].nombre[:40]
                    print(f"{nombre:<40} {item['cantidad']:<6} "
                          f"Q{item['producto'].precio:<9.2f} Q{item['subtotal']:<9.2f}")
                    total += item['subtotal']
                print("-"*66)
                print(f"{'TOTAL:':<56} Q{total:.2f}")
                print(f"\nItems en carrito: {len(items)}")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al ver carrito: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def finalizar_compra(self):
        """Finaliza la compra y genera pedido (Cola)"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           FINALIZAR COMPRA")
            print("="*70)
            
            items = self.carrito.obtener_lista()
            
            if not items:
                print("\nEl carrito está vacío")
                self.pausar()
                return
            
            # Mostrar resumen
            print("\nResumen del pedido:")
            total = 0
            for item in items:
                print(f"  - {item['producto'].nombre} x{item['cantidad']} = Q{item['subtotal']:.2f}")
                total += item['subtotal']
            print(f"\nTotal: Q{total:.2f}")
            
            # Solicitar datos
            nombre = input("\nNombre completo: ")
            telefono = input("Teléfono: ")
            direccion = input("Dirección de entrega: ")
            
            # Crear pedido
            pedido = {
                'cliente': {'nombre': nombre, 'telefono': telefono, 'direccion': direccion},
                'items': items,
                'total': total,
                'fecha': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'estado': 'pendiente'
            }
            
            # Agregar a cola de pedidos
            self.cola_pedidos.encolar(pedido)
            
            # Limpiar carrito
            self.carrito = ListaEnlazada()
            
            print("\nPedido realizado con éxito!")
            print(f"Su pedido ha sido agregado a la cola de procesamiento")
            print(f"Pedidos pendientes: {self.cola_pedidos.tamano()}")
            
            self.registrar_accion(f"Pedido realizado por {nombre} - Total: Q{total:.2f}")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al finalizar compra: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def ver_pedidos_pendientes(self):
        """Muestra pedidos en la cola"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           PEDIDOS PENDIENTES")
            print("="*70)
            
            pedidos = self.cola_pedidos.listar()
            
            if not pedidos:
                print("\nNo hay pedidos pendientes")
            else:
                print(f"\nTotal de pedidos en cola: {len(pedidos)}")
                for i, pedido in enumerate(pedidos, 1):
                    print(f"\n--- Pedido #{i} ---")
                    print(f"Cliente: {pedido['cliente']['nombre']}")
                    print(f"Total: Q{pedido['total']:.2f}")
                    print(f"Fecha: {pedido['fecha']}")
                    print(f"Estado: {pedido['estado']}")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al ver pedidos: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def ver_historial(self):
        """Muestra historial de acciones (Pila)"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           HISTORIAL DE ACCIONES")
            print("="*70)
            
            if self.historial_acciones.esta_vacia():
                print("\nNo hay acciones registradas")
            else:
                print(f"\nTotal de acciones: {self.historial_acciones.tamano()}")
                print("\nÚltimas 10 acciones:")
                
                temp_pila = Pila()
                contador = 0
                
                while not self.historial_acciones.esta_vacia() and contador < 10:
                    accion = self.historial_acciones.desapilar()
                    print(f"  {contador + 1}. {accion}")
                    temp_pila.apilar(accion)
                    contador += 1
                
                # Restaurar pila
                while not temp_pila.esta_vacia():
                    self.historial_acciones.apilar(temp_pila.desapilar())
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al ver historial: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def comparar_algoritmos(self):
        """Compara tiempos de ejecución de algoritmos"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("       COMPARACIÓN DE ALGORITMOS DE ORDENAMIENTO")
            print("="*70)
            
            productos = self.producto_dao.listar()
            
            if len(productos) < 5:
                print("\nSe necesitan al menos 5 productos para comparar")
                self.pausar()
                return
            
            print(f"\nComparando con {len(productos)} productos...")
            
            import time
            resultados = {}
            
            algoritmos = {
                'Bubble Sort': AlgoritmosOrdenamiento.bubble_sort,
                'Selection Sort': AlgoritmosOrdenamiento.selection_sort,
                'Shell Sort': AlgoritmosOrdenamiento.shell_sort,
                'Quick Sort': AlgoritmosOrdenamiento.quick_sort
            }
            
            for nombre, funcion in algoritmos.items():
                inicio = time.time()
                funcion(productos, clave=lambda p: p.precio)
                fin = time.time()
                resultados[nombre] = (fin - inicio) * 1000
            
            print("\nTiempos de ejecución:")
            print(f"\n{'Algoritmo':<20} {'Tiempo (ms)':<15} {'Complejidad':<15}")
            print("-"*50)
            
            complejidades = {
                'Bubble Sort': 'O(n²)',
                'Selection Sort': 'O(n²)',
                'Shell Sort': 'O(n log n)',
                'Quick Sort': 'O(n log n)'
            }
            
            for algoritmo, tiempo in sorted(resultados.items(), key=lambda x: x[1]):
                print(f"{algoritmo:<20} {tiempo:<15.4f} {complejidades[algoritmo]:<15}")
            
            mas_rapido = min(resultados, key=resultados.get)
            print(f"\nAlgoritmo más eficiente: {mas_rapido}")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al comparar algoritmos: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    # ==================== ADMINISTRADOR ====================
    
    def login_administrador(self):
        """Login para administradores"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("            ACCESO ADMINISTRADOR")
            print("="*70)
            
            usuario = input("\nUsuario: ")
            password = input("Contraseña: ")
            
            admin = self.registro_usuario.validar_login(usuario, password)
            
            if admin:
                self.usuario_actual = admin
                print(f"\nBienvenido {admin.nombre}")
                self.registrar_accion(f"Login administrador: {admin.nombre}")
                self.pausar()
                self.menu_administrador()
            else:
                print("\nCredenciales incorrectas")
                self.pausar()
                
        except Exception as e:
            logger.error(f"Error en login: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def menu_administrador(self):
        """Menú administrador"""
        while True:
            try:
                self.limpiar_pantalla()
                print("="*70)
                print("                PANEL DE ADMINISTRACIÓN")
                print("="*70)
                print(f"\nUsuario: {self.usuario_actual.nombre} | Rol: {self.usuario_actual.rol}")
                
                print("\nGESTIÓN DE PRODUCTOS")
                print("1. Agregar producto")
                print("2. Modificar producto")
                print("3. Eliminar producto")
                print("4. Ver todos los productos")
                
                print("\nGESTIÓN DE CLIENTES")
                print("5. Ver lista de clientes")
                print("6. Buscar cliente")
                
                print("\nGESTIÓN DE PEDIDOS")
                print("7. Procesar siguiente pedido (Cola)")
                print("8. Ver todos los pedidos pendientes")
                
                print("\nREPORTES Y ESTADÍSTICAS")
                print("9. Estadísticas del sistema")
                print("10. Reporte de ventas (Matriz)")
                
                print("\nSISTEMA")
                print("11. Gestionar usuarios")
                print("12. Ver caché de búsquedas")
                print("13. Cerrar sesión")
                
                opcion = input("\nSeleccione una opción: ")
                
                if opcion == '1':
                    self.agregar_producto()
                elif opcion == '2':
                    self.modificar_producto()
                elif opcion == '3':
                    self.eliminar_producto()
                elif opcion == '4':
                    self.ver_productos_ordenados()
                elif opcion == '5':
                    self.ver_clientes()
                elif opcion == '6':
                    self.buscar_clientes()
                elif opcion == '7':
                    self.procesar_pedido()
                elif opcion == '8':
                    self.ver_pedidos_pendientes()
                elif opcion == '9':
                    self.mostrar_estadisticas_sistema()
                elif opcion == '10':
                    self.reporte_ventas_matriz()
                elif opcion == '11':
                    self.gestionar_usuarios()
                elif opcion == '12':
                    self.ver_estadisticas_cache()
                elif opcion == '13':
                    self.usuario_actual = None
                    break
                else:
                    print("\nOpción inválida")
                    self.pausar()
                    
            except KeyboardInterrupt:
                print("\n\nCerrando sesión...")
                self.usuario_actual = None
                break
            except Exception as e:
                logger.error(f"Error en menú administrador: {e}")
                print(f"\nError: {e}")
                self.pausar()
    
    def agregar_producto(self):
        """Agrega un nuevo producto"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           AGREGAR NUEVO PRODUCTO")
            print("="*70)
            
            categorias = self.producto_dao.listar_categorias()
            print("\nCategorías disponibles:")
            for cat in categorias:
                print(f"{cat['id']}. {cat['nombre']}")
            
            categoria_id = int(input("\nCategoría: "))
            nombre = input("Nombre: ")
            precio = float(input("Precio (Q): "))
            medida = input("Medida: ")
            especificaciones = input("Especificaciones: ")
            
            producto = Producto(None, nombre, precio, medida, especificaciones, categoria_id)
            
            if self.producto_dao.insertar(producto):
                print("\nProducto agregado exitosamente")
                self.registrar_accion(f"Producto agregado: {nombre}")
            else:
                print("\nError al agregar el producto")
            
            self.pausar()
            
        except ValueError:
            print("\nDatos inválidos")
            self.pausar()
        except Exception as e:
            logger.error(f"Error al agregar producto: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def modificar_producto(self):
        """Modifica producto"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           MODIFICAR PRODUCTO")
            print("="*70)
            
            id_producto = int(input("\nID del producto: "))
            producto = self.producto_dao.buscar_por_id(id_producto)
            
            if producto:
                print(f"\nProducto actual: {producto.nombre}")
                print(f"Precio actual: Q{producto.precio:.2f}")
                
                print("\nIngrese nuevos datos (Enter para mantener):")
                nombre = input(f"Nombre [{producto.nombre}]: ") or producto.nombre
                precio_input = input(f"Precio [{producto.precio}]: ")
                precio = float(precio_input) if precio_input else producto.precio
                
                producto.nombre = nombre
                producto.precio = precio
                
                if self.producto_dao.actualizar(producto):
                    print("\nProducto actualizado")
                    self.registrar_accion(f"Producto modificado: {nombre}")
                else:
                    print("\nError al actualizar")
            else:
                print("\nProducto no encontrado")
            
            self.pausar()
            
        except ValueError:
            print("\nDatos inválidos")
            self.pausar()
        except Exception as e:
            logger.error(f"Error al modificar producto: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def eliminar_producto(self):
        """Elimina producto"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           ELIMINAR PRODUCTO")
            print("="*70)
            
            id_producto = int(input("\nID del producto: "))
            producto = self.producto_dao.buscar_por_id(id_producto)
            
            if producto:
                print(f"\nProducto: {producto.nombre}")
                confirmar = input("Confirmar eliminación? (s/n): ")
                
                if confirmar.lower() == 's':
                    if self.producto_dao.eliminar(id_producto):
                        print("\nProducto eliminado")
                        self.registrar_accion(f"Producto eliminado: {producto.nombre}")
                    else:
                        print("\nError al eliminar")
            else:
                print("\nProducto no encontrado")
            
            self.pausar()
            
        except ValueError:
            print("\nID inválido")
            self.pausar()
        except Exception as e:
            logger.error(f"Error al eliminar producto: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def ver_clientes(self):
        """Lista clientes ordenados"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("              LISTA DE CLIENTES")
            print("="*70)
            
            clientes = self.cliente_dao.listar()
            
            if clientes:
                # Ordenar clientes alfabéticamente
                clientes_ordenados = ordenar_clientes_por_nombre(clientes, algoritmo='quick')
                
                print(f"\n{'ID':<5} {'Nombre':<25} {'Teléfono':<15} {'Email':<25}")
                print("-"*70)
                for c in clientes_ordenados:
                    nombre_completo = f"{c.nombre} {c.apellido}"
                    print(f"{c.id_cliente:<5} {nombre_completo:<25} {c.telefono:<15} {c.email:<25}")
                print(f"\nTotal clientes: {len(clientes)}")
            else:
                print("\nNo hay clientes registrados")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al ver clientes: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def buscar_clientes(self):
        """Busca clientes por nombre"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("              BUSCAR CLIENTES")
            print("="*70)
            
            nombre = input("\nNombre a buscar: ")
            clientes = self.cliente_dao.listar()
            
            # Búsqueda secuencial
            resultados = AlgoritmosBusqueda.busqueda_secuencial_multiple(
                clientes,
                nombre,
                clave=lambda c: f"{c.nombre} {c.apellido}"
            )
            
            if resultados:
                print(f"\nEncontrados {len(resultados)} clientes:")
                print(f"\n{'ID':<5} {'Nombre':<25} {'Teléfono':<15}")
                print("-"*45)
                for _, c in resultados:
                    nombre_completo = f"{c.nombre} {c.apellido}"
                    print(f"{c.id_cliente:<5} {nombre_completo:<25} {c.telefono:<15}")
            else:
                print(f"\nNo se encontraron clientes con '{nombre}'")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al buscar clientes: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def procesar_pedido(self):
        """Procesa el siguiente pedido en la cola (FIFO)"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           PROCESAR PEDIDO (Cola FIFO)")
            print("="*70)
            
            if self.cola_pedidos.esta_vacia():
                print("\nNo hay pedidos pendientes")
                self.pausar()
                return
            
            # Desencolar (procesar el primero en entrar)
            pedido = self.cola_pedidos.desencolar()
            
            print("\nProcesando pedido:")
            print(f"\nCliente: {pedido['cliente']['nombre']}")
            print(f"Teléfono: {pedido['cliente']['telefono']}")
            print(f"Dirección: {pedido['cliente']['direccion']}")
            print(f"Fecha: {pedido['fecha']}")
            print(f"\nTotal: Q{pedido['total']:.2f}")
            
            print("\nItems:")
            for item in pedido['items']:
                print(f"  - {item['producto'].nombre} x{item['cantidad']} = Q{item['subtotal']:.2f}")
            
            print(f"\nPedidos restantes en cola: {self.cola_pedidos.tamano()}")
            
            confirmar = input("\nMarcar como procesado? (s/n): ")
            
            if confirmar.lower() == 's':
                print("\nPedido procesado exitosamente")
                self.registrar_accion(f"Pedido procesado - Cliente: {pedido['cliente']['nombre']}")
            else:
                # Volver a encolar
                self.cola_pedidos.encolar(pedido)
                print("\nPedido devuelto a la cola")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al procesar pedido: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def reporte_ventas_matriz(self):
        """Reporte de ventas usando matriz bidimensional"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("         REPORTE DE VENTAS (Matriz 2D)")
            print("="*70)
            
            print("\nSimulación de ventas por producto y mes")
            print("(Matriz bidimensional: Productos x Meses)")
            
            # Simular algunos datos de ejemplo
            import random
            productos = self.producto_dao.listar()[:10]
            
            if not productos:
                print("\nNo hay productos para reportar")
                self.pausar()
                return
            
            # Generar datos aleatorios para demostración
            for i, producto in enumerate(productos):
                for mes in range(12):
                    cantidad = random.randint(0, 20)
                    self.matriz_ventas.registrar_venta(i, mes, cantidad)
            
            print(f"\n{'Producto':<30} {'Total Ventas':<15} {'Mes Mayor':<15}")
            print("-"*60)
            
            meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 
                     'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
            
            for i, producto in enumerate(productos):
                total = self.matriz_ventas.total_ventas_producto(i)
                ventas_mensuales = self.matriz_ventas.obtener_ventas_producto(i)
                mes_mayor = ventas_mensuales.index(max(ventas_mensuales))
                
                nombre_corto = producto.nombre[:30]
                print(f"{nombre_corto:<30} {total:<15} {meses[mes_mayor]:<15}")
            
            # Producto más vendido
            prod_id, max_ventas = self.matriz_ventas.producto_mas_vendido()
            if prod_id >= 0:
                print(f"\nProducto más vendido: {productos[prod_id].nombre}")
                print(f"   Total: {max_ventas} unidades")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error en reporte de ventas: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def gestionar_usuarios(self):
        """Gestión de usuarios administradores"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("           GESTIÓN DE USUARIOS")
            print("="*70)
            
            usuarios = self.registro_usuario.listar_usuarios()
            
            print(f"\n{'ID':<5} {'Nombre':<25} {'Usuario':<15} {'Rol':<15}")
            print("-"*60)
            for u in usuarios:
                print(f"{u.id_admin:<5} {u.nombre:<25} {u.usuario:<15} {u.rol:<15}")
            
            print(f"\nTotal usuarios: {len(usuarios)}")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al gestionar usuarios: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def ver_estadisticas_cache(self):
        """Muestra estadísticas del caché de búsqueda"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("         ESTADÍSTICAS DE CACHÉ (Hashing)")
            print("="*70)
            
            stats = self.cache_busqueda.estadisticas()
            
            print("\nRendimiento del caché:")
            print(f"\nBúsquedas exitosas (hits): {stats['hits']}")
            print(f"Búsquedas fallidas (misses): {stats['misses']}")
            print(f"Total de búsquedas: {stats['total']}")
            print(f"Tasa de acierto: {stats['tasa_acierto']:.2f}%")
            print(f"Elementos en caché: {stats['elementos']}")
            
            print("\nVentajas del Hashing:")
            print("  - Búsqueda en tiempo O(1) constante")
            print("  - Mejora significativa en búsquedas repetidas")
            print("  - Reduce carga en la base de datos")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al ver estadísticas de caché: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def mostrar_estadisticas_sistema(self):
        """Estadísticas generales del sistema"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("         ESTADÍSTICAS DEL SISTEMA")
            print("="*70)
            
            print("\nESTRUCTURAS DE DATOS IMPLEMENTADAS:")
            print(f"\n  Pila (Stack):")
            print(f"    - Acciones en historial: {self.historial_acciones.tamano()}")
            
            print(f"\n  Cola (Queue):")
            print(f"    - Pedidos pendientes: {self.cola_pedidos.tamano()}")
            
            print(f"\n  Lista Enlazada:")
            print(f"    - Items en carrito actual: {len(self.carrito)}")
            
            print(f"\n  Tabla Hash:")
            print(f"    - Factor de carga: {self.cache_productos.factor_carga():.2%}")
            print(f"    - Elementos: {self.cache_productos.num_elementos}")
            
            stats_cache = self.cache_busqueda.estadisticas()
            print(f"\n  Caché de Búsqueda:")
            print(f"    - Tasa de acierto: {stats_cache['tasa_acierto']:.2f}%")
            print(f"    - Total búsquedas: {stats_cache['total']}")
            
            print(f"\nOPERACIONES REALIZADAS:")
            print(f"  - Búsquedas: {self.contador_busquedas}")
            print(f"  - Ordenamientos: {self.contador_ordenamientos}")
            
            print("\nALGORITMOS IMPLEMENTADOS:")
            print("  Ordenamiento: Bubble, Selection, Shell, Quick, Bogo Sort")
            print("  Búsqueda: Secuencial, Binaria, Hashing")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al mostrar estadísticas: {e}")
            print(f"\nError: {e}")
            self.pausar()
    
    def registrar_usuario(self):
        """Registra nuevo usuario administrador"""
        try:
            self.limpiar_pantalla()
            print("="*70)
            print("        REGISTRAR NUEVO ADMINISTRADOR")
            print("="*70)
            
            nombre = input("\nNombre completo: ")
            usuario = input("Nombre de usuario: ")
            password = input("Contraseña: ")
            
            print("\nRoles disponibles:")
            print("1. Administrador (acceso completo)")
            print("2. Vendedor (acceso limitado)")
            rol_opcion = input("Seleccione rol: ")
            
            rol = "administrador" if rol_opcion == "1" else "vendedor"
            
            admin = Administrador(None, nombre, usuario, password, rol)
            
            if self.registro_usuario.registrar(admin):
                print(f"\nUsuario '{usuario}' registrado exitosamente")
                print(f"  Rol asignado: {rol}")
                self.registrar_accion(f"Usuario registrado: {usuario}")
            else:
                print("\nError al registrar el usuario")
            
            self.pausar()
            
        except Exception as e:
            logger.error(f"Error al registrar usuario: {e}")
            print(f"\nError: {e}")
            self.pausar()


# ==================== EJECUCIÓN PRINCIPAL ====================

def main():
    """Función principal del sistema"""
    try:
        print("\n" + "="*70)
        print("         Iniciando Creative Designs...")
        print("="*70)
        print("\nSistema implementando:")
        print("  - Estructuras de datos lineales (Pila, Cola, Lista Enlazada)")
        print("  - Tabla Hash para búsquedas O(1)")
        print("  - Arreglos multidimensionales (Matriz de ventas)")
        print("  - 5 Algoritmos de ordenamiento")
        print("  - Búsqueda secuencial, binaria y hashing")
        print("  - Recursividad e iteración")
        print("  - Manejo de punteros (referencias)")
        
        input("\nPresione Enter para continuar...")
        
        sistema = SistemaCreativeDesigns()
        sistema.menu_principal()
        
    except KeyboardInterrupt:
        print("\n\nSistema interrumpido por el usuario")
        logger.info("Sistema cerrado por interrupción")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Error crítico en main: {e}")
        print(f"\nError crítico: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()