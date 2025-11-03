"""
MODELO CLIENTE - Creative Designs
Clase completa que representa un cliente del sistema

Autor: Creative Designs Team
Fecha: 2025
Descripción: Modelo de datos para clientes con validaciones y manejo de errores
"""

import re
import logging
from datetime import datetime
from typing import Optional, Tuple, Dict, List

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ClienteException(Exception):
    """Excepción personalizada para errores relacionados con Cliente"""
    pass


class Cliente:
    """
    Clase Cliente - Representa un cliente en el sistema
    
    Atributos:
        id_cliente (int): Identificador único del cliente
        nombre (str): Nombre del cliente
        apellido (str): Apellido del cliente
        telefono (str): Número telefónico
        email (str): Correo electrónico
        direccion (str): Dirección física
        fecha_registro (datetime): Fecha de registro en el sistema
    """
    
    def __init__(self, id_cliente=None, nombre="", apellido="", telefono="", email="", direccion=""):
        """
        Constructor de la clase Cliente
        
        Args:
            id_cliente (int, optional): ID único del cliente
            nombre (str): Nombre del cliente
            apellido (str): Apellido del cliente
            telefono (str): Número de teléfono
            email (str): Correo electrónico
            direccion (str): Dirección del cliente
            
        Raises:
            ClienteException: Si hay error al crear el cliente
        """
        try:
            self.id_cliente = id_cliente
            self.nombre = nombre.strip() if nombre else ""
            self.apellido = apellido.strip() if apellido else ""
            self.telefono = telefono.strip() if telefono else ""
            self.email = email.strip().lower() if email else ""
            self.direccion = direccion.strip() if direccion else ""
            self.fecha_registro = datetime.now()
        except Exception as e:
            logger.error(f"Error al crear Cliente: {e}")
            raise ClienteException(f"No se pudo crear el cliente: {str(e)}")
    
    # ==================== MÉTODOS MÁGICOS ====================
    
    def __str__(self):
        """Representación en string del cliente"""
        try:
            return f"Cliente({self.id_cliente}, {self.nombre} {self.apellido}, {self.telefono}, {self.email})"
        except Exception as e:
            logger.error(f"Error en __str__: {e}")
            return f"Cliente(Error: {str(e)})"
    
    def __repr__(self):
        """Representación oficial del objeto"""
        try:
            return f"Cliente(id={self.id_cliente}, nombre='{self.nombre}', apellido='{self.apellido}')"
        except Exception as e:
            return f"Cliente(Error)"
    
    def __eq__(self, otro):
        """Comparación de igualdad entre clientes"""
        try:
            if not isinstance(otro, Cliente):
                return False
            return self.id_cliente == otro.id_cliente
        except Exception as e:
            logger.error(f"Error en comparación: {e}")
            return False
    
    def __lt__(self, otro):
        """Comparación menor que (para ordenamiento)"""
        try:
            if not isinstance(otro, Cliente):
                return NotImplemented
            return self.nombre_completo().lower() < otro.nombre_completo().lower()
        except Exception as e:
            logger.error(f"Error en comparación menor que: {e}")
            return NotImplemented
    
    def __hash__(self):
        """Función hash para usar en sets y diccionarios"""
        try:
            return hash(self.id_cliente) if self.id_cliente else hash(id(self))
        except Exception as e:
            logger.error(f"Error en hash: {e}")
            return 0
    
    # ==================== MÉTODOS DE ACCESO ====================
    
    def nombre_completo(self) -> str:
        """
        Retorna el nombre completo del cliente
        
        Returns:
            str: Nombre y apellido concatenados
        """
        try:
            return f"{self.nombre} {self.apellido}".strip()
        except Exception as e:
            logger.error(f"Error al obtener nombre completo: {e}")
            return ""
    
    def iniciales(self) -> str:
        """
        Retorna las iniciales del cliente
        
        Returns:
            str: Iniciales en mayúsculas
        """
        try:
            inicial_nombre = self.nombre[0].upper() if self.nombre else ""
            inicial_apellido = self.apellido[0].upper() if self.apellido else ""
            return f"{inicial_nombre}{inicial_apellido}"
        except Exception as e:
            logger.error(f"Error al obtener iniciales: {e}")
            return ""
    
    def edad_registro(self) -> int:
        """
        Calcula cuántos días tiene registrado el cliente
        
        Returns:
            int: Días desde el registro
        """
        try:
            diferencia = datetime.now() - self.fecha_registro
            return diferencia.days
        except Exception as e:
            logger.error(f"Error al calcular edad de registro: {e}")
            return 0
    
    # ==================== VALIDACIONES ====================
    
    def validar_nombre(self) -> Tuple[bool, str]:
        """
        Valida que el nombre sea válido
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        try:
            if not self.nombre or self.nombre.strip() == "":
                return False, "El nombre no puede estar vacío"
            
            if len(self.nombre) < 2:
                return False, "El nombre debe tener al menos 2 caracteres"
            
            if len(self.nombre) > 100:
                return False, "El nombre no puede exceder 100 caracteres"
            
            if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", self.nombre):
                return False, "El nombre solo puede contener letras y espacios"
            
            return True, "Nombre válido"
            
        except Exception as e:
            logger.error(f"Error al validar nombre: {e}")
            return False, f"Error en validación: {str(e)}"
    
    def validar_apellido(self) -> Tuple[bool, str]:
        """
        Valida que el apellido sea válido
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        try:
            if not self.apellido or self.apellido.strip() == "":
                return False, "El apellido no puede estar vacío"
            
            if len(self.apellido) < 2:
                return False, "El apellido debe tener al menos 2 caracteres"
            
            if len(self.apellido) > 100:
                return False, "El apellido no puede exceder 100 caracteres"
            
            if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", self.apellido):
                return False, "El apellido solo puede contener letras y espacios"
            
            return True, "Apellido válido"
            
        except Exception as e:
            logger.error(f"Error al validar apellido: {e}")
            return False, f"Error en validación: {str(e)}"
    
    def validar_telefono(self) -> Tuple[bool, str]:
        """
        Valida que el teléfono sea válido (formato Guatemala: 8 dígitos)
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        try:
            if not self.telefono or self.telefono.strip() == "":
                return False, "El teléfono no puede estar vacío"
            
            # Limpiar teléfono (quitar espacios, guiones, paréntesis)
            telefono_limpio = re.sub(r'[\s\-\(\)]', '', self.telefono)
            
            # Validar formato Guatemala: 8 dígitos
            if not re.match(r'^[0-9]{8}$', telefono_limpio):
                return False, "El teléfono debe tener 8 dígitos (formato Guatemala)"
            
            return True, "Teléfono válido"
            
        except Exception as e:
            logger.error(f"Error al validar teléfono: {e}")
            return False, f"Error en validación: {str(e)}"
    
    def validar_email(self) -> Tuple[bool, str]:
        """
        Valida que el email sea válido
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        try:
            if not self.email or self.email.strip() == "":
                return False, "El email no puede estar vacío"
            
            # Patrón regex para email
            patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            
            if not re.match(patron_email, self.email):
                return False, "El formato del email no es válido"
            
            if len(self.email) > 100:
                return False, "El email no puede exceder 100 caracteres"
            
            return True, "Email válido"
            
        except Exception as e:
            logger.error(f"Error al validar email: {e}")
            return False, f"Error en validación: {str(e)}"
    
    def validar_direccion(self) -> Tuple[bool, str]:
        """
        Valida que la dirección sea válida
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        try:
            if not self.direccion or self.direccion.strip() == "":
                return False, "La dirección no puede estar vacía"
            
            if len(self.direccion) < 10:
                return False, "La dirección debe tener al menos 10 caracteres"
            
            if len(self.direccion) > 255:
                return False, "La dirección no puede exceder 255 caracteres"
            
            return True, "Dirección válida"
            
        except Exception as e:
            logger.error(f"Error al validar dirección: {e}")
            return False, f"Error en validación: {str(e)}"
    
    def validar_completo(self) -> Tuple[bool, List[str]]:
        """
        Valida todos los campos del cliente
        
        Returns:
            tuple: (bool, list) - (es_valido, lista_errores)
        """
        errores = []
        
        try:
            # Validar nombre
            valido, mensaje = self.validar_nombre()
            if not valido:
                errores.append(f"Nombre: {mensaje}")
            
            # Validar apellido
            valido, mensaje = self.validar_apellido()
            if not valido:
                errores.append(f"Apellido: {mensaje}")
            
            # Validar teléfono
            valido, mensaje = self.validar_telefono()
            if not valido:
                errores.append(f"Teléfono: {mensaje}")
            
            # Validar email
            valido, mensaje = self.validar_email()
            if not valido:
                errores.append(f"Email: {mensaje}")
            
            # Validar dirección
            valido, mensaje = self.validar_direccion()
            if not valido:
                errores.append(f"Dirección: {mensaje}")
            
            return len(errores) == 0, errores
            
        except Exception as e:
            logger.error(f"Error en validación completa: {e}")
            errores.append(f"Error general: {str(e)}")
            return False, errores
    
    # ==================== MÉTODOS DE UTILIDAD ====================
    
    def to_dict(self) -> Dict:
        """
        Convierte el objeto Cliente a diccionario
        
        Returns:
            dict: Diccionario con todos los atributos del cliente
        """
        try:
            return {
                'id_cliente': self.id_cliente,
                'nombre': self.nombre,
                'apellido': self.apellido,
                'telefono': self.telefono,
                'email': self.email,
                'direccion': self.direccion,
                'nombre_completo': self.nombre_completo(),
                'fecha_registro': self.fecha_registro.strftime("%Y-%m-%d %H:%M:%S") if self.fecha_registro else None
            }
        except Exception as e:
            logger.error(f"Error al convertir a diccionario: {e}")
            return {}
    
    @classmethod
    def desde_dict(cls, datos: Dict) -> Optional['Cliente']:
        """
        Crea un objeto Cliente desde un diccionario
        
        Args:
            datos (dict): Diccionario con los datos del cliente
            
        Returns:
            Cliente: Nueva instancia de Cliente o None si hay error
        """
        try:
            return cls(
                id_cliente=datos.get('id_cliente'),
                nombre=datos.get('nombre', ''),
                apellido=datos.get('apellido', ''),
                telefono=datos.get('telefono', ''),
                email=datos.get('email', ''),
                direccion=datos.get('direccion', '')
            )
        except Exception as e:
            logger.error(f"Error al crear desde diccionario: {e}")
            return None
    
    def formatear_telefono(self) -> str:
        """
        Formatea el teléfono en un formato legible (XXXX-XXXX)
        
        Returns:
            str: Teléfono formateado
        """
        try:
            telefono_limpio = re.sub(r'[\s\-\(\)]', '', self.telefono)
            if len(telefono_limpio) == 8:
                return f"{telefono_limpio[:4]}-{telefono_limpio[4:]}"
            return self.telefono
        except Exception as e:
            logger.error(f"Error al formatear teléfono: {e}")
            return self.telefono
    
    def dominio_email(self) -> str:
        """
        Extrae el dominio del email
        
        Returns:
            str: Dominio del email
        """
        try:
            if '@' in self.email:
                return self.email.split('@')[1]
            return ""
        except Exception as e:
            logger.error(f"Error al extraer dominio: {e}")
            return ""
    
    def info_completa(self) -> str:
        """
        Retorna información completa del cliente en formato legible
        
        Returns:
            str: Información completa formateada
        """
        try:
            info = f"""
{'='*60}
INFORMACIÓN DEL CLIENTE
{'='*60}
ID:              {self.id_cliente or 'N/A'}
Nombre:          {self.nombre_completo()}
Teléfono:        {self.formatear_telefono()}
Email:           {self.email}
Dirección:       {self.direccion}
Registro:        {self.fecha_registro.strftime("%d/%m/%Y") if self.fecha_registro else 'N/A'}
Días registrado: {self.edad_registro()}
{'='*60}
            """
            return info.strip()
        except Exception as e:
            logger.error(f"Error al generar información completa: {e}")
            return f"Error al mostrar información: {str(e)}"
    
    def resumen_corto(self) -> str:
        """
        Retorna un resumen corto del cliente
        
        Returns:
            str: Resumen en una línea
        """
        try:
            return f"{self.nombre_completo()} | {self.formatear_telefono()} | {self.email}"
        except Exception as e:
            logger.error(f"Error al generar resumen: {e}")
            return "Error en resumen"
    
    # ==================== MÉTODOS ESTÁTICOS ====================
    
    @staticmethod
    def crear_vacio() -> 'Cliente':
        """
        Crea un cliente vacío
        
        Returns:
            Cliente: Instancia de cliente con valores por defecto
        """
        try:
            return Cliente()
        except Exception as e:
            logger.error(f"Error al crear cliente vacío: {e}")
            raise ClienteException(f"No se pudo crear cliente vacío: {str(e)}")
    
    @staticmethod
    def validar_formato_telefono(telefono: str) -> bool:
        """
        Valida el formato de un teléfono sin crear un objeto Cliente
        
        Args:
            telefono (str): Número de teléfono a validar
            
        Returns:
            bool: True si el formato es válido
        """
        try:
            if not telefono:
                return False
            telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono)
            return bool(re.match(r'^[0-9]{8}$', telefono_limpio))
        except Exception as e:
            logger.error(f"Error al validar formato de teléfono: {e}")
            return False
    
    @staticmethod
    def validar_formato_email(email: str) -> bool:
        """
        Valida el formato de un email sin crear un objeto Cliente
        
        Args:
            email (str): Email a validar
            
        Returns:
            bool: True si el formato es válido
        """
        try:
            if not email:
                return False
            patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
            return bool(re.match(patron_email, email))
        except Exception as e:
            logger.error(f"Error al validar formato de email: {e}")
            return False
    
    @staticmethod
    def comparar_clientes(cliente1: 'Cliente', cliente2: 'Cliente', criterio: str = 'nombre') -> int:
        """
        Compara dos clientes según un criterio
        
        Args:
            cliente1 (Cliente): Primer cliente
            cliente2 (Cliente): Segundo cliente
            criterio (str): 'nombre', 'apellido', 'email', 'telefono'
            
        Returns:
            int: -1 si cliente1 < cliente2, 0 si iguales, 1 si cliente1 > cliente2
        """
        try:
            if criterio == 'nombre':
                valor1 = cliente1.nombre.lower()
                valor2 = cliente2.nombre.lower()
            elif criterio == 'apellido':
                valor1 = cliente1.apellido.lower()
                valor2 = cliente2.apellido.lower()
            elif criterio == 'email':
                valor1 = cliente1.email.lower()
                valor2 = cliente2.email.lower()
            elif criterio == 'telefono':
                valor1 = cliente1.telefono
                valor2 = cliente2.telefono
            else:
                valor1 = cliente1.nombre_completo().lower()
                valor2 = cliente2.nombre_completo().lower()
            
            if valor1 < valor2:
                return -1
            elif valor1 > valor2:
                return 1
            else:
                return 0
                
        except Exception as e:
            logger.error(f"Error al comparar clientes: {e}")
            return 0
    
    # ==================== MÉTODOS DE CLASE ====================
    
    @classmethod
    def crear_desde_input(cls) -> Optional['Cliente']:
        """
        Crea un cliente solicitando los datos por teclado
        
        Returns:
            Cliente: Nueva instancia de Cliente con datos ingresados o None si hay error
        """
        try:
            print("\n" + "="*50)
            print("       REGISTRO DE NUEVO CLIENTE")
            print("="*50)
            
            nombre = input("\nNombre: ").strip()
            apellido = input("Apellido: ").strip()
            telefono = input("Teléfono (8 dígitos): ").strip()
            email = input("Email: ").strip()
            direccion = input("Dirección: ").strip()
            
            cliente = cls(
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                email=email,
                direccion=direccion
            )
            
            # Validar
            valido, errores = cliente.validar_completo()
            
            if not valido:
                print("\nERRORES EN LOS DATOS:")
                for error in errores:
                    print(f"  - {error}")
                return None
            
            print("\nCliente creado exitosamente")
            return cliente
            
        except Exception as e:
            logger.error(f"Error al crear cliente desde input: {e}")
            print(f"\nError al crear cliente: {str(e)}")
            return None


# ==================== FUNCIONES AUXILIARES ====================

def ordenar_clientes_por_nombre(clientes: List[Cliente]) -> List[Cliente]:
    """
    Ordena una lista de clientes alfabéticamente por nombre completo
    
    Args:
        clientes (list): Lista de objetos Cliente
        
    Returns:
        list: Lista ordenada de clientes
    """
    try:
        return sorted(clientes, key=lambda c: c.nombre_completo().lower())
    except Exception as e:
        logger.error(f"Error al ordenar clientes: {e}")
        return clientes


def ordenar_clientes_por_apellido(clientes: List[Cliente]) -> List[Cliente]:
    """
    Ordena una lista de clientes alfabéticamente por apellido
    
    Args:
        clientes (list): Lista de objetos Cliente
        
    Returns:
        list: Lista ordenada de clientes
    """
    try:
        return sorted(clientes, key=lambda c: c.apellido.lower())
    except Exception as e:
        logger.error(f"Error al ordenar por apellido: {e}")
        return clientes


def buscar_cliente_por_nombre(clientes: List[Cliente], nombre_buscar: str) -> List[Cliente]:
    """
    Busca clientes cuyo nombre contenga el texto buscado
    
    Args:
        clientes (list): Lista de clientes
        nombre_buscar (str): Texto a buscar
        
    Returns:
        list: Lista de clientes que coinciden
    """
    try:
        resultados = []
        nombre_buscar = nombre_buscar.lower()
        
        for cliente in clientes:
            if nombre_buscar in cliente.nombre_completo().lower():
                resultados.append(cliente)
        
        return resultados
    except Exception as e:
        logger.error(f"Error al buscar cliente: {e}")
        return []


def filtrar_por_dominio_email(clientes: List[Cliente], dominio: str) -> List[Cliente]:
    """
    Filtra clientes por dominio de email
    
    Args:
        clientes (list): Lista de clientes
        dominio (str): Dominio a buscar
        
    Returns:
        list: Clientes con ese dominio
    """
    try:
        return [c for c in clientes if dominio.lower() in c.email.lower()]
    except Exception as e:
        logger.error(f"Error al filtrar por dominio: {e}")
        return []


def estadisticas_clientes(clientes: List[Cliente]) -> Dict:
    """
    Genera estadísticas sobre una lista de clientes
    
    Args:
        clientes (list): Lista de clientes
        
    Returns:
        dict: Diccionario con estadísticas
    """
    try:
        if not clientes:
            return {
                'total': 0,
                'dominios_email': {},
                'promedio_dias_registro': 0
            }
        
        dominios = {}
        total_dias = 0
        
        for cliente in clientes:
            try:
                dominio = cliente.dominio_email()
                dominios[dominio] = dominios.get(dominio, 0) + 1
                total_dias += cliente.edad_registro()
            except:
                continue
        
        return {
            'total': len(clientes),
            'dominios_email': dominios,
            'promedio_dias_registro': total_dias / len(clientes) if clientes else 0
        }
    except Exception as e:
        logger.error(f"Error al generar estadísticas: {e}")
        return {'total': 0, 'dominios_email': {}, 'promedio_dias_registro': 0}