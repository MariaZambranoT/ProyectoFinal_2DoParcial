create database Proyecto_Final_POO

Use Proyecto_Final_POO

create table Personas 
(
id_persona smallint primary key,
nombre varchar (50),
apellido varchar (50),
cedula char (10),
edad tinyint,
fecha_nacimiento date,
email varchar (100),
peso DECIMAL(10, 2),
estatura DECIMAL(5, 2)

)

use Proyecto_Final_POO
go

select * from Personas

INSERT INTO personas (id_persona, nombre, apellido, cedula, edad, fecha_nacimiento, email, peso, estatura)
VALUES (1, 'María', 'Zamb', 1234567891, NULL, '2000-01-01', 'maria@gmail.com', 10, 1.50),
       (2, 'Mana', 'Zamb', 1234567891, NULL, '2000-01-01', 'maria@gmail.com', 10, 1.50),
       (3, 'Carlos', 'González', 4561236581, NULL, '2000-01-01', 'carlo@hotmail.com', 10, 1.80),
       (4, 'Pepsi Man', NULL, 0312457888, NULL, '2000-01-01', 'htf@hotmail.com', 16.2, 1.02),
       (5, 'Talbot', 'Linux', 0478945665, NULL, '1967-08-19', 'linux@hotmail.com', 1.85, 1.75);

