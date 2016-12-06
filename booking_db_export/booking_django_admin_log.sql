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
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-11-15 15:00:04.033663','1','admin',1,'[{\"added\": {}}]',1,1),(2,'2016-11-15 19:52:06.388050','1','hala',1,'[{\"added\": {}}]',2,1),(3,'2016-11-21 17:30:33.618114','2','reguly3:hala-2016-11-21-10:00 - 10:30-sali je gabaj',1,'[{\"added\": {}}]',3,1),(4,'2016-11-21 17:58:34.884905','3','asdf:hala-2016-11-21-13:30-14:00-gaabj',1,'[{\"added\": {}}]',3,1),(5,'2016-11-21 17:58:56.337403','4','qweqwe:hala-2016-11-21-10:30-11:00-gabgaj',1,'[{\"added\": {}}]',3,1),(6,'2016-11-21 17:59:16.458860','5','afs:hala-2016-11-21-17:00-17:30-gabaj',1,'[{\"added\": {}}]',3,1),(7,'2016-11-27 21:11:54.275428','5','afs:hala-2016-11-21-17:00-17:30-True',2,'[]',3,1),(8,'2016-11-27 21:15:25.236915','6','reguly3:hala-2016-11-27-10:00 - 10:30-False',1,'[{\"added\": {}}]',3,1),(9,'2016-11-27 21:18:53.037007','6','reguly3:hala-2016-11-27-10:00 - 10:30-False',3,'',3,1),(10,'2016-11-27 21:18:53.041012','5','afs:hala-2016-11-21-17:00-17:30-True',3,'',3,1),(11,'2016-11-27 21:18:53.043455','4','qweqwe:hala-2016-11-21-10:30-11:00-False',3,'',3,1),(12,'2016-11-27 21:18:53.045457','3','asdf:hala-2016-11-21-13:30-14:00-False',3,'',3,1),(13,'2016-11-27 21:18:53.049460','2','reguly3:hala-2016-11-21-10:00 - 10:30-False',3,'',3,1),(14,'2016-11-27 21:19:08.064140','7','reguly3:hala-2016-11-27-10:30-11:00-False',1,'[{\"added\": {}}]',3,1),(15,'2016-11-27 21:19:33.790616','8','ortut:hala-2016-11-27-08:00-08:30-True',1,'[{\"added\": {}}]',3,1),(16,'2016-11-27 21:19:56.446259','9','admin:hala-2016-11-27-10:30-11:00-False',1,'[{\"added\": {}}]',3,1),(17,'2016-11-27 21:22:38.010538','9','admin:hala-2016-11-28-10:30-11:00-False',2,'[{\"changed\": {\"fields\": [\"date\"]}}]',3,1),(18,'2016-11-27 21:22:42.214218','8','ortut:hala-2016-11-28-08:00-08:30-True',2,'[{\"changed\": {\"fields\": [\"date\"]}}]',3,1),(19,'2016-11-27 21:22:46.772009','7','reguly3:hala-2016-11-28-10:30-11:00-False',2,'[{\"changed\": {\"fields\": [\"date\"]}}]',3,1),(20,'2016-11-28 18:43:03.511000','2','stena',1,'[{\"added\": {}}]',2,1),(21,'2016-11-28 18:43:19.726000','10','asfasffsafasf:stena-2016-11-28-11:00-11:30-False',1,'[{\"added\": {}}]',3,1),(22,'2016-11-29 22:39:39.626000','11','af:hala-2016-11-29-08:00-08:30-False',1,'[{\"added\": {}}]',3,1),(23,'2016-12-03 17:31:08.564000','15','user_login:hala-2016-10-02-09:00-09:30-False',3,'',3,1),(24,'2016-12-03 17:31:08.569000','14','user_login:hala-2016-10-02-08:30-09:00-False',3,'',3,1),(25,'2016-12-03 17:31:08.572000','13','user_login:hala-2016-10-01-Pondelok 09:00-09:30-False',3,'',3,1),(26,'2016-12-03 17:31:08.574000','12','user_login:hala-2016-10-01-Pondelok 08:30-09:00-False',3,'',3,1),(27,'2016-12-04 00:29:08.788000','19','user_login:hala-2016-12-01-08:30-09:00-False',3,'',3,1),(28,'2016-12-04 00:29:08.793000','18','user_login:hala-2016-11-29-08:30-09:00-False',3,'',3,1),(29,'2016-12-04 00:29:08.795000','17','user_login:hala-2016-10-02-08:30-09:00-False',3,'',3,1),(30,'2016-12-04 00:29:08.798000','16','user_login:hala-2016-10-02-08:30-09:00-False',3,'',3,1),(31,'2016-12-04 00:35:35.243000','21','user_login:hala-2016-12-01-08:30-09:00-False',3,'',3,1),(32,'2016-12-04 00:35:35.248000','20','user_login:hala-2016-11-29-08:30-09:00-False',3,'',3,1),(33,'2016-12-04 12:27:51.340000','2','stena',2,'[{\"changed\": {\"fields\": [\"capacity\"]}}]',2,1),(34,'2016-12-04 12:28:04.043000','3','sauna',1,'[{\"added\": {}}]',2,1),(35,'2016-12-04 12:28:12.419000','4','posilnovna',1,'[{\"added\": {}}]',2,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
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
