# Sistema de Registro e Inicio de Sesion - Creative Designs
# Estructura de datos: Listas y diccionarios para almacenamiento de usuarios

class SistemaAutenticacion:
    def __init__(self):
        # Listas para almacenar usuarios (estructura de datos lineal)
        self.usuarios_clientes = []  # Lista de diccionarios para clientes
        self.usuarios_admin = []     # Lista de diccionarios para administradores
        
        # Administrador por defecto (almacenado en heap)
        self.usuarios_admin.append({
            'usuario': 'admin',
            'contrasena': 'admin123',
            'correo': 'admin@creativedesigns.com',
            'tipo': 'administrador'
        })
        
        # Cliente de prueba (almacenado en heap)
        self.usuarios_clientes.append({
            'usuario': 'cliente1',
            'contrasena': '12345',
            'correo': 'cliente1@example.com',
            'telefono': '12345678',
            'tipo': 'cliente'
        })
        
        # Variable para almacenar sesion activa (referencia/puntero)
        self.sesion_activa = None

    def mostrar_menu_principal(self):
        """Muestra el menu principal del sistema"""
        print("\n" + "="*50)
        print("CREATIVE DESIGNS - Sistema de Gestion")
        print("="*50)
        print("1. Registrarse como Cliente")
        print("2. Iniciar Sesion como Cliente")
        print("3. Iniciar Sesion como Administrador")
        print("4. Salir")
        print("="*50)

    def validar_datos_registro(self, usuario, contrasena, correo):
        """Validacion de datos usando busqueda secuencial"""
        # Busqueda secuencial en lista de clientes
        for cliente in self.usuarios_clientes:
            if cliente['usuario'] == usuario:
                return False, "El usuario ya existe"
        
        # Validacion de longitud de contrasena
        if len(contrasena) < 5:
            return False, "La contrasena debe tener al menos 5 caracteres"
        
        # Validacion basica de correo
        if '@' not in correo or '.' not in correo:
            return False, "Correo electronico invalido"
        
        return True, "Datos validos"

    def registrar_cliente(self):
        """Registro de nuevo cliente usando estructuras de datos"""
        print("\n" + "-"*50)
        print("REGISTRO DE CLIENTE")
        print("-"*50)
        
        # Entrada de datos (almacenados temporalmente en stack)
        usuario = input("Ingrese nombre de usuario: ")
        contrasena = input("Ingrese contrasena: ")
        correo = input("Ingrese correo electronico: ")
        telefono = input("Ingrese telefono: ")
        
        # Validacion de datos
        es_valido, mensaje = self.validar_datos_registro(usuario, contrasena, correo)
        
        if not es_valido:
            print(f"\nError: {mensaje}")
            return False
        
        # Crear nuevo cliente (diccionario almacenado en heap)
        nuevo_cliente = {
            'usuario': usuario,
            'contrasena': contrasena,
            'correo': correo,
            'telefono': telefono,
            'tipo': 'cliente'
        }
        
        # Agregar a la lista de clientes
        self.usuarios_clientes.append(nuevo_cliente)
        
        print(f"\nRegistro exitoso. Bienvenido {usuario}")
        return True

    def buscar_usuario_secuencial(self, lista_usuarios, usuario, contrasena):
        """Busqueda secuencial de usuario en lista"""
        # Recorre la lista elemento por elemento
        for i in range(len(lista_usuarios)):
            if (lista_usuarios[i]['usuario'] == usuario and 
                lista_usuarios[i]['contrasena'] == contrasena):
                return lista_usuarios[i]  # Retorna referencia al usuario
        return None

    def iniciar_sesion_cliente(self):
        """Inicio de sesion para clientes"""
        print("\n" + "-"*50)
        print("INICIO DE SESION - CLIENTE")
        print("-"*50)
        
        usuario = input("Usuario: ")
        contrasena = input("Contrasena: ")
        
        # Busqueda secuencial del usuario
        usuario_encontrado = self.buscar_usuario_secuencial(
            self.usuarios_clientes, usuario, contrasena
        )
        
        if usuario_encontrado:
            self.sesion_activa = usuario_encontrado  # Asignacion de referencia
            print(f"\nBienvenido {usuario_encontrado['usuario']}")
            print(f"Tipo de cuenta: Cliente")
            print(f"Correo: {usuario_encontrado['correo']}")
            return True
        else:
            print("\nUsuario o contrasena incorrectos")
            return False

    def iniciar_sesion_admin(self):
        """Inicio de sesion para administradores"""
        print("\n" + "-"*50)
        print("INICIO DE SESION - ADMINISTRADOR")
        print("-"*50)
        
        usuario = input("Usuario: ")
        contrasena = input("Contrasena: ")
        
        # Busqueda secuencial del administrador
        usuario_encontrado = self.buscar_usuario_secuencial(
            self.usuarios_admin, usuario, contrasena
        )
        
        if usuario_encontrado:
            self.sesion_activa = usuario_encontrado
            print(f"\nBienvenido Administrador {usuario_encontrado['usuario']}")
            print(f"Acceso completo al sistema")
            return True
        else:
            print("\nCredenciales de administrador incorrectas")
            return False

    def cerrar_sesion(self):
        """Cierra la sesion activa"""
        if self.sesion_activa:
            print(f"\nSesion cerrada para {self.sesion_activa['usuario']}")
            self.sesion_activa = None
        else:
            print("\nNo hay sesion activa")

    def mostrar_sesion_activa(self):
        """Muestra informacion de la sesion actual"""
        if self.sesion_activa:
            print("\n" + "-"*50)
            print("SESION ACTIVA")
            print("-"*50)
            print(f"Usuario: {self.sesion_activa['usuario']}")
            print(f"Tipo: {self.sesion_activa['tipo']}")
            print(f"Correo: {self.sesion_activa['correo']}")
            if self.sesion_activa['tipo'] == 'cliente':
                print(f"Telefono: {self.sesion_activa['telefono']}")
        else:
            print("\nNo hay sesion activa")

    def listar_todos_usuarios(self):
        """Lista todos los usuarios registrados (solo para admin)"""
        if not self.sesion_activa or self.sesion_activa['tipo'] != 'administrador':
            print("\nAcceso denegado. Solo administradores")
            return
        
        print("\n" + "="*50)
        print("LISTADO DE USUARIOS")
        print("="*50)
        
        print("\nADMINISTRADORES:")
        for admin in self.usuarios_admin:
            print(f"  Usuario: {admin['usuario']}")
        
        print("\nCLIENTES:")
        for cliente in self.usuarios_clientes:
            print(f"  Usuario: {cliente['usuario']} | Tel: {cliente['telefono']}")


