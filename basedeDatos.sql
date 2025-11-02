-- Base de datos Creative Designs
CREATE DATABASE IF NOT EXISTS creative_designs;
USE creative_designs;

-- Tabla de Categorías de Stickers
CREATE TABLE CategoriaSticker (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    descripcion TEXT
);

-- Tabla de Stickers (Productos)
CREATE TABLE Sticker (
    id INT AUTO_INCREMENT PRIMARY KEY,
    categoria_id INT,
    nombre VARCHAR(100) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    medida VARCHAR(50),
    especificaciones VARCHAR(255),
    colores VARCHAR(100),
    FOREIGN KEY (categoria_id) REFERENCES CategoriaSticker(id)
);

-- Tabla de Clientes
CREATE TABLE clientes (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100),
    direccion TEXT
);

-- Insertar Categorías
INSERT INTO CategoriaSticker (nombre, descripcion) VALUES
('Vinilo de Corte', 'Stickers resistentes al intemperie, ideales para vehículos'),
('Holográfico', 'Stickers con efecto holográfico brillante'),
('Papel Adhesivo', 'Stickers en papel adhesivo con o sin corte electrónico'),
('Vinilo Especial', 'Dorado espejo, cromo espejo, tornasol y reflectivo');

-- Insertar Productos (Stickers)

-- Vinilo de Corte
INSERT INTO Sticker (categoria_id, nombre, precio, medida, especificaciones) VALUES
(1, 'Sticker Vinilo Corte 15x15 o menos', 20.00, '15x15 cm o menos', 
 'No se despintan. Resistentes al intemperie, ideal para vehículos');

-- Holográficos
INSERT INTO Sticker (categoria_id, nombre, precio, medida, especificaciones) VALUES
(2, 'Sticker Holográfico con corte electrónico', 40.00, 'Hoja A4 - 8/9 por hoja', 
 'Corte electrónico preciso'),
(2, 'Sticker Holográfico sin corte', 30.00, 'Hoja A4 - 8/9 por hoja', 
 'Impreso sin corte, hoja completa');

-- Papel Adhesivo
INSERT INTO Sticker (categoria_id, nombre, precio, medida, especificaciones) VALUES
(3, 'Sticker Papel Adhesivo con corte electrónico', 35.00, 'Hoja carta - 6/7 por hoja', 
 'Con corte electrónico de precisión'),
(3, 'Sticker Papel Adhesivo sin corte', 30.00, 'Hoja carta - 6/7 por hoja', 
 'Solo impresión, sin corte');

-- Vinilos Especiales
INSERT INTO Sticker (categoria_id, nombre, precio, medida, especificaciones) VALUES
(4, 'Vinilo Dorado Espejo', 30.00, '15x15 cm o menos', 
 'Acabado espejo dorado, cualquier diseño'),
(4, 'Vinilo Cromo Espejo', 30.00, '15x15 cm o menos', 
 'Acabado cromado brillante, cualquier diseño'),
(4, 'Vinilo Tornasol', 30.00, '15x15 cm o menos', 
 'Efecto tornasol multicolor, cualquier diseño'),
(4, 'Vinilo Reflectivo Amarillo', 40.00, '15x15 cm o menos', 
 'Alta visibilidad, color amarillo reflectivo'),
(4, 'Vinilo Reflectivo Rojo', 40.00, '15x15 cm o menos', 
 'Alta visibilidad, color rojo reflectivo'),
(4, 'Vinilo Reflectivo Blanco', 40.00, '15x15 cm o menos', 
 'Alta visibilidad, color blanco reflectivo');

-- Insertar algunos clientes de ejemplo
INSERT INTO clientes (nombre, apellido, telefono, email, direccion) VALUES
('Juan', 'Pérez', '12345678', 'juan.perez@example.com', 'Ciudad de Guatemala'),
('María', 'López', '87654321', 'maria.lopez@example.com', 'Antigua Guatemala'),
('Carlos', 'Ramírez', '55667788', 'carlos.ramirez@example.com', 'Quetzaltenango');