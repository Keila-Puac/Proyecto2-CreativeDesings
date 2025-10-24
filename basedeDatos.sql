-- Tabla de categorías de stickers
CREATE TABLE CategoriaSticker (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    descripcion VARCHAR(255)
);

-- Tabla de stickers (productos)
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

INSERT INTO CategoriaSticker (nombre, descripcion) VALUES
('Vinilo de Corte', 'Stickers resistentes al intemperie, ideales para vehículos'),
('Holográfico', 'Stickers con efecto holográfico'),
('Papel Adhesivo', 'Stickers en papel adhesivo con o sin corte electrónico'),
('Vinilo Especial', 'Dorado espejo, cromo espejo, tornasol y reflectivo');

-- Vinilo de Corte
INSERT INTO Sticker (categoria_id, nombre, precio, medida, especificaciones)
VALUES
(1, 'Sticker Vinilo Corte 15x15 o menos', 20.00, '15x15 cm o menos',
 'No se despintan. Resistentes al intemperie, ideal para vehículos');

-- Holográficos
INSERT INTO Sticker (categoria_id, nombre, precio, medida, especificaciones)
VALUES
(2, 'Sticker Holográfico con corte', 40.00, 'Hoja A4 - 8/9 por hoja', 'Corte electrónico'),
(2, 'Sticker Holográfico sin corte', 30.00, 'Hoja A4 - 8/9 por hoja', 'Impreso sin corte');

-- Papel adhesivo
INSERT INTO Sticker (categoria_id, nombre, precio, medida, especificaciones)
VALUES
(3, 'Sticker Papel Adhesivo con corte', 35.00, 'Hoja carta - 6/7 por hoja', 'Con corte electrónico'),
(3, 'Sticker Papel Adhesivo sin corte', 30.00, 'Hoja carta - 6/7 por hoja', 'Solo impresión');

-- Vinilos Especiales
INSERT INTO Sticker (categoria_id, nombre, precio, medida, especificaciones)
VALUES
(4, 'Dorado Espejo/Cromo Espejo', 30.00, '15x15 cm o menos', 'Cualquier diseño'),
(4, 'Vinilo Tornasol', 30.00, '15x15 cm o menos', 'Cualquier diseño'),
(4, 'Vinilo Reflectivo', 40.00, '15x15 cm o menos', 'Colores: amarillo, rojo y blanco');