# Funcion principal para ejecutar el sistema
def main():
    sistema = SistemaAutenticacion()
    
    while True:
        sistema.mostrar_menu_principal()
        
        try:
            opcion = input("\nSeleccione una opcion: ")
            
            if opcion == '1':
                sistema.registrar_cliente()
            
            elif opcion == '2':
                if sistema.iniciar_sesion_cliente():
                    # Menu de cliente
                    while sistema.sesion_activa:
                        print("\n--- MENU CLIENTE ---")
                        print("1. Ver mi informacion")
                        print("2. Cerrar sesion")
                        sub_opcion = input("Opcion: ")
                        
                        if sub_opcion == '1':
                            sistema.mostrar_sesion_activa()
                        elif sub_opcion == '2':
                            sistema.cerrar_sesion()
                            break
            
            elif opcion == '3':
                if sistema.iniciar_sesion_admin():
                    # Aqui se integrara con Administrador.py
                    print("\nRedirigiendo al panel de administrador...")
                    print("(Aqui se llamara a la interfaz de Administrador.py)")
                    sistema.cerrar_sesion()
            
            elif opcion == '4':
                print("\nGracias por usar Creative Designs")
                break
            
            else:
                print("\nOpcion invalida")
        
        except Exception as e:
            print(f"\nError: {e}")


if __name__ == "__main__":
    main()