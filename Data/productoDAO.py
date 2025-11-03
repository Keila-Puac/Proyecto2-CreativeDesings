"""
PRODUCTO DAO - Creative Designs
Data Access Object para la gestión de productos en la base de datos
"""

import sys
import os
import logging
from typing import List, Optional, Tuple

# Agregar directorio raíz al path
current_dir = os.path.dirname(os.path.abspath(_file_))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

try:
    from Data.conexion import Conexion
except ImportError:
    try:
        from conexion import Conexion
    except ImportError as e:
        print(f"Error: No se pudo importar Conexion: {e}")
        sys.exit(1)

try:
    from Productos import Producto
except ImportError as e:
    print(f"Error: No se pudo importar Producto: {e}")
    sys.exit(1)

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(_name_)

class ProductoDAO:
    def _init_(self):
        self.conexion = Conexion()
    
    def listar(self):
        """Retorna todos los productos (stickers)"""
        productos = []
        try:
            conn = self.conexion.conectar()
            cursor = conn.cursor()
            sql = """SELECT s.id, s.nombre, s.precio, s.medida, 
                     s.especificaciones, s.categoria_id 
                     FROM Sticker s ORDER BY s.nombre"""
            cursor.execute(sql)
            resultados = cursor.fetchall()
            
            for row in resultados:
                producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5])
                productos.append(producto)
            
            cursor.close()
        except Exception as e:
            print(f"Error al listar productos: {e}")
        finally:
            self.conexion.desconectar()
        
        return productos
    
    def listar_por_categoria(self, categoria_id):
        """Lista productos de una categoría específica"""
        productos = []
        try:
            conn = self.conexion.conectar()
            cursor = conn.cursor()
            sql = """SELECT s.id, s.nombre, s.precio, s.medida, 
                     s.especificaciones, s.categoria_id 
                     FROM Sticker s 
                     WHERE s.categoria_id = %s
                     ORDER BY s.nombre"""
            cursor.execute(sql, (categoria_id,))
            resultados = cursor.fetchall()
            
            for row in resultados:
                producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5])
                productos.append(producto)
            
            cursor.close()
        except Exception as e:
            print(f"Error al listar productos por categoría: {e}")
        finally:
            self.conexion.desconectar()
        
        return productos
    
    def listar_categorias(self):
        """Lista todas las categorías de stickers"""
        categorias = []
        try:
            conn = self.conexion.conectar()
            cursor = conn.cursor()
            sql = "SELECT id, nombre, descripcion FROM CategoriaSticker ORDER BY id"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            
            for row in resultados:
                categorias.append({
                    'id': row[0],
                    'nombre': row[1],
                    'descripcion': row[2]
                })
            
            cursor.close()
        except Exception as e:
            print(f"Error al listar categorías: {e}")
        finally:
            self.conexion.desconectar()
        
        return categorias
    
    def buscar_por_id(self, id_producto):
        """Busca un producto por su ID"""
        producto = None
        try:
            conn = self.conexion.conectar()
            cursor = conn.cursor()
            sql = """SELECT id, nombre, precio, medida, especificaciones, categoria_id 
                     FROM Sticker WHERE id = %s"""
            cursor.execute(sql, (id_producto,))
            row = cursor.fetchone()
            
            if row:
                producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5])
            
            cursor.close()
        except Exception as e:
            print(f"Error al buscar producto: {e}")
        finally:
            self.conexion.desconectar()
        
        return producto
    
    def buscar_por_nombre(self, nombre):
        """Busca productos por nombre"""
        productos = []
        try:
            conn = self.conexion.conectar()
            cursor = conn.cursor()
            sql = """SELECT id, nombre, precio, medida, especificaciones, categoria_id 
                     FROM Sticker WHERE nombre LIKE %s ORDER BY nombre"""
            patron = f"%{nombre}%"
            cursor.execute(sql, (patron,))
            resultados = cursor.fetchall()
            
            for row in resultados:
                producto = Producto(row[0], row[1], row[2], row[3], row[4], row[5])
                productos.append(producto)
            
            cursor.close()
        except Exception as e:
            print(f"Error al buscar productos: {e}")
        finally:
            self.conexion.desconectar()
        
        return productos
    
    def insertar(self, producto):
        """Inserta un nuevo producto"""
        resultado = False
        try:
            conn = self.conexion.conectar()
            cursor = conn.cursor()
            sql = """INSERT INTO Sticker (categoria_id, nombre, precio, medida, especificaciones) 
                     VALUES (%s, %s, %s, %s, %s)"""
            valores = (producto.categoria_id, producto.nombre, producto.precio, 
                      producto.medida, producto.especificaciones)
            cursor.execute(sql, valores)
            conn.commit()
            resultado = True
            cursor.close()
        except Exception as e:
            print(f"Error al insertar producto: {e}")
            conn.rollback()
        finally:
            self.conexion.desconectar()
        
        return resultado
    
    def actualizar(self, producto):
        """Actualiza un producto existente"""
        resultado = False
        try:
            conn = self.conexion.conectar()
            cursor = conn.cursor()
            sql = """UPDATE Sticker SET categoria_id=%s, nombre=%s, precio=%s, 
                     medida=%s, especificaciones=%s WHERE id=%s"""
            valores = (producto.categoria_id, producto.nombre, producto.precio, 
                      producto.medida, producto.especificaciones, producto.id_producto)
            cursor.execute(sql, valores)
            conn.commit()
            resultado = True
            cursor.close()
        except Exception as e:
            print(f"Error al actualizar producto: {e}")
            conn.rollback()
        finally:
            self.conexion.desconectar()
        
        return resultado
    
    def eliminar(self, id_producto):
        """Elimina un producto por su ID"""
        resultado = False
        try:
            conn = self.conexion.conectar()
            cursor = conn.cursor()
            sql = "DELETE FROM Sticker WHERE id = %s"
            cursor.execute(sql, (id_producto,))
            conn.commit()
            resultado = True
            cursor.close()
        except Exception as e:
            print(f"Error al eliminar producto: {e}")
            conn.rollback()
        finally:
            self.conexion.desconectar()
        
        return resultado