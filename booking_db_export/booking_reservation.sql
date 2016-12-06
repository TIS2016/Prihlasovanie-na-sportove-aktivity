-- MySQL dump 10.13  Distrib 5.7.12, for Win32 (AMD64)
--
-- Host: localhost    Database: booking
-- ------------------------------------------------------
-- Server version	5.7.16-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `reservation`
--

DROP TABLE IF EXISTS `reservation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `reservation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `login` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  `surname` varchar(50) NOT NULL,
  `date` date NOT NULL,
  `time` varchar(100) NOT NULL,
  `note` varchar(100) NOT NULL,
  `is_blocked` tinyint(1) NOT NULL,
  `room_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `reservation_8273f993` (`room_id`),
  CONSTRAINT `reservation_room_id_fb29c782_fk_rooms_id` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reservation`
--

LOCK TABLES `reservation` WRITE;
/*!40000 ALTER TABLE `reservation` DISABLE KEYS */;
INSERT INTO `reservation` VALUES (7,'reguly3','asdf','asdfasdf','2016-11-28','10:30-11:00','sdafsadf',0,1),(9,'admin','asdasd','asdasdd','2016-11-28','10:30-11:00','asdasda',0,1),(10,'asfasffsafasf','asfasf','asfsaf','2016-11-28','11:00-11:30','asf',0,2),(11,'af','asd','asdasd','2016-11-29','08:00-08:30','asd',0,1),(23,'user_login','user_name','user_surname','2016-12-15','08:30-09:00','',0,1),(25,'user_login','user_name','user_surname','2016-12-14','08:00-08:30','',0,1),(31,'user_login','user_name','user_surname','2016-11-28','10:30-11:00','gabaj',0,1),(33,'user_login','user_name','user_surname','2016-12-05','08:00-08:30','erehr',0,1),(35,'user_login','user_name','user_surname','2016-11-28','08:00-08:30','bemsdgsdg',0,1),(36,'user_login','user_name','user_surname','2016-12-06','08:30-09:00','rehrehtr',0,1),(37,'user_login','user_name','user_surname','2016-12-05','08:30-09:00','rhtrth',0,1),(39,'user_login','user_name','user_surname','2016-12-05','09:30-10:00','htrthht',0,1),(40,'user_login','user_name','user_surname','2016-12-05','10:00-10:30','hththtththh',0,1),(41,'user_login','user_name','user_surname','2016-12-13','09:30-10:00','kkk',0,1),(42,'user_login','user_name','user_surname','2016-12-06','08:00-08:30','55',0,1);
/*!40000 ALTER TABLE `reservation` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-12-06 11:06:11
