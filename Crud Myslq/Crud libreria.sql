-- Crear la base de datos
CREATE DATABASE biblioteca;

-- Usar la base de datos
USE biblioteca;

-- Crear la tabla de libros
CREATE TABLE libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(200) NOT NULL,
    autor VARCHAR(150) NOT NULL,
    genero VARCHAR(100),
    año_publicacion INT,
    isbn VARCHAR(20) UNIQUE,
    editorial VARCHAR(100),
    precio DECIMAL(10, 2),
    stock INT DEFAULT 0,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
-- Insertar un solo libro
INSERT INTO libros (titulo, autor, genero, año_publicacion, isbn, editorial, precio, stock)
VALUES ('Cien años de soledad', 'Gabriel García Márquez', 'Novela', 1967, '978-0307474728', 'Editorial Sudamericana', 45.50, 15);

-- Insertar varios libros a la vez
INSERT INTO libros (titulo, autor, genero, año_publicacion, isbn, editorial, precio, stock)
VALUES 
    ('Don Quijote de la Mancha', 'Miguel de Cervantes', 'Novela', 1605, '978-8437604947', 'Cátedra', 38.00, 20),
    ('1984', 'George Orwell', 'Ciencia ficción', 1949, '978-0451524935', 'Signet Classic', 32.00, 25),
    ('El principito', 'Antoine de Saint-Exupéry', 'Infantil', 1943, '978-0156012195', 'Harcourt', 28.00, 30);
    -- Ver todos los libros
SELECT * FROM libros;

-- Ver solo algunos campos
SELECT id, titulo, autor, precio FROM libros;

-- Buscar un libro específico por ID
SELECT * FROM libros WHERE id = 1;

-- Buscar libros por autor
SELECT * FROM libros WHERE autor = 'Gabriel García Márquez';

-- Buscar libros por género
SELECT * FROM libros WHERE genero = 'Novela';

-- Buscar libros con precio menor a 40
SELECT * FROM libros WHERE precio < 40;

-- Buscar libros que contengan una palabra en el título
SELECT * FROM libros WHERE titulo LIKE '%años%';

-- Ordenar libros por precio (de menor a mayor)
SELECT * FROM libros ORDER BY precio ASC;

-- Ordenar libros por año de publicación (más reciente primero)
SELECT * FROM libros ORDER BY año_publicacion DESC;

-- Contar cuántos libros hay
SELECT COUNT(*) AS total_libros FROM libros;

-- Actualizar el precio de un libro específico
UPDATE libros 
SET precio = 50.00 
WHERE id = 1;

-- Actualizar el stock de un libro
UPDATE libros 
SET stock = 10 
WHERE isbn = '978-0307474728';

-- Actualizar varios campos a la vez
UPDATE libros 
SET precio = 35.00, stock = 18 
WHERE id = 2;

-- Aumentar el precio de todos los libros en un 10%
UPDATE libros 
SET precio = precio * 1.10;

-- Eliminar un libro específico por ID
DELETE FROM libros WHERE id = 1;

-- Eliminar libros por autor
DELETE FROM libros WHERE autor = 'Gabriel García Márquez';

-- Eliminar libros sin stock
DELETE FROM libros WHERE stock = 0;

-- CUIDADO: esto elimina TODOS los libros
DELETE FROM libros;

-- Libros agrupados por género
SELECT genero, COUNT(*) AS cantidad 
FROM libros 
GROUP BY genero;

-- Promedio de precios
SELECT AVG(precio) AS precio_promedio FROM libros;

-- Libro más caro
SELECT * FROM libros ORDER BY precio DESC LIMIT 1;

-- Total en inventario (suma de todos los stocks)
SELECT SUM(stock) AS total_libros_inventario FROM libros;
