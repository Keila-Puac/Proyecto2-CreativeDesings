# Interfaz de inicio de sesión y registro de usuarios

class Entrar:
    def __init__(self):
        # Diccionario donde se almacenan todos los usuarios del sistema
        self.Usuarios = {
            "Usuario1": {"Contraseña": "12345", "Correo": "usuario1@example.com"}
        }

        # Atributos individuales del usuario actual
        self.nombre = None
        self.contraseña = None
        self.correo = None

    def Registrarse(self, nombre=None, contraseña=None, correo=None):
        print("\n<< Registro de Usuario >>")

        # Si no se pasan los datos como argumentos, se solicitan por teclado
        if not nombre:
            nombre = input("Ingrese su nombre de usuario: ")
        if not contraseña:
            contraseña = input("Ingrese su contraseña: ")
        if not correo:
            correo = input("Ingrese su correo electrónico: ")

        # Guardar los valores en el objeto actual
        self.nombre = nombre
        self.contraseña = contraseña
        self.correo = correo

        # Validaciones básicas
        if self.nombre in self.Usuarios:
            print("El usuario ingresado ya existe.")
            return
        if len(self.contraseña) < 5:
            print("La contraseña debe tener al menos 5 caracteres.")
            return

        # Guardar el nuevo usuario en el diccionario general
        self.Usuarios[self.nombre] = {
            "Contraseña": self.contraseña,
            "Correo": self.correo
        }

        print(f"{self.nombre}, su cuenta ha sido registrada exitosamente.")
        print("Usuarios registrados:", self.Usuarios)

    def InicioSesión(self, nombre=None, contraseña=None):
        print("\n<< Inicio de Sesión >>")

        # Permitir tanto ingreso manual como por argumentos
        if not nombre:
            nombre = input("Ingrese su nombre de usuario: ")
        if not contraseña:
            contraseña = input("Ingrese su contraseña: ")

        # Guardar los datos en el objeto actual
        self.nombre = nombre
        self.contraseña = contraseña

        if (self.nombre in self.Usuarios and
                self.Usuarios[self.nombre]["Contraseña"] == self.contraseña):
            print(f"Bienvenido {self.nombre}.")
            self.correo = self.Usuarios[self.nombre]["Correo"]
        else:
            print("Usuario o contraseña incorrectos.")

    def MostrarDatos(self):
        if self.nombre and self.correo:
            print("\nUsuario actual:", self.nombre)
            print("Correo:", self.correo)
        else:
            print("\nNo hay sesión activa.")