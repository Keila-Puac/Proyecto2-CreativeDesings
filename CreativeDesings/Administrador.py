"""
MODELO ADMINISTRADOR - Creative Designs
Clase completa que representa un usuario administrador del sistema

Autor: Creative Designs Team
Fecha: 2025
Descripción: Modelo de usuario con roles, validaciones y manejo de errores
"""

import re
import logging
from datetime import datetime
from enum import Enum
from typing import Optional, Tuple, Dict, List

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class AdministradorException(Exception):
    """Excepción personalizada para errores relacionados con Administrador"""
    pass


class RolUsuario(Enum):
    """Enumeración de roles disponibles en el sistema"""
    ADMINISTRADOR = "administrador"
    VENDEDOR = "vendedor"
    SUPERVISOR = "supervisor"
    INVITADO = "invitado"


class Administrador:
    """
    Clase Administrador - Representa un usuario del sistema con permisos
    
    Atributos:
        id_admin (int): Identificador único
        nombre (str): Nombre completo del usuario
        usuario (str): Nombre de usuario único para login
        password (str): Contraseña del usuario
        rol (str): Rol del usuario en el sistema
        activo (bool): Estado del usuario
        fecha_creacion (datetime): Fecha de creación de la cuenta
        ultimo_acceso (datetime): Último inicio de sesión
        intentos_fallidos (int): Contador de intentos de login fallidos
    """
    
    # Configuración de seguridad
    MAX_INTENTOS_LOGIN = 3
    MIN_LONGITUD_PASSWORD = 5
    MAX_LONGITUD_PASSWORD = 50
    
    def __init__(self, id_admin=None, nombre="", usuario="", password="", rol="vendedor"):
        """
        Constructor de la clase Administrador
        
        Args:
            id_admin (int, optional): ID único del administrador
            nombre (str): Nombre completo
            usuario (str): Nombre de usuario para login
            password (str): Contraseña
            rol (str): Rol del usuario
            
        Raises:
            AdministradorException: Si hay error al crear el administrador
        """
        try:
            self.id_admin = id_admin
            self.nombre = nombre.strip() if nombre else ""
            self.usuario = usuario.strip().lower() if usuario else ""
            self.password = password if password else ""
            self.rol = rol.lower() if rol else "vendedor"
            self.activo = True
            self.fecha_creacion = datetime.now()
            self.ultimo_acceso = None
            self.intentos_fallidos = 0
            self.permisos_personalizados = []
            
        except Exception as e:
            logger.error(f"Error al crear Administrador: {e}")
            raise AdministradorException(f"No se pudo crear el administrador: {str(e)}")
    
    # ==================== MÉTODOS MÁGICOS ====================
    
    def __str__(self):
        """Representación en string del administrador"""
        try:
            estado = "Activo" if self.activo else "Inactivo"
            return f"Administrador({self.id_admin}, {self.nombre}, {self.usuario}, {self.rol}, {estado})"
        except Exception as e:
            logger.error(f"Error en __str__: {e}")
            return f"Administrador(Error: {str(e)})"
    
    def __repr__(self):
        """Representación oficial del objeto"""
        try:
            return f"Administrador(id={self.id_admin}, usuario='{self.usuario}', rol='{self.rol}')"
        except Exception as e:
            return "Administrador(Error)"
    
    def __eq__(self, otro):
        """Comparación de igualdad"""
        try:
            if not isinstance(otro, Administrador):
                return False
            return self.id_admin == otro.id_admin
        except Exception as e:
            logger.error(f"Error en comparación: {e}")
            return False
    
    def __hash__(self):
        """Hash para usar en sets y diccionarios"""
        try:
            return hash((self.id_admin, self.usuario)) if self.id_admin else hash(id(self))
        except Exception as e:
            logger.error(f"Error en hash: {e}")
            return 0
    
    def __lt__(self, otro):
        """Comparación para ordenamiento por nombre"""
        try:
            if not isinstance(otro, Administrador):
                return NotImplemented
            return self.nombre.lower() < otro.nombre.lower()
        except Exception as e:
            logger.error(f"Error en comparación menor que: {e}")
            return NotImplemented
    
    # ==================== VALIDACIONES ====================
    
    def validar_nombre(self) -> Tuple[bool, str]:
        """
        Valida el nombre del administrador
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje)
        """
        try:
            if not self.nombre or self.nombre.strip() == "":
                return False, "El nombre no puede estar vacío"
            
            if len(self.nombre) < 3:
                return False, "El nombre debe tener al menos 3 caracteres"
            
            if len(self.nombre) > 100:
                return False, "El nombre no puede exceder 100 caracteres"
            
            if not re.match(r"^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$", self.nombre):
                return False, "El nombre solo puede contener letras y espacios"
            
            return True, "Nombre válido"
            
        except Exception as e:
            logger.error(f"Error al validar nombre: {e}")
            return False, f"Error en validación: {str(e)}"
    
    def validar_usuario(self) -> Tuple[bool, str]:
        """
        Valida el nombre de usuario
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje)
        """
        try:
            if not self.usuario or self.usuario.strip() == "":
                return False, "El usuario no puede estar vacío"
            
            if len(self.usuario) < 4:
                return False, "El usuario debe tener al menos 4 caracteres"
            
            if len(self.usuario) > 50:
                return False, "El usuario no puede exceder 50 caracteres"
            
            # Solo letras, números y guión bajo
            if not re.match(r"^[a-z0-9_]+$", self.usuario):
                return False, "El usuario solo puede contener letras minúsculas, números y guión bajo"
            
            # No puede empezar con número
            if self.usuario[0].isdigit():
                return False, "El usuario no puede empezar con un número"
            
            return True, "Usuario válido"
            
        except Exception as e:
            logger.error(f"Error al validar usuario: {e}")
            return False, f"Error en validación: {str(e)}"
    
    def validar_password(self) -> Tuple[bool, str]:
        """
        Valida la contraseña
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje)
        """
        try:
            if not self.password:
                return False, "La contraseña no puede estar vacía"
            
            if len(self.password) < self.MIN_LONGITUD_PASSWORD:
                return False, f"La contraseña debe tener al menos {self.MIN_LONGITUD_PASSWORD} caracteres"
            
            if len(self.password) > self.MAX_LONGITUD_PASSWORD:
                return False, f"La contraseña no puede exceder {self.MAX_LONGITUD_PASSWORD} caracteres"
            
            # Verificar complejidad básica
            tiene_numero = any(c.isdigit() for c in self.password)
            tiene_letra = any(c.isalpha() for c in self.password)
            
            if not (tiene_numero and tiene_letra):
                return False, "La contraseña debe contener al menos una letra y un número"
            
            return True, "Contraseña válida"
            
        except Exception as e:
            logger.error(f"Error al validar contraseña: {e}")
            return False, f"Error en validación: {str(e)}"
    
    def validar_rol(self) -> Tuple[bool, str]:
        """
        Valida el rol del administrador
        
        Returns:
            tuple: (bool, str) - (es_valido, mensaje)
        """
        try:
            roles_validos = [r.value for r in RolUsuario]
            
            if self.rol.lower() not in roles_validos:
                return False, f"Rol inválido. Roles válidos: {', '.join(roles_validos)}"
            
            return True, "Rol válido"
            
        except Exception as e:
            logger.error(f"Error al validar rol: {e}")
            return False, f"Error en validación: {str(e)}"
    
    def validar_completo(self) -> Tuple[bool, List[str]]:
        """
        Valida todos los campos del administrador
        
        Returns:
            tuple: (bool, list) - (es_valido, lista_errores)
        """
        errores = []
        
        try:
            # Validar nombre
            valido, mensaje = self.validar_nombre()
            if not valido:
                errores.append(f"Nombre: {mensaje}")
            
            # Validar usuario
            valido, mensaje = self.validar_usuario()
            if not valido:
                errores.append(f"Usuario: {mensaje}")
            
            # Validar contraseña
            valido, mensaje = self.validar_password()
            if not valido:
                errores.append(f"Contraseña: {mensaje}")
            
            # Validar rol
            valido, mensaje = self.validar_rol()
            if not valido:
                errores.append(f"Rol: {mensaje}")
            
            return len(errores) == 0, errores
            
        except Exception as e:
            logger.error(f"Error en validación completa: {e}")
            errores.append(f"Error general: {str(e)}")
            return False, errores
    
    # ==================== AUTENTICACIÓN ====================
    
    def validar_credenciales(self, usuario: str, password: str) -> Tuple[bool, str]:
        """
        Valida las credenciales de inicio de sesión
        
        Args:
            usuario (str): Nombre de usuario
            password (str): Contraseña
            
        Returns:
            tuple: (bool, str) - (autenticado, mensaje)
        """
        try:
            # Verificar si la cuenta está activa
            if not self.activo:
                return False, "Cuenta inactiva. Contacte al administrador."
            
            # Verificar intentos fallidos
            if self.intentos_fallidos >= self.MAX_INTENTOS_LOGIN:
                return False, f"Cuenta bloqueada por {self.MAX_INTENTOS_LOGIN} intentos fallidos."
            
            # Validar usuario
            if self.usuario != usuario.strip().lower():
                self.incrementar_intentos_fallidos()
                return False, "Usuario o contraseña incorrectos"
            
            # Validar contraseña
            if self.password != password:
                self.incrementar_intentos_fallidos()
                return False, "Usuario o contraseña incorrectos"
            
            # Autenticación exitosa
            self.resetear_intentos_fallidos()
            self.registrar_acceso()
            return True, "Autenticación exitosa"
            
        except Exception as e:
            logger.error(f"Error en autenticación: {e}")
            return False, f"Error en autenticación: {str(e)}"
    
    def incrementar_intentos_fallidos(self):
        """Incrementa el contador de intentos fallidos"""
        try:
            self.intentos_fallidos += 1
            if self.intentos_fallidos >= self.MAX_INTENTOS_LOGIN:
                self.desactivar()
        except Exception as e:
            logger.error(f"Error al incrementar intentos: {e}")
    
    def resetear_intentos_fallidos(self):
        """Resetea el contador de intentos fallidos"""
        try:
            self.intentos_fallidos = 0
        except Exception as e:
            logger.error(f"Error al resetear intentos: {e}")
    
    def registrar_acceso(self):
        """Registra el último acceso del usuario"""
        try:
            self.ultimo_acceso = datetime.now()
        except Exception as e:
            logger.error(f"Error al registrar acceso: {e}")
    
    # ==================== GESTIÓN DE CUENTA ====================
    
    def cambiar_password(self, password_actual: str, password_nueva: str, 
                        password_confirmacion: str) -> Tuple[bool, str]:
        """
        Cambia la contraseña del usuario
        
        Args:
            password_actual (str): Contraseña actual
            password_nueva (str): Nueva contraseña
            password_confirmacion (str): Confirmación de nueva contraseña
            
        Returns:
            tuple: (bool, str) - (exitoso, mensaje)
        """
        try:
            # Verificar contraseña actual
            if self.password != password_actual:
                return False, "La contraseña actual es incorrecta"
            
            # Verificar que las nuevas contraseñas coincidan
            if password_nueva != password_confirmacion:
                return False, "Las contraseñas nuevas no coinciden"
            
            # Verificar que sea diferente a la actual
            if password_nueva == password_actual:
                return False, "La nueva contraseña debe ser diferente a la actual"
            
            # Validar nueva contraseña
            password_temp = self.password
            self.password = password_nueva
            valido, mensaje = self.validar_password()
            
            if not valido:
                self.password = password_temp
                return False, mensaje
            
            return True, "Contraseña cambiada exitosamente"
            
        except Exception as e:
            logger.error(f"Error al cambiar contraseña: {e}")
            return False, f"Error al cambiar contraseña: {str(e)}"
    
    def activar(self) -> Tuple[bool, str]:
        """Activa la cuenta del usuario"""
        try:
            self.activo = True
            self.resetear_intentos_fallidos()
            return True, "Cuenta activada"
        except Exception as e:
            logger.error(f"Error al activar cuenta: {e}")
            return False, f"Error al activar cuenta: {str(e)}"
    
    def desactivar(self) -> Tuple[bool, str]:
        """Desactiva la cuenta del usuario"""
        try:
            self.activo = False
            return True, "Cuenta desactivada"
        except Exception as e:
            logger.error(f"Error al desactivar cuenta: {e}")
            return False, f"Error al desactivar cuenta: {str(e)}"
    
    def cambiar_rol(self, nuevo_rol: str) -> Tuple[bool, str]:
        """
        Cambia el rol del usuario
        
        Args:
            nuevo_rol (str): Nuevo rol a asignar
            
        Returns:
            tuple: (bool, str) - (exitoso, mensaje)
        """
        try:
            rol_anterior = self.rol
            self.rol = nuevo_rol.lower()
            
            valido, mensaje = self.validar_rol()
            if not valido:
                self.rol = rol_anterior
                return False, mensaje
            
            return True, f"Rol cambiado de {rol_anterior} a {self.rol}"
            
        except Exception as e:
            logger.error(f"Error al cambiar rol: {e}")
            return False, f"Error al cambiar rol: {str(e)}"
    
    # ==================== PERMISOS ====================
    
    def es_administrador(self) -> bool:
        """Verifica si el usuario es administrador"""
        try:
            return self.rol.lower() == "administrador"
        except Exception as e:
            logger.error(f"Error al verificar si es administrador: {e}")
            return False
    
    def es_vendedor(self) -> bool:
        """Verifica si el usuario es vendedor"""
        try:
            return self.rol.lower() == "vendedor"
        except Exception as e:
            logger.error(f"Error al verificar si es vendedor: {e}")
            return False
    
    def es_supervisor(self) -> bool:
        """Verifica si el usuario es supervisor"""
        try:
            return self.rol.lower() == "supervisor"
        except Exception as e:
            logger.error(f"Error al verificar si es supervisor: {e}")
            return False
    
    def tiene_permiso(self, permiso: str) -> bool:
        """
        Verifica si el usuario tiene un permiso específico
        
        Args:
            permiso (str): Nombre del permiso a verificar
            
        Returns:
            bool: True si tiene el permiso
        """
        try:
            # Administrador tiene todos los permisos
            if self.es_administrador():
                return True
            
            # Verificar permisos personalizados
            if permiso in self.permisos_personalizados:
                return True
            
            # Permisos por rol
            permisos_vendedor = ['ver_productos', 'ver_clientes', 'crear_pedidos']
            permisos_supervisor = permisos_vendedor + ['ver_reportes', 'gestionar_productos']
            
            if self.es_supervisor():
                return permiso in permisos_supervisor
            elif self.es_vendedor():
                return permiso in permisos_vendedor
            
            return False
            
        except Exception as e:
            logger.error(f"Error al verificar permiso: {e}")
            return False
    
    def agregar_permiso(self, permiso: str) -> bool:
        """Agrega un permiso personalizado al usuario"""
        try:
            if permiso not in self.permisos_personalizados:
                self.permisos_personalizados.append(permiso)
                return True
            return False
        except Exception as e:
            logger.error(f"Error al agregar permiso: {e}")
            return False
    
    def remover_permiso(self, permiso: str) -> bool:
        """Remueve un permiso personalizado del usuario"""
        try:
            if permiso in self.permisos_personalizados:
                self.permisos_personalizados.remove(permiso)
                return True
            return False
        except Exception as e:
            logger.error(f"Error al remover permiso: {e}")
            return False