import mysql.connector

def crear_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="CreativeDB"
        )
        return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar a MySQL: {error}")
        return None
