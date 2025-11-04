import mysql.connector
from mysql.connector import Error
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ConexionException(Exception):
    """Excepción personalizada para errores de conexión"""
    pass


class Conexion:
    """
    Clase para manejar la conexión a la base de datos MySQL
    """

    def __init__(self):
        """Inicializa los parámetros de conexión"""
        try:
            self.host = 'localhost'
            self.database = 'creative_designs'
            self.user = 'root'
            self.password = ''  # CAMBIA POR TU CONTRASEÑA DE MYSQL
            self.port = 3306
            self.conexion = None
        except Exception as e:
            logger.error(f"Error al inicializar configuración de conexión: {e}")
            raise ConexionException(f"Error en configuración: {e}")

    def conectar(self):
        """Establece la conexión con la base de datos"""
        try:
            if self.conexion is None or not self.conexion.is_connected():
                self.conexion = mysql.connector.connect(
                    host=self.host,
                    database=self.database,
                    user=self.user,
                    password=self.password,
                    port=self.port,
                    charset='utf8mb4'
                )

                if self.conexion.is_connected():
                    db_info = self.conexion.get_server_info()
                    logger.info(f"Conectado a MySQL Server versión {db_info}")
                    return self.conexion
                else:
                    logger.error("No se pudo conectar a la base de datos")
                    return None

        except Error as e:
            logger.error(f"Error al conectar a MySQL: {e}")
            print(f"Error de conexión: {e}")
            print("\nVerifique:")
            print("1. MySQL está ejecutándose")
            print("2. La base de datos 'creative_designs' existe")
            print("3. Usuario y contraseña son correctos")
            print(f"4. Configuración actual: host={self.host}, user={self.user}, db={self.database}")
            return None

        except Exception as e:
            logger.error(f"Error inesperado al conectar: {e}")
            return None

    def desconectar(self):
        """Cierra la conexión con la base de datos"""
        try:
            if self.conexion is not None and self.conexion.is_connected():
                self.conexion.close()
                logger.info("Conexión MySQL cerrada")
        except Error as e:
            logger.error(f"Error al cerrar conexión: {e}")
        except Exception as e:
            logger.error(f"Error inesperado al cerrar: {e}")

    def obtener_cursor(self):
        """Retorna un cursor para ejecutar consultas"""
        try:
            if self.conexion and self.conexion.is_connected():
                return self.conexion.cursor()
            else:
                logger.warning("No hay conexión activa para crear cursor")
                return None
        except Exception as e:
            logger.error(f"Error al obtener cursor: {e}")
            return None

    def verificar_conexion(self):
        """Verifica si la conexión está activa"""
        try:
            return self.conexion is not None and self.conexion.is_connected()
        except:
            return False

    def ejecutar_query(self, query, params=None):
        """Ejecuta una query SQL"""
        cursor = None
        try:
            conn = self.conectar()
            if not conn:
                return False, "No se pudo conectar a la base de datos"

            cursor = conn.cursor()

            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if query.strip().upper().startswith('SELECT'):
                resultado = cursor.fetchall()
                return True, resultado
            else:
                conn.commit()
                return True, cursor.rowcount

        except Error as e:
            logger.error(f"Error al ejecutar query: {e}")
            if self.conexion:
                try:
                    self.conexion.rollback()
                except:
                    pass
            return False, str(e)

        except Exception as e:
            logger.error(f"Error inesperado: {e}")
            return False, str(e)

        finally:
            if cursor:
                try:
                    cursor.close()
                except:
                    pass
            self.desconectar()


# Función de prueba
def probar_conexion():
    """Prueba la conexión a la base de datos"""
    print("=" * 60)
    print("PROBANDO CONEXIÓN A BASE DE DATOS")
    print("=" * 60)

    try:
        conn = Conexion()
        conexion = conn.conectar()

        if conexion and conexion.is_connected():
            print("\n✓ Conexión exitosa!")

            cursor = conexion.cursor()
            cursor.execute("SELECT DATABASE();")
            db_name = cursor.fetchone()
            print(f"✓ Base de datos actual: {db_name[0]}")

            cursor.execute("SHOW TABLES;")
            tablas = cursor.fetchall()
            print(f"✓ Tablas encontradas: {len(tablas)}")
            for tabla in tablas:
                print(f"  - {tabla[0]}")

            cursor.close()
            conn.desconectar()
            print("\n✓ Conexión cerrada correctamente")
            return True
        else:
            print("\n✗ No se pudo conectar a la base de datos")
            print("\nPosibles soluciones:")
            print("1. Verificar que MySQL esté ejecutándose")
            print("2. Crear la base de datos: mysql -u root -p < basedeDatos.sql")
            print("3. Verificar usuario y contraseña en conexion.py")
            return False

    except Exception as e:
        print(f"\n✗ Error: {e}")
        return False


if __name__ == "__main__":
    probar_conexion()
