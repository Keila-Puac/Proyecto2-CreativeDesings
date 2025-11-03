"""
CLIENTE DAO - Creative Designs
Data Access Object para la gestión de clientes en la base de datos

Autor: Creative Designs Team
Fecha: 2025
Descripción: Capa de acceso a datos con manejo robusto de errores y transacciones
"""

import sys
import logging
from typing import List, Optional, Tuple, Dict

# Configurar carpeta padre para imports
sys.path.append('..')

try:
    from Data.conexion import Conexion
    from Cliente import Cliente
except ImportError as e:
    print(f"Error al importar módulos: {e}")
    print("Asegúrese de que los archivos conexion.py y Cliente.py existan")
    sys.exit(1)

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ClienteDAOException(Exception):
    """Excepción personalizada para errores del DAO"""
    pass


class ClienteDAO:
    """
    Data Access Object para Cliente
    Maneja todas las operaciones CRUD con la base de datos
    
    Métodos principales:
        - listar(): Obtiene todos los clientes
        - buscar_por_id(): Busca un cliente por ID
        - buscar_por_nombre(): Busca clientes por nombre
        - buscar_por_email(): Busca cliente por email
        - buscar_por_telefono(): Busca cliente por teléfono
        - insertar(): Inserta un nuevo cliente
        - actualizar(): Actualiza un cliente existente
        - eliminar(): Elimina un cliente
        - existe_email(): Verifica si un email ya existe
        - contar(): Cuenta el total de clientes
        - buscar_avanzada(): Búsqueda con múltiples criterios
        - listar_paginado(): Lista con paginación
    """
    
    def __init__(self):
        """Inicializa el DAO con la conexión a la base de datos"""
        try:
            self.conexion = Conexion()
            logger.info("ClienteDAO inicializado correctamente")
        except Exception as e:
            logger.error(f"Error al inicializar ClienteDAO: {e}")
            raise ClienteDAOException(f"No se pudo inicializar ClienteDAO: {e}")
    
    # ==================== MÉTODOS DE LECTURA ====================
    
    def listar(self) -> List[Cliente]:
        """
        Obtiene todos los clientes de la base de datos
        
        Returns:
            List[Cliente]: Lista de todos los clientes
            
        Raises:
            ClienteDAOException: Si ocurre un error en la consulta
        """
        clientes = []
        conn = None
        cursor = None
        
        try:
            conn = self.conexion.conectar()
            if not conn:
                raise ClienteDAOException("No se pudo establecer conexión con la base de datos")
            
            cursor = conn.cursor()
            sql = """
                SELECT id_cliente, nombre, apellido, telefono, email, direccion 
                FROM clientes 
                ORDER BY nombre, apellido
            """
            
            cursor.execute(sql)
            resultados = cursor.fetchall()
            
            logger.info(f"Se obtuvieron {len(resultados)} clientes de la base de datos")
            
            for row in resultados:
                try:
                    cliente = Cliente(
                        id_cliente=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        telefono=row[3],
                        email=row[4],
                        direccion=row[5]
                    )
                    clientes.append(cliente)
                except Exception as e:
                    logger.warning(f"Error al crear objeto Cliente desde fila {row[0]}: {e}")
                    continue
            
            return clientes
            
        except Exception as e:
            logger.error(f"Error al listar clientes: {e}")
            raise ClienteDAOException(f"Error al obtener lista de clientes: {e}")
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    def buscar_por_id(self, id_cliente: int) -> Optional[Cliente]:
        """
        Busca un cliente por su ID
        
        Args:
            id_cliente (int): ID del cliente a buscar
            
        Returns:
            Optional[Cliente]: Cliente encontrado o None
            
        Raises:
            ClienteDAOException: Si ocurre un error en la consulta
            ValueError: Si el ID no es válido
        """
        if not id_cliente or not isinstance(id_cliente, int) or id_cliente <= 0:
            raise ValueError("El ID del cliente debe ser un entero positivo")
        
        conn = None
        cursor = None
        
        try:
            conn = self.conexion.conectar()
            if not conn:
                raise ClienteDAOException("No se pudo establecer conexión con la base de datos")
            
            cursor = conn.cursor()
            sql = """
                SELECT id_cliente, nombre, apellido, telefono, email, direccion 
                FROM clientes 
                WHERE id_cliente = %s
            """
            
            cursor.execute(sql, (id_cliente,))
            row = cursor.fetchone()
            
            if row:
                logger.info(f"Cliente con ID {id_cliente} encontrado")
                return Cliente(
                    id_cliente=row[0],
                    nombre=row[1],
                    apellido=row[2],
                    telefono=row[3],
                    email=row[4],
                    direccion=row[5]
                )
            else:
                logger.info(f"No se encontró cliente con ID {id_cliente}")
                return None
                
        except ValueError as e:
            raise e
        except Exception as e:
            logger.error(f"Error al buscar cliente por ID {id_cliente}: {e}")
            raise ClienteDAOException(f"Error al buscar cliente: {e}")
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    def buscar_por_nombre(self, nombre: str) -> List[Cliente]:
        """
        Busca clientes cuyo nombre o apellido contenga el texto especificado
        
        Args:
            nombre (str): Texto a buscar en nombre o apellido
            
        Returns:
            List[Cliente]: Lista de clientes que coinciden con la búsqueda
            
        Raises:
            ClienteDAOException: Si ocurre un error en la consulta
        """
        if not nombre or not isinstance(nombre, str):
            return []
        
        clientes = []
        conn = None
        cursor = None
        
        try:
            conn = self.conexion.conectar()
            if not conn:
                raise ClienteDAOException("No se pudo establecer conexión con la base de datos")
            
            cursor = conn.cursor()
            sql = """
                SELECT id_cliente, nombre, apellido, telefono, email, direccion 
                FROM clientes 
                WHERE nombre LIKE %s OR apellido LIKE %s
                ORDER BY nombre, apellido
            """
            
            patron = f"%{nombre.strip()}%"
            cursor.execute(sql, (patron, patron))
            resultados = cursor.fetchall()
            
            logger.info(f"Búsqueda de '{nombre}': {len(resultados)} resultados")
            
            for row in resultados:
                try:
                    cliente = Cliente(
                        id_cliente=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        telefono=row[3],
                        email=row[4],
                        direccion=row[5]
                    )
                    clientes.append(cliente)
                except Exception as e:
                    logger.warning(f"Error al crear cliente desde búsqueda: {e}")
                    continue
            
            return clientes
            
        except Exception as e:
            logger.error(f"Error al buscar clientes por nombre '{nombre}': {e}")
            raise ClienteDAOException(f"Error en búsqueda por nombre: {e}")
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    def buscar_por_email(self, email: str) -> Optional[Cliente]:
        """
        Busca un cliente por su email (único)
        
        Args:
            email (str): Email del cliente
            
        Returns:
            Optional[Cliente]: Cliente encontrado o None
        """
        if not email or not isinstance(email, str):
            return None
        
        conn = None
        cursor = None
        
        try:
            conn = self.conexion.conectar()
            if not conn:
                raise ClienteDAOException("No se pudo establecer conexión")
            
            cursor = conn.cursor()
            sql = """
                SELECT id_cliente, nombre, apellido, telefono, email, direccion 
                FROM clientes 
                WHERE email = %s
            """
            
            cursor.execute(sql, (email.strip().lower(),))
            row = cursor.fetchone()
            
            if row:
                return Cliente(
                    id_cliente=row[0],
                    nombre=row[1],
                    apellido=row[2],
                    telefono=row[3],
                    email=row[4],
                    direccion=row[5]
                )
            return None
            
        except Exception as e:
            logger.error(f"Error al buscar por email: {e}")
            return None
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    def buscar_por_telefono(self, telefono: str) -> List[Cliente]:
        """
        Busca clientes por teléfono
        
        Args:
            telefono (str): Teléfono a buscar
            
        Returns:
            List[Cliente]: Lista de clientes con ese teléfono
        """
        if not telefono:
            return []
        
        clientes = []
        conn = None
        cursor = None
        
        try:
            conn = self.conexion.conectar()
            if not conn:
                return []
            
            cursor = conn.cursor()
            sql = """
                SELECT id_cliente, nombre, apellido, telefono, email, direccion 
                FROM clientes 
                WHERE telefono LIKE %s
            """
            
            patron = f"%{telefono}%"
            cursor.execute(sql, (patron,))
            resultados = cursor.fetchall()
            
            for row in resultados:
                try:
                    cliente = Cliente(
                        id_cliente=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        telefono=row[3],
                        email=row[4],
                        direccion=row[5]
                    )
                    clientes.append(cliente)
                except:
                    continue
            
            return clientes
            
        except Exception as e:
            logger.error(f"Error al buscar por teléfono: {e}")
            return []
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    # ==================== MÉTODOS DE ESCRITURA ====================
    
    def insertar(self, cliente: Cliente) -> Tuple[bool, str]:
        """
        Inserta un nuevo cliente en la base de datos
        
        Args:
            cliente (Cliente): Objeto cliente a insertar
            
        Returns:
            Tuple[bool, str]: (éxito, mensaje)
            
        Raises:
            ClienteDAOException: Si ocurre un error en la inserción
        """
        if not isinstance(cliente, Cliente):
            return False, "El objeto no es una instancia válida de Cliente"
        
        # Validar datos del cliente
        valido, errores = cliente.validar_completo()
        if not valido:
            return False, f"Datos inválidos: {', '.join(errores)}"
        
        conn = None
        cursor = None
        
        try:
            # Verificar si el email ya existe
            if self.existe_email(cliente.email):
                return False, f"El email {cliente.email} ya está registrado"
            
            conn = self.conexion.conectar()
            if not conn:
                raise ClienteDAOException("No se pudo establecer conexión")
            
            cursor = conn.cursor()
            sql = """
                INSERT INTO clientes (nombre, apellido, telefono, email, direccion) 
                VALUES (%s, %s, %s, %s, %s)
            """
            
            valores = (
                cliente.nombre,
                cliente.apellido,
                cliente.telefono,
                cliente.email.lower(),
                cliente.direccion
            )
            
            cursor.execute(sql, valores)
            conn.commit()
            
            # Obtener el ID generado
            cliente.id_cliente = cursor.lastrowid
            
            logger.info(f"Cliente insertado exitosamente con ID {cliente.id_cliente}")
            return True, f"Cliente registrado con ID {cliente.id_cliente}"
            
        except Exception as e:
            if conn:
                try:
                    conn.rollback()
                except:
                    pass
            logger.error(f"Error al insertar cliente: {e}")
            return False, f"Error al registrar cliente: {str(e)}"
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    def actualizar(self, cliente: Cliente) -> Tuple[bool, str]:
        """
        Actualiza un cliente existente
        
        Args:
            cliente (Cliente): Cliente con datos actualizados
            
        Returns:
            Tuple[bool, str]: (éxito, mensaje)
        """
        if not isinstance(cliente, Cliente):
            return False, "El objeto no es una instancia válida de Cliente"
        
        if not cliente.id_cliente:
            return False, "El cliente debe tener un ID válido"
        
        # Validar datos
        valido, errores = cliente.validar_completo()
        if not valido:
            return False, f"Datos inválidos: {', '.join(errores)}"
        
        conn = None
        cursor = None
        
        try:
            # Verificar si el cliente existe
            cliente_existente = self.buscar_por_id(cliente.id_cliente)
            if not cliente_existente:
                return False, f"No existe cliente con ID {cliente.id_cliente}"
            
            # Verificar email único (excluyendo el mismo cliente)
            cliente_email = self.buscar_por_email(cliente.email)
            if cliente_email and cliente_email.id_cliente != cliente.id_cliente:
                return False, f"El email {cliente.email} ya está en uso por otro cliente"
            
            conn = self.conexion.conectar()
            if not conn:
                raise ClienteDAOException("No se pudo establecer conexión")
            
            cursor = conn.cursor()
            sql = """
                UPDATE clientes 
                SET nombre = %s, apellido = %s, telefono = %s, email = %s, direccion = %s
                WHERE id_cliente = %s
            """
            
            valores = (
                cliente.nombre,
                cliente.apellido,
                cliente.telefono,
                cliente.email.lower(),
                cliente.direccion,
                cliente.id_cliente
            )
            
            cursor.execute(sql, valores)
            conn.commit()
            
            if cursor.rowcount > 0:
                logger.info(f"Cliente {cliente.id_cliente} actualizado exitosamente")
                return True, "Cliente actualizado exitosamente"
            else:
                return False, "No se realizaron cambios"
                
        except Exception as e:
            if conn:
                try:
                    conn.rollback()
                except:
                    pass
            logger.error(f"Error al actualizar cliente: {e}")
            return False, f"Error al actualizar: {str(e)}"
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    def eliminar(self, id_cliente: int) -> Tuple[bool, str]:
        """
        Elimina un cliente de la base de datos
        
        Args:
            id_cliente (int): ID del cliente a eliminar
            
        Returns:
            Tuple[bool, str]: (éxito, mensaje)
        """
        if not id_cliente or not isinstance(id_cliente, int) or id_cliente <= 0:
            return False, "ID de cliente inválido"
        
        conn = None
        cursor = None
        
        try:
            # Verificar que existe
            cliente = self.buscar_por_id(id_cliente)
            if not cliente:
                return False, f"No existe cliente con ID {id_cliente}"
            
            conn = self.conexion.conectar()
            if not conn:
                raise ClienteDAOException("No se pudo establecer conexión")
            
            cursor = conn.cursor()
            sql = "DELETE FROM clientes WHERE id_cliente = %s"
            
            cursor.execute(sql, (id_cliente,))
            conn.commit()
            
            if cursor.rowcount > 0:
                logger.info(f"Cliente {id_cliente} eliminado exitosamente")
                return True, "Cliente eliminado exitosamente"
            else:
                return False, "No se pudo eliminar el cliente"
                
        except Exception as e:
            if conn:
                try:
                    conn.rollback()
                except:
                    pass
            logger.error(f"Error al eliminar cliente {id_cliente}: {e}")
            return False, f"Error al eliminar: {str(e)}"
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    # ==================== MÉTODOS AUXILIARES ====================
    
    def existe_email(self, email: str) -> bool:
        """
        Verifica si un email ya existe en la base de datos
        
        Args:
            email (str): Email a verificar
            
        Returns:
            bool: True si existe, False si no
        """
        try:
            cliente = self.buscar_por_email(email)
            return cliente is not None
        except Exception as e:
            logger.error(f"Error al verificar email: {e}")
            return False
    
    def contar(self) -> int:
        """
        Cuenta el total de clientes en la base de datos
        
        Returns:
            int: Número total de clientes
        """
        conn = None
        cursor = None
        
        try:
            conn = self.conexion.conectar()
            if not conn:
                return 0
            
            cursor = conn.cursor()
            sql = "SELECT COUNT(*) FROM clientes"
            cursor.execute(sql)
            resultado = cursor.fetchone()
            
            return resultado[0] if resultado else 0
            
        except Exception as e:
            logger.error(f"Error al contar clientes: {e}")
            return 0
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    def buscar_avanzada(self, nombre=None, telefono=None, email=None) -> List[Cliente]:
        """
        Búsqueda avanzada con múltiples criterios
        
        Args:
            nombre (str, optional): Nombre a buscar
            telefono (str, optional): Teléfono a buscar
            email (str, optional): Email a buscar
            
        Returns:
            List[Cliente]: Lista de clientes que coinciden
        """
        if not any([nombre, telefono, email]):
            return []
        
        clientes = []
        conn = None
        cursor = None
        
        try:
            conn = self.conexion.conectar()
            if not conn:
                return []
            
            condiciones = []
            valores = []
            
            sql_base = """
                SELECT id_cliente, nombre, apellido, telefono, email, direccion 
                FROM clientes WHERE 1=1
            """
            
            if nombre:
                condiciones.append("(nombre LIKE %s OR apellido LIKE %s)")
                patron = f"%{nombre}%"
                valores.extend([patron, patron])
            
            if telefono:
                condiciones.append("telefono LIKE %s")
                valores.append(f"%{telefono}%")
            
            if email:
                condiciones.append("email LIKE %s")
                valores.append(f"%{email}%")
            
            if condiciones:
                sql_base += " AND " + " AND ".join(condiciones)
            
            sql_base += " ORDER BY nombre, apellido"
            
            cursor = conn.cursor()
            cursor.execute(sql_base, tuple(valores))
            resultados = cursor.fetchall()
            
            for row in resultados:
                try:
                    cliente = Cliente(
                        id_cliente=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        telefono=row[3],
                        email=row[4],
                        direccion=row[5]
                    )
                    clientes.append(cliente)
                except:
                    continue
            
            return clientes
            
        except Exception as e:
            logger.error(f"Error en búsqueda avanzada: {e}")
            return []
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass
    
    def listar_paginado(self, pagina: int = 1, por_pagina: int = 10) -> Tuple[List[Cliente], int]:
        """
        Lista clientes con paginación
        
        Args:
            pagina (int): Número de página (inicia en 1)
            por_pagina (int): Cantidad de registros por página
            
        Returns:
            Tuple[List[Cliente], int]: (lista_clientes, total_paginas)
        """
        conn = None
        cursor = None
        
        try:
            # Calcular offset
            offset = (pagina - 1) * por_pagina
            
            conn = self.conexion.conectar()
            if not conn:
                return [], 0
            
            cursor = conn.cursor()
            
            # Contar total
            cursor.execute("SELECT COUNT(*) FROM clientes")
            total = cursor.fetchone()[0]
            total_paginas = (total + por_pagina - 1) // por_pagina
            
            # Obtener datos paginados
            sql = """
                SELECT id_cliente, nombre, apellido, telefono, email, direccion 
                FROM clientes 
                ORDER BY nombre, apellido
                LIMIT %s OFFSET %s
            """
            
            cursor.execute(sql, (por_pagina, offset))
            resultados = cursor.fetchall()
            
            clientes = []
            for row in resultados:
                try:
                    cliente = Cliente(
                        id_cliente=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        telefono=row[3],
                        email=row[4],
                        direccion=row[5]
                    )
                    clientes.append(cliente)
                except:
                    continue
            
            return clientes, total_paginas
            
        except Exception as e:
            logger.error(f"Error en paginación: {e}")
            return [], 0
            
        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            if conn:
                try:
                    self.conexion.desconectar()
                except:
                    pass