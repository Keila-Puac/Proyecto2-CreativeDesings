from Administrador import Administrador

class RegistroUsuario:
    def __init__(self):
        # Listas para almacenar usuarios
        self.usuarios_admin = []
        
        # Administrador por defecto
        admin_default = Administrador(1, "Administrador Principal", "admin", "admin123", "administrador")
        self.usuarios_admin.append(admin_default)
    
    def validar_datos_registro(self, usuario, password):
        """Valida los datos antes de registrar"""
        # Verificar si el usuario ya existe
        for admin in self.usuarios_admin:
            if admin.usuario == usuario:
                return False, "El usuario ya existe"
        
        # Validar longitud de contraseña
        if len(password) < 5:
            return False, "La contraseña debe tener al menos 5 caracteres"
        
        return True, "Datos válidos"
    
    def registrar(self, administrador):
        """Registra un nuevo administrador/usuario"""
        es_valido, mensaje = self.validar_datos_registro(
            administrador.usuario, 
            administrador.password
        )
        
        if not es_valido:
            print(f"Error: {mensaje}")
            return False
        
        # Asignar ID automático
        if len(self.usuarios_admin) > 0:
            ultimo_id = max(admin.id_admin for admin in self.usuarios_admin if admin.id_admin)
            administrador.id_admin = ultimo_id + 1
        else:
            administrador.id_admin = 1
        
        # Agregar a la lista
        self.usuarios_admin.append(administrador)
        return True
    
    def validar_login(self, usuario, password):
        """Valida las credenciales de inicio de sesión"""
        for admin in self.usuarios_admin:
            if admin.usuario == usuario and admin.password == password:
                return admin
        return None
    
    def listar_usuarios(self):
        """Lista todos los usuarios registrados"""
        return self.usuarios_admin
    
    def buscar_por_usuario(self, usuario):
        """Busca un usuario por nombre de usuario"""
        for admin in self.usuarios_admin:
            if admin.usuario == usuario:
                return admin
        return None
    
    def actualizar_usuario(self, usuario_antiguo, usuario_nuevo):
        """Actualiza los datos de un usuario"""
        for i, admin in enumerate(self.usuarios_admin):
            if admin.usuario == usuario_antiguo:
                self.usuarios_admin[i] = usuario_nuevo
                return True
        return False
    
    def eliminar_usuario(self, usuario):
        """Elimina un usuario del sistema"""
        for i, admin in enumerate(self.usuarios_admin):
            if admin.usuario == usuario:
                del self.usuarios_admin[i]
                return True
        return False