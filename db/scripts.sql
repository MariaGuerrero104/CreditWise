CREATE DATABASE creditwise;
USE creditwise;

CREATE TABLE usuarios (
    documento INT PRIMARY KEY,
    nombre VARCHAR(100),
    gmail VARCHAR(100),
    contrasena VARCHAR(100),
    puntaje INT
);

CREATE TABLE misiones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    descripcion TEXT,
    puntos INT
);

CREATE TABLE evaluaciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    mision_id INT,
    puntaje INT,
    fecha DATE,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(documento),
    FOREIGN KEY (mision_id) REFERENCES misiones(id)
);
