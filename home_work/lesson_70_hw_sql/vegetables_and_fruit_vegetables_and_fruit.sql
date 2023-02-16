-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: vegetables_and_fruit
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vegetables_and_fruit`
--

DROP TABLE IF EXISTS `vegetables_and_fruit`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vegetables_and_fruit` (
  `id` int NOT NULL AUTO_INCREMENT,
  `fruit_name` varchar(100) NOT NULL,
  `fruit_type` varchar(100) DEFAULT NULL,
  `color` varchar(100) DEFAULT NULL,
  `caloric_content` float DEFAULT NULL,
  `fruit_description` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `CHK_fruit_type` CHECK (((`fruit_type` = _utf8mb4'vegetable') or (`fruit_type` = _utf8mb4'fruit')))
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vegetables_and_fruit`
--

LOCK TABLES `vegetables_and_fruit` WRITE;
/*!40000 ALTER TABLE `vegetables_and_fruit` DISABLE KEYS */;
INSERT INTO `vegetables_and_fruit` VALUES (7,'apple','fruit','red',225,'very sweet and healthy'),(8,'orange','fruit','orange',111,'very sour and healthy'),(9,'potato','vegetable','white-yellow',50,'healthy'),(10,'corn','vegetable','yellow',50,'healthy'),(11,'melon','fruit','yellow',350,'healthy and to more water'),(12,'watermelon','fruit','green',15,'healthy and to more water');
/*!40000 ALTER TABLE `vegetables_and_fruit` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-02-14 20:46:21
