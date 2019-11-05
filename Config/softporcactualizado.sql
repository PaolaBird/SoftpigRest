USE softporc;
-- -----------------------------------------------------
-- Table `Person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Person (
  `NO_EMPLOYEE` TINYINT(2) UNSIGNED AUTO_INCREMENT NOT NULL,
  `state` ENUM('En Funciones', 'Inhabilitado', 'Despedido') NULL DEFAULT 'En Funciones',
  `salary`  INT NULL,
  `contract` ENUM('Indefinido', 'Temporal', 'Servicio') NULL DEFAULT 'Indefinido',
  `hoursWorked`  INT NULL,
  `dateAdmission` TIMESTAMP NULL ,
  `dateOff` TIMESTAMP NULL,
  `document` CHAR(10) NOT NULL,
  `firstName` VARCHAR(50) NOT NULL,
  `secondName` VARCHAR(50) NULL DEFAULT '-',
  `fatherLastName` VARCHAR(50) NOT NULL,
  `motherLastName` VARCHAR(50) NOT NULL,
  `sex` ENUM('Mujer', 'Hombre') NULL DEFAULT NULL,
  `email` VARCHAR(100) NOT NULL,
  `phone` CHAR(7) NULL DEFAULT 'Unkown',
  `celPhone` CHAR(10) NOT NULL,
  `idRole` TINYINT(2) UNSIGNED ZEROFILL NULL DEFAULT NULL,
  `password` CHAR(32) NOT NULL,
  `idInstalation` TINYINT(4) NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`NO_EMPLOYEE`),
  UNIQUE INDEX `document` (`document` ASC)  ,
  INDEX `idRole` (`idRole` ASC)  ,
  INDEX `idInstalation` (`idInstalation` ASC)  ,
  CONSTRAINT `Person_ibfk_1`
    FOREIGN KEY (`idRole`)
    REFERENCES `RoleCat` (`ID_ROLE`)
    ON UPDATE CASCADE,
  CONSTRAINT `Person_ibfk_2`
    FOREIGN KEY (`idInstalation`)
    REFERENCES `InstalationCat` (`ID_INSTALATION`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;