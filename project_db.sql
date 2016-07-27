-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema project_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema project_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `project_db` DEFAULT CHARACTER SET utf8 ;
USE `project_db` ;

-- -----------------------------------------------------
-- Table `project_db`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_db`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `fb_id` TEXT NULL,
  `fb_token` TEXT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_db`.`locations`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_db`.`locations` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(255) NULL,
  `address` VARCHAR(255) NULL,
  `city` VARCHAR(255) NULL,
  `latitude` VARCHAR(45) NULL,
  `longitude` VARCHAR(45) NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_db`.`favorites`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_db`.`favorites` (
  `user_id` INT NOT NULL,
  `location_id` INT NOT NULL,
  INDEX `fk_users_has_locations_locations1_idx` (`location_id` ASC),
  INDEX `fk_users_has_locations_users_idx` (`user_id` ASC),
  CONSTRAINT `fk_users_has_locations_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `project_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_locations_locations1`
    FOREIGN KEY (`location_id`)
    REFERENCES `project_db`.`locations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `project_db`.`reviews`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `project_db`.`reviews` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `location_id` INT NOT NULL,
  `content` TEXT NULL,
  `rating` INT NULL,
  `created_at` DATETIME NULL,
  `updated_at` DATETIME NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_users_has_locations_locations2_idx` (`location_id` ASC),
  INDEX `fk_users_has_locations_users1_idx` (`user_id` ASC),
  CONSTRAINT `fk_users_has_locations_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `project_db`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_users_has_locations_locations2`
    FOREIGN KEY (`location_id`)
    REFERENCES `project_db`.`locations` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
