--Datos
--
-- Dumping data for table TypeInstalationCat
--

SET AUTOCOMMIT = 0;
INSERT INTO TypeInstalationCat (typeInstalation) VALUES
('Oficinas'),
('Bodegas' ),
('Corrales');
COMMIT;

--
-- Dumping data for table InstalationCat
--

SET AUTOCOMMIT = 0;
INSERT INTO InstalationCat (idTypeInstalation, name, capacity) VALUES
(1, 'Oficina', 	 0),
(2, 'Articulos', 1000),
(3, 'Gestacion', 200),
(3, 'Parto',     200),
(3, 'Lechones',  200),
(3, 'Marrano',   200),
(3, 'Primales',  200),
(3, 'Gordo',     200);
COMMIT;

--
-- Dumping data for table RaceCat
--

SET AUTOCOMMIT = 0;
INSERT INTO RaceCat (race, description) VALUES
('Duroc', 'Raza norteamericana.\r\nDesarrollo, conversion y velocidad de crecimiento. Su capa varia del amarillos a las diferentes gamas del rojo.\r\n Orejas mediana, cabeza pequeña, cara ancha, ojos prominentes, cuello corto, pecho amplio.\r\n Nueve lechones y lechera.'),
('Duroc, Hampshire', 'Combina la productividad de la raza duroc y la buena calidad de la carne de la raza hampshire'),
('Hampshire', 'Nativa de Inglaterra y Estados Unidos.\r\nColor negro, con una cincha blanca que abarca sus extremidades delanteras.\r\nOrejas erguidas.\r\nVulnerable a los cambios de temperatura.\r\nProlificidad, aptitud lechera, poca habilidad materna.\r\nProduce poca grasa.'),
('Landrace', 'Origen Danes.\r\nColoración blanca.\r\nOrejas largas hacia adelante.\r\nGran longitud corporal.\r\nGran prolificidad, 12 lechones por camada con muy buen peso al nacer (1300gr a 1500gr).\r\nAptitud lechera y materna.\r\n\r\n'),
('Pietrain', 'Origen belga, Gran Bretaña y Alemania.\r\nPerfil cóncavo  orejas rectas.\r\nPiel blanca con manchas o pecas negras.\r\nEscasa en leche y mala habilidad materna.\r\nMala velocidad de crecimiento y deficiente conversión.\r\nGran volumen de jamón.'),
('Yorkshire', 'Originario de Inglaterra.\r\nDe capa blanca. Es largo, ancho y profundo, con apariencia maciza.\r\nCabeza mediana y esquelética. Hocico ancho y las orejas medianas hacia adelante.\r\nCaracterísticas rusticas y prolíficas, promedia 11 lechones por camada.\r\nAptitud materna y lechera.\r\nLongitud y rapidez de crecimiento\r\nEsta raza incluye a la Large White de gran tamaño y la Middle White de tamaño mediano.');
COMMIT;


SET AUTOCOMMIT = 0;
INSERT INTO Pig (state, sex, weigth, idRace, growthPhase, pigStage, health, idInstalation, birthDate, acquisitionDate) VALUES 
('Activo','Macho',  94,  1 , 'Lactancia', 'Lechon',  'Sano', 5, '2018-10-02', '2018-12-09'),
('Activo','Hembra', 90,  1,  'Lactancia', 'Lechon',  'Sano', 5, '2018-12-01', '2018-12-01'),
('Activo','Macho',  100, 3,  'Levante',   'Marrano', 'Sano', 5, '2018-12-01', '2018-12-01'),
('Activo','Hembra', 100, 3,  'Engorde',   'Marrano', 'Sano', 5, '2018-12-01', '2018-12-01'),
('Activo','Hembra', 90,  1,  'Lactancia', 'Lechon',  'Sano', 5, '2018-12-01', '2018-12-01'),
('Activo','Hembra', 90,  1,  'Lactancia', 'Lechon',  'Sano', 5, '2018-12-01', '2018-12-01');
COMMIT;

--
-- Dumping data for table RoleCat
--

SET AUTOCOMMIT = 0;
INSERT INTO RoleCat (ID_ROLE, role) VALUES
(0,  'Administrador'),
(10, 'Empleado Administrativo'),
(11, 'Empleado Operativo');
COMMIT;


--
-- Dumping data for table Person VALUES
--

SET AUTOCOMMIT = 0;
INSERT INTO Person (NO_EMPLOYEE,state, DOCUMENT, firstName, secondName, fatherLastName, motherLastName, sex, email, phone, celPhone, idRole, password, idInstalation) VALUES
(01,'En funciones','1090502664', 'Juan',  'Fernando', 'Romero',   'Ortega', 'Male', 'juanfernandoro@ufps.edu.co', '5782723', '3003719983', 0,  MD5('0001'), 1),
(02,'En funciones','1090512864', 'Yindy', 'Paola',    'Pajaro',   'Urquijo', 'Female', 'yindypaolapu@ufps.edu.co',   '5486985', '3012546589', 10, MD5('1002'), 2),
(03,'Inhabilitado','1085545454', 'Diego', 'Alirio',   'Gonzalez', 'Melgarejo', 'Male', 'diegoaliriogm@ufps.edu.co',  '5465623', '3012521456', 11, MD5('1103'), 3);
COMMIT;

--
-- Dumping data for table Alarm
--

SET AUTOCOMMIT = 0;
INSERT INTO alarm (employee, date_start, issue) VALUES
(01, '2019-01-12', 'Vacunar lechones recien nacidos'),
(02,'2019-01-12', 'Limpiar corral de primales'),
(02,'2019-01-12', 'Agregar pienso al corral de los primales');
COMMIT;

--
-- Dumping data for table TypeArticleCat
--

SET AUTOCOMMIT = 0;
INSERT INTO TypeArticleCat (typeArticle, description) VALUES
('Crianza',              'Dosificador medicamentos, Dosificador pienso , Deposito de agua,Fontaneria'),
('Cuidados',             'Basculas,Bebederos, Calefacion, Comederos, Marcaje, Refrigeracion, Rejillas, Ventilacion'),
('Ferreteria',           'Tornillos, Martillos, Alicates, etc'),
('Implementos medicos',  'Jeringas, Inseminacion'),
('Limpieza',             'Higiene, Desinfeccion'),
('Varios',               'Articulos varios');
COMMIT;

--
-- Dumping data for table Article VALUES
--

SET AUTOCOMMIT = 0;
INSERT INTO Article (idType, name, quantity, available, loan, idInstalation)VALUES
(1, 'Bebederos', 100, 97, 2, 2),
(1, 'Deposito de Agua', 90, 3, 87, 2);
COMMIT;

--
-- Dumping data for table ArticlePerson VALUES
--

SET AUTOCOMMIT = 0;
INSERT INTO articleperson (idArticle, idPerson, borrowedCopies)VALUES
(1, 01, 2),
(1, 02,3);
COMMIT;

--
-- Dumping data for table Female VALUES
--

SET AUTOCOMMIT = 0;
INSERT INTO Female (ID_FEMALE, virgin, gestation) VALUES 
(14, 'Si', 'No'),
(16, 'Si', 'No'),
(17, 'Si', 'No');
COMMIT;

--
-- Dumping data for table Male VALUES
--

SET AUTOCOMMIT = 0;
INSERT INTO Male (ID_MALE, physicalConformation) VALUES
(13, 'Grosor de 24 cm los perniles'),
(15, 'Aumento rapido de peso');
COMMIT;