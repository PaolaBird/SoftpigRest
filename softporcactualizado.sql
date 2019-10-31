USE softporc;

-- -----------------------------------------------------
-- Table `RoleCat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS RoleCat (
  `ID_ROLE` TINYINT(2)  ZEROFILL AUTO_INCREMENT,
  `role` VARCHAR(50) NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_ROLE`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `TypeInstalationCat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS TypeInstalationCat (
  `ID_TYPE_INSTALATION` TINYINT(4) AUTO_INCREMENT NOT NULL,
  `typeInstalation` VARCHAR(10) NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_TYPE_INSTALATION`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `InstalationCat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS InstalationCat (
  `ID_INSTALATION` TINYINT(4) AUTO_INCREMENT NOT NULL,
  `idTypeInstalation` TINYINT(4) NOT NULL,
  `name` VARCHAR(15) NOT NULL,
  `capacity` SMALLINT(6) NOT NULL,
  `mAncho` SMALLINT UNSIGNED NOT NULL,
  `mLargo` SMALLINT UNSIGNED NOT NULL,
  `mAlto` SMALLINT UNSIGNED NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_INSTALATION`),
  INDEX `idTypeInstalation` (`idTypeInstalation` ASC),
  CONSTRAINT `InstalationCat_ibfk_1`
    FOREIGN KEY (`idTypeInstalation`)
    REFERENCES `TypeInstalationCat` (`ID_TYPE_INSTALATION`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `Person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Person (
  `NO_EMPLOYEE` TINYINT(2) UNSIGNED ZEROFILL NOT NULL,
  `state` ENUM('En Funciones', 'Inhabilitado', 'Despedido') NULL DEFAULT NULL,
  `document` CHAR(10) NOT NULL,
  `firstName` VARCHAR(50) NOT NULL,
  `secondName` VARCHAR(50) NULL DEFAULT '-',
  `fatherLastName` VARCHAR(50) NOT NULL,
  `motherLastName` VARCHAR(50) NOT NULL,
  `sex` ENUM('Female', 'Male') NULL DEFAULT NULL,
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
AUTO_INCREMENT = 1
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `Alarm`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Alarm (
  `ID_ALARM` SMALLINT(6) AUTO_INCREMENT NOT NULL,
  `employee` TINYINT(2) UNSIGNED ZEROFILL NULL,
  `date_start` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `issue` VARCHAR(255) NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`ID_ALARM`),
  INDEX `employee` (`employee` ASC)  ,
  CONSTRAINT `Alarm_ibfk_1`
    FOREIGN KEY (`employee`)
    REFERENCES `Person` (`NO_EMPLOYEE`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `TypeArticleCat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS TypeArticleCat(
  `ID_TYPE_ARTICLE` TINYINT(4) AUTO_INCREMENT NOT NULL,
  `typeArticle` VARCHAR(25) NOT NULL,
  `description` TEXT NULL DEFAULT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_TYPE_ARTICLE`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `Article`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Article (
  `ID_ARTICLE` TINYINT(4) AUTO_INCREMENT NOT NULL,
  `idType` TINYINT(4) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `quantity` SMALLINT(6) NOT NULL,
  `available` SMALLINT(6) UNSIGNED NULL,
  `loan` SMALLINT(6) UNSIGNED NULL,
  `idInstalation` TINYINT(4) NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_ARTICLE`),
  INDEX `idType` (`idType` ASC)  ,
  CONSTRAINT `Article_ibfk_1`
    FOREIGN KEY (`idType`)
    REFERENCES `TypeArticleCat` (`ID_TYPE_ARTICLE`)
    ON UPDATE CASCADE,
  CONSTRAINT `Article_ibfk_2`
  	FOREIGN KEY (`idInstalation`)
  	REFERENCES `InstalationCat` (`ID_INSTALATION`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `RaceCat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS RaceCat (
  `ID_RACE` TINYINT(4) AUTO_INCREMENT NOT NULL,
  `race` VARCHAR(50) NOT NULL,
  `description` TEXT NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_RACE`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `Pig`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Pig (
  `ID_PIG` SMALLINT(6) AUTO_INCREMENT NOT NULL,
  `state` ENUM('De Baja', 'ACTIVO') NULL DEFAULT NULL,
  `sex` ENUM('Female', 'Male') NOT NULL,
  `weigth` TINYINT(4) NOT NULL,
  `idRace` TINYINT(4) NOT NULL,
  `growthPhase` ENUM('Lactancia', 'Destete', 'Levante', 'Engorde') NOT NULL,
  `pigStage` ENUM('Lechon', 'Marrano', 'Primal', 'Gordo') NOT NULL,
  `health` ENUM('Sano', 'Enfermo') NOT NULL,
  `idInstalation` TINYINT(4) NOT NULL,
  `birthDate` DATE NULL DEFAULT '0000-00-00' COMMENT 'Desconocida',
  `acquisitionDate` DATE NULL DEFAULT '0000-00-00' COMMENT 'Desconocidad',
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_PIG`),
  INDEX `idRace` (`idRace` ASC)  ,
  INDEX `idInstalation` (`idInstalation` ASC)  ,
  CONSTRAINT `Pig_ibfk_1`
    FOREIGN KEY (`idRace`)
    REFERENCES `RaceCat` (`ID_RACE`)
    ON UPDATE CASCADE,
  CONSTRAINT `Pig_ibfk_2`
    FOREIGN KEY (`idInstalation`)
    REFERENCES `InstalationCat` (`ID_INSTALATION`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `Male`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Male (
  `ID_MALE` SMALLINT(6) NOT NULL,
  `state` ENUM('Active', 'Inactive') NULL,
  `physicalConformation` TEXT NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_MALE`),
  CONSTRAINT `Male_ibfk_1`
    FOREIGN KEY (`ID_MALE`)
    REFERENCES `Pig` (`ID_PIG`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `Female`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Female (
  `ID_FEMALE` SMALLINT(6) NOT NULL,
  `state` ENUM('Active', 'Inactive')  NULL DEFAULT NULL,
  `virgin` ENUM('No', 'Si') NOT NULL DEFAULT 'Si',
  `gestation` ENUM('No', 'Si') NOT NULL DEFAULT 'No',
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_FEMALE`),
  CONSTRAINT `fk_Female_Pig1`
    FOREIGN KEY (`ID_FEMALE`)
    REFERENCES `Pig` (`ID_PIG`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `Birth`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS Birth (
  `ID_BIRTH` SMALLINT(6) AUTO_INCREMENT NOT NULL,	
  `ID_FEMALE` SMALLINT(6) NOT NULL,
  `idMale` SMALLINT(6) NOT NULL,
  `DATE_BIRTH` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `noBabies` TINYINT(4) NOT NULL,
  `noMummy` TINYINT(4) NOT NULL,
  `noDead` TINYINT(4) NOT NULL,
  `idAlarm` SMALLINT(6) NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`ID_BIRTH`, `ID_FEMALE`, `DATE_BIRTH`),
  INDEX  `ID_FEMALE_B` (`ID_FEMALE` ASC)  ,
  INDEX `idMale` (`idMale` ASC)  ,
  INDEX `idAlarm` (`idAlarm` ASC)  ,
  CONSTRAINT `Birth_ibfk_2`
    FOREIGN KEY (`idMale`)
    REFERENCES `Male` (`ID_MALE`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `Female_ibfk_1`
    FOREIGN KEY (`ID_FEMALE`)
    REFERENCES `Female` (`ID_FEMALE`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `Alarm_ibfk_2`
    FOREIGN KEY (`idAlarm`)
    REFERENCES `Alarm` (`ID_ALARM`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `ExamCat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ExamCat (
  `ID_EXAM_CAT` TINYINT(4) AUTO_INCREMENT NOT NULL,
  `examName` VARCHAR(15) NOT NULL,
  `examDescription` TEXT NULL DEFAULT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_EXAM_CAT`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `MaleExam`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS MaleExam (
  `ID_MALE` SMALLINT(6) NOT NULL,
  `ID_EXAM` TINYINT(4) NOT NULL,
  `EXAM_DATE` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `examResult` TEXT NULL DEFAULT NULL,
  PRIMARY KEY (`ID_MALE`, `ID_EXAM`, `EXAM_DATE`),
  INDEX `ID_EXAM` (`ID_EXAM` ASC)  ,
  CONSTRAINT `MaleExam_ibfk_1`
    FOREIGN KEY (`ID_MALE`)
    REFERENCES `Male` (`ID_MALE`)
    ON UPDATE CASCADE,
  CONSTRAINT `MaleExam_ibfk_2`
    FOREIGN KEY (`ID_EXAM`)
    REFERENCES `ExamCat` (`ID_EXAM_CAT`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `TypeMedicineCat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS TypeMedicineCat (
  `ID_TYPE_MEDICINE` TINYINT(4) AUTO_INCREMENT NOT NULL,
  `typeMedicine` VARCHAR(50) NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_TYPE_MEDICINE`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `MedicineCat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS MedicineCat (
  `ID_MEDICINE` TINYINT(4) AUTO_INCREMENT NOT NULL,
  `idTypeMedicine` TINYINT(4) NOT NULL,
  `name` VARCHAR(50) NOT NULL,
  `quantity` SMALLINT(6) NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_MEDICINE`),
  INDEX `idTypeMedicine` (`idTypeMedicine` ASC)  ,
  CONSTRAINT `MedicineCat_ibfk_1`
    FOREIGN KEY (`idTypeMedicine`)
    REFERENCES `TypeMedicineCat` (`ID_TYPE_MEDICINE`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `MedicinePig`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS MedicinePig (
  `ID_MEDICINE` TINYINT(4) NOT NULL,
  `ID_PIG` SMALLINT(6) NOT NULL,
  `DATE_TIME` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `applied` ENUM('No', 'Si') NULL DEFAULT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`ID_MEDICINE`, `ID_PIG`, `DATE_TIME`),
  INDEX `ID_PIG` (`ID_PIG` ASC)  ,
  CONSTRAINT `MedicinePig_ibfk_1`
    FOREIGN KEY (`ID_MEDICINE`)
    REFERENCES `MedicineCat` (`ID_MEDICINE`)
    ON UPDATE CASCADE,
  CONSTRAINT `MedicinePig_ibfk_2`
    FOREIGN KEY (`ID_PIG`)
    REFERENCES `Pig` (`ID_PIG`)
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `PeriodGestation`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS PeriodGestation (
  `ID_PERIOD_GESTATION` SMALLINT(6) AUTO_INCREMENT NOT NULL,
  `ID_FEMALE` SMALLINT(6) NOT NULL,
  `idMale` SMALLINT(6) NOT NULL,
  `DATE_START` DATE NOT NULL,
  `idAlarm` SMALLINT(6) NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_PERIOD_GESTATION`, `ID_FEMALE`, `DATE_START`),
  INDEX `ID_FEMALE` (`ID_FEMALE` ASC)  ,
  INDEX `idMale` (`idMale` ASC)  ,
  INDEX `Alarm_ibfk_1_idx` (`idAlarm` ASC)  ,
  CONSTRAINT `PeriodGestation_ibfk_1`
    FOREIGN KEY (`ID_FEMALE`)
    REFERENCES `Female` (`ID_FEMALE`)
    ON UPDATE CASCADE,
  CONSTRAINT `PeriodGestation_ibfk_2`
    FOREIGN KEY (`idMale`)
    REFERENCES `Male` (`ID_MALE`)
    ON UPDATE CASCADE,
  CONSTRAINT `PeriodGestation_ibfk_3`
    FOREIGN KEY (`idAlarm`)
    REFERENCES `Alarm` (`ID_ALARM`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `PeriodHeat`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS PeriodHeat (
  `ID_PERIOD_HEAT` SMALLINT(6) AUTO_INCREMENT NOT NULL,
  `ID_FEMALE` SMALLINT(6) NOT NULL,
  `typeMating` ENUM('Natural', 'Inseminacion') NOT NULL,
  `sincrony` ENUM('No', 'Si') NULL DEFAULT NULL,
  `DATE_START` DATE NOT NULL,
  `dateEnd` DATE NOT NULL,
  `idAlarm` SMALLINT(6) NOT NULL,
  `lastUpdate` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID_PERIOD_HEAT`, `ID_FEMALE`, `DATE_START`),
  INDEX `ID_FEMALE` (`ID_FEMALE` ASC)  ,
  INDEX `Alarm_ibfk_2_idx` (`idAlarm` ASC)  ,
  CONSTRAINT `PeriodHeat_ibfk_1`
    FOREIGN KEY (`ID_FEMALE`)
    REFERENCES `Female` (`ID_FEMALE`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
CONSTRAINT `PeriodHeat_ibfk_2`
    FOREIGN KEY (`idAlarm`)
    REFERENCES `Alarm` (`ID_ALARM`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `ArticlePerson`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS ArticlePerson (
  `ID_ARTICLE_PERSON` SMALLINT AUTO_INCREMENT NOT NULL,	
  `idArticle` TINYINT(4) NOT NULL,
  `idPerson` TINYINT(2)  UNSIGNED NOT NULL,
  `borrowedCopies` TINYINT(4) UNSIGNED NOT NULL,
  INDEX `idPerson_fk_idx` (`idPerson` ASC)  ,
  INDEX `idArticle_fk_idx` (`idArticle` ASC), 
  PRIMARY KEY (`ID_ARTICLE_PERSON`),
  CONSTRAINT `idArticle_person_fk`
    FOREIGN KEY (`idArticle`)
    REFERENCES `Article` (`ID_ARTICLE`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE,
  CONSTRAINT `idPerson_article_fk`
    FOREIGN KEY (`idPerson`)
    REFERENCES `Person` (`NO_EMPLOYEE`)
    ON DELETE RESTRICT
    ON UPDATE CASCADE)
ENGINE = InnoDB;


