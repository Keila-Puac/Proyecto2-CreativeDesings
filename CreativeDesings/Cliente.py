"""
MODELO CLIENTE - Creative Designs
Clase completa que representa un cliente del sistema

Autor: Creative Designs Team
Fecha: 2025
Descripción: Modelo de datos para clientes con validaciones y métodos auxiliares
"""

import re
from datetime import datetime


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
    
    Almacenamiento en memoria:
        - Referencia al objeto: Stack
        - Datos del objeto: Heap
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
        """
        self.id_cliente = id_cliente
        self.nombre = nombre.strip()
        self.apellido = apellido.strip()
        self.telefono = telefono.strip()
        self.email = email.strip().lower()
        self.direccion = direccion.strip()
        self.fecha_registro = datetime.now()
    
    # ==================== MÉTODOS MÁGICOS ====================
    
    def __str__(self):
        """
        Representación en string del cliente
        Uso: print(cliente)
        """
        return f"Cliente({self.id_cliente}, {self.nombre} {self.apellido}, {self.telefono}, {self.email})"
    
    def __repr__(self):
        """
        Representación oficial del objeto
        Uso: En consola interactiva
        """
        return f"Cliente(id={self.id_cliente}, nombre='{self.nombre}', apellido='{self.apellido}')"
    
    def __eq__(self, otro):
        """
        Comparación de igualdad entre clientes
        Dos clientes son iguales si tienen el mismo ID
        
        Args:
            otro (Cliente): Otro cliente a comparar
            
        Returns:
            bool: True si son iguales, False si no
        """
        if not isinstance(otro, Cliente):
            return False
        return self.id_cliente == otro.id_cliente
    
    def __lt__(self, otro):
        """
        Comparación menor que (para ordenamiento)
        Compara por nombre completo alfabéticamente
        
        Args:
            otro (Cliente): Otro cliente a comparar
            
        Returns:
            bool: True si este cliente es "menor" que el otro
        """
        if not isinstance(otro, Cliente):
            return NotImplemented
        return self.nombre_completo().lower() < otro.nombre_completo().lower()
    
    def __hash__(self):
        """
        Función hash para poder usar en sets y diccionarios
        
        Returns:
            int: Hash del cliente basado en su ID
        """
        return hash(self.id_cliente)
    
    # ==================== MÉTODOS DE ACCESO ====================
    
    def nombre_completo(self):
        """
        Retorna el nombre completo del cliente
        
        Returns:
            str: Nombre y apellido concatenados
            
        Example:
            >>> cliente = Cliente(nombre="Juan", apellido="Pérez")
            >>> cliente.nombre_completo()
            'Juan Pérez'
        """
        return f"{self.nombre} {self.apellido}"
    
    def iniciales(self):
        """
        Retorna las iniciales del cliente
        
        Returns:
            str: Iniciales en mayúsculas
            
        Example:
            >>> cliente = Cliente(nombre="Juan", apellido="Pérez")
            >>> cliente.iniciales()
            'JP'
        """
        inicial_nombre = self.nombre[0].upper() if self.nombre else ""
        inicial_apellido = self.apellido[0].upper() if self.apellido else ""
        return f"{inicial_nombre}{inicial_apellido}"
    
    def edad_registro(self):
        """
        Calcula cuántos días tiene registrado el cliente
        
        Returns:
            int: Días desde el registro
        """
        diferencia = datetime.now() - self.fecha_registro
        return diferencia.days
    
    # ==================== VALIDACIONES ====================
    
    def validar_nombre(self):
        """
        Valida que el nombre sea válido
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        if not self.nombre or self.nombre.strip() == "":
            return False, "El nombre no puede estar vacío"
        
        if len(self.nombre) < 2:
            return False, "El nombre debe tener al menos 2 caracteres"
        
        if len(self.nombre) > 100:
            return False, "El nombre no puede exceder 100 caracteres"
        
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", self.nombre):
            return False, "El nombre solo puede contener letras y espacios"
        
        return True, "Nombre válido"
    
    def validar_apellido(self):
        """
        Valida que el apellido sea válido
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        if not self.apellido or self.apellido.strip() == "":
            return False, "El apellido no puede estar vacío"
        
        if len(self.apellido) < 2:
            return False, "El apellido debe tener al menos 2 caracteres"
        
        if len(self.apellido) > 100:
            return False, "El apellido no puede exceder 100 caracteres"
        
        if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", self.apellido):
            return False, "El apellido solo puede contener letras y espacios"
        
        return True, "Apellido válido"
    
    def validar_telefono(self):
        """
        Valida que el teléfono sea válido (formato Guatemala)
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        if not self.telefono or self.telefono.strip() == "":
            return False, "El teléfono no puede estar vacío"
        
        # Limpiar teléfono (quitar espacios, guiones, paréntesis)
        telefono_limpio = re.sub(r'[\s\-\(\)]', '', self.telefono)
        
        # Validar formato Guatemala: 8 dígitos
        if not re.match(r'^[0-9]{8}$', telefono_limpio):
            return False, "El teléfono debe tener 8 dígitos (formato Guatemala)"
        
        return True, "Teléfono válido"
    
    def validar_email(self):
        """
        Valida que el email sea válido
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        if not self.email or self.email.strip() == "":
            return False, "El email no puede estar vacío"
        
        # Patrón regex para email
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(patron_email, self.email):
            return False, "El formato del email no es válido"
        
        if len(self.email) > 100:
            return False, "El email no puede exceder 100 caracteres"
        
        return True, "Email válido"
    
    def validar_direccion(self):
        """
        Valida que la dirección sea válida
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje_error)
        """
        if not self.direccion or self.direccion.strip() == "":
            return False, "La dirección no puede estar vacía"
        
        if len(self.direccion) < 10:
            return False, "La dirección debe tener al menos 10 caracteres"
        
        if len(self.direccion) > 255:
            return False, "La dirección no puede exceder 255 caracteres"
        
        return True, "Dirección válida"
    
    def validar_completo(self):
        """
        Valida todos los campos del cliente
        
        Returns:
            tuple: (bool, list) - (es_valido, lista_errores)
            
        Example:
            >>> cliente = Cliente(nombre="Juan", apellido="Pérez")
            >>> valido, errores = cliente.validar_completo()
            >>> if not valido:
            ...     for error in errores:
            ...         print(error)
        """
        errores = []
        
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
    
    # ==================== MÉTODOS DE UTILIDAD ====================
    
    def to_dict(self):
        """
        Convierte el objeto Cliente a diccionario
        Útil para serialización JSON o almacenamiento
        
        Returns:
            dict: Diccionario con todos los atributos del cliente
            
        Example:
            >>> cliente = Cliente(1, "Juan", "Pérez")
            >>> datos = cliente.to_dict()
            >>> print(datos['nombre'])
            'Juan'
        """
        return {
            'id_cliente': self.id_cliente,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'email': self.email,
            'direccion': self.direccion,
            'nombre_completo': self.nombre_completo(),
            'fecha_registro': self.fecha_registro.strftime("%Y-%m-%d %H:%M:%S")
        }
    
    @classmethod
    def desde_dict(cls, datos):
        """
        Crea un objeto Cliente desde un diccionario
        
        Args:
            datos (dict): Diccionario con los datos del cliente
            
        Returns:
            Cliente: Nueva instancia de Cliente
            
        Example:
            >>> datos = {'nombre': 'Juan', 'apellido': 'Pérez'}
            >>> cliente = Cliente.desde_dict(datos)
        """
        return cls(
            id_cliente=datos.get('id_cliente'),
            nombre=datos.get('nombre', ''),
            apellido=datos.get('apellido', ''),
            telefono=datos.get('telefono', ''),
            email=datos.get('email', ''),
            direccion=datos.get('direccion', '')
        )
    
    def formatear_telefono(self):
        """
        Formatea el teléfono en un formato legible
        
        Returns:
            str: Teléfono formateado (XXXX-XXXX)
            
        Example:
            >>> cliente = Cliente(telefono="12345678")
            >>> cliente.formatear_telefono()
            '1234-5678'
        """
        telefono_limpio = re.sub(r'[\s\-\(\)]', '', self.telefono)
        if len(telefono_limpio) == 8:
            return f"{telefono_limpio[:4]}-{telefono_limpio[4:]}"
        return self.telefono
    
    def dominio_email(self):
        """
        Extrae el dominio del email
        
        Returns:
            str: Dominio del email
            
        Example:
            >>> cliente = Cliente(email="juan@gmail.com")
            >>> cliente.dominio_email()
            'gmail.com'
        """
        if '@' in self.email:
            return self.email.split('@')[1]
        return ""
    
    def info_completa(self):
        """
        Retorna información completa del cliente en formato legible
        
        Returns:
            str: Información completa formateada
        """
        info = f"""
╔══════════════════════════════════════════════════════╗
║           INFORMACIÓN DEL CLIENTE                    ║
╠══════════════════════════════════════════════════════╣
║ ID:              {self.id_cliente or 'N/A'}
║ Nombre:          {self.nombre_completo()}
║ Teléfono:        {self.formatear_telefono()}
║ Email:           {self.email}
║ Dirección:       {self.direccion}
║ Registro:        {self.fecha_registro.strftime("%d/%m/%Y")}
║ Días registrado: {self.edad_registro()}
╚══════════════════════════════════════════════════════╝
        """
        return info.strip()
    
    def resumen_corto(self):
        """
        Retorna un resumen corto del cliente
        
        Returns:
            str: Resumen en una línea
        """
        return f"{self.nombre_completo()} | {self.formatear_telefono()} | {self.email}"
    
    # ==================== MÉTODOS ESTÁTICOS ====================
    
    @staticmethod
    def crear_vacio():
        """
        Crea un cliente vacío
        
        Returns:
            Cliente: Instancia de cliente con valores por defecto
        """
        return Cliente()
    
    @staticmethod
    def validar_formato_telefono(telefono):
        """
        Valida el formato de un teléfono sin crear un objeto Cliente
        
        Args:
            telefono (str): Número de teléfono a validar
            
        Returns:
            bool: True si el formato es válido
        """
        telefono_limpio = re.sub(r'[\s\-\(\)]', '', telefono)
        return bool(re.match(r'^[0-9]{8}$', telefono_limpio))
    
    @staticmethod
    def validar_formato_email(email):
        """
        Valida el formato de un email sin crear un objeto Cliente
        
        Args:
            email (str): Email a validar
            
        Returns:
            bool: True si el formato es válido
        """
        patron_email = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(patron_email, email))
    
    @staticmethod
    def comparar_clientes(cliente1, cliente2, criterio='nombre'):
        """
        Compara dos clientes según un criterio
        
        Args:
            cliente1 (Cliente): Primer cliente
            cliente2 (Cliente): Segundo cliente
            criterio (str): 'nombre', 'apellido', 'email', 'telefono'
            
        Returns:
            int: -1 si cliente1 < cliente2, 0 si iguales, 1 si cliente1 > cliente2
        """
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
    
    # ==================== MÉTODOS DE CLASE ====================
    
    @classmethod
    def crear_desde_input(cls):
        """
        Crea un cliente solicitando los datos por teclado
        
        Returns:
            Cliente: Nueva instancia de Cliente con datos ingresados
        """
        print("\n" + "="*50)
        print("       REGISTRO DE NUEVO CLIENTE")
        print("="*50)
        
        nombre = input("\n👤 Nombre: ").strip()
        apellido = input("👤 Apellido: ").strip()
        telefono = input("📞 Teléfono (8 dígitos): ").strip()
        email = input("📧 Email: ").strip()
        direccion = input("📍 Dirección: ").strip()
        
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
            print("\n❌ ERRORES EN LOS DATOS:")
            for error in errores:
                print(f"  • {error}")
            return None
        
        print("\n✅ Cliente creado exitosamente")
        return cliente


# ==================== FUNCIONES AUXILIARES ====================

def ordenar_clientes_por_nombre(clientes):
    """
    Ordena una lista de clientes alfabéticamente por nombre completo
    Usa el método de ordenamiento de Python (Timsort - O(n log n))
    
    Args:
        clientes (list): Lista de objetos Cliente
        
    Returns:
        list: Lista ordenada de clientes
    """
    return sorted(clientes, key=lambda c: c.nombre_completo().lower())


def ordenar_clientes_por_apellido(clientes):
    """
    Ordena una lista de clientes alfabéticamente por apellido
    
    Args:
        clientes (list): Lista de objetos Cliente
        
    Returns:
        list: Lista ordenada de clientes
    """
    return sorted(clientes, key=lambda c: c.apellido.lower())


def buscar_cliente_por_nombre(clientes, nombre_buscar):
    """
    Busca clientes cuyo nombre contenga el texto buscado
    Búsqueda secuencial O(n)
    
    Args:
        clientes (list): Lista de clientes
        nombre_buscar (str): Texto a buscar
        
    Returns:
        list: Lista de clientes que coinciden
    """
    resultados = []
    nombre_buscar = nombre_buscar.lower()
    
    for cliente in clientes:
        if nombre_buscar in cliente.nombre_completo().lower():
            resultados.append(cliente)
    
    return resultados


def filtrar_por_dominio_email(clientes, dominio):
    """
    Filtra clientes por dominio de email
    
    Args:
        clientes (list): Lista de clientes
        dominio (str): Dominio a buscar (ej: 'gmail.com')
        
    Returns:
        list: Clientes con ese dominio
    """
    return [c for c in clientes if dominio.lower() in c.email.lower()]


def estadisticas_clientes(clientes):
    """
    Genera estadísticas sobre una lista de clientes
    
    Args:
        clientes (list): Lista de clientes
        
    Returns:
        dict: Diccionario con estadísticas
    """
    if not clientes:
        return {
            'total': 0,
            'dominios_email': {},
            'promedio_dias_registro': 0
        }
    
    # Contar dominios
    dominios = {}
    total_dias = 0
    
    for cliente in clientes:
        dominio = cliente.dominio_email()
        dominios[dominio] = dominios.get(dominio, 0) + 1
        total_dias += cliente.edad_registro()
    
    return {
        'total': len(clientes),
        'dominios_email': dominios,
        'promedio_dias_registro': total_dias / len(clientes) if clientes else 0
    }


# ==================== PRUEBAS / EJEMPLOS ====================

if __name__ == "__main__":
    """
    Ejemplos de uso de la clase Cliente
    """
    print("="*60)
    print("       PRUEBAS DE LA CLASE CLIENTE")
    print("="*60)
    
    # Crear cliente
    cliente1 = Cliente(
        id_cliente=1,
        nombre="Juan",
        apellido="Pérez García",
        telefono="55123456",
        email="juan.perez@gmail.com",
        direccion="Zona 10, Ciudad de Guatemala"
    )
    
    print("\n1. INFORMACIÓN COMPLETA:")
    print(cliente1.info_completa())
    
    print("\n2. VALIDACIONES:")
    valido, errores = cliente1.validar_completo()
    if valido:
        print("Todos los datos son válidos")
    else:
        print("Errores encontrados:")
        for error in errores:
            print(f"  • {error}")
    
    print("\n3. MÉTODOS AUXILIARES:")
    print(f"Nombre completo: {cliente1.nombre_completo()}")
    print(f"Iniciales: {cliente1.iniciales()}")
    print(f"Teléfono formateado: {cliente1.formatear_telefono()}")
    print(f"Dominio email: {cliente1.dominio_email()}")
    print(f"Días registrado: {cliente1.edad_registro()}")
    
    print("\n4. CONVERSIÓN A DICCIONARIO:")
    datos = cliente1.to_dict()
    for clave, valor in datos.items():
        print(f"  {clave}: {valor}")
    
    print("\n" + "="*60)
    print("       PRUEBAS COMPLETADAS")
    print("="*60)