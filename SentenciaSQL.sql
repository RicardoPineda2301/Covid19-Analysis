CREATE DATABASE finaldp;

USE finaldp;


CREATE TABLE `finaldp`.`confirmado` (
  `Provincia` VARCHAR(100) NULL,
  `Pais` VARCHAR(100) NULL,
  `Lat` FLOAT NULL,
  `Lon` FLOAT NULL,
  `Fecha` VARCHAR(45) NULL,
  `Casos` INT NULL);


CREATE TABLE `finaldp`.`muertes` (
  `Provincia` VARCHAR(100) NULL,
  `Pais` VARCHAR(100) NULL,
  `Lat` FLOAT NULL,
  `Lon` FLOAT NULL,
  `Fecha` VARCHAR(45) NULL,
  `Casos` INT NULL);


CREATE TABLE `finaldp`.`recuperados` (
  `Provincia` VARCHAR(100) NULL,
  `Pais` VARCHAR(100) NULL,
  `Lat` FLOAT NULL,
  `Lon` FLOAT NULL,
  `Fecha` VARCHAR(45) NULL,
  `Casos` INT NULL);
