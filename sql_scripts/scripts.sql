CREATE TABLE `personinfodb`.`personinfo` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(85) NOT NULL,
  `age` INT NOT NULL,
  `salary` INT NOT NULL,
  PRIMARY KEY (`id`));

INSERT INTO `personinfodb`.`personinfo`(`id`,`name`,`age`,`salary`) VALUES(0,'bal',23,200);