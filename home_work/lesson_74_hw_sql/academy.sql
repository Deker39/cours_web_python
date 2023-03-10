-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: academy
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
-- Table structure for table `audience`
--

DROP TABLE IF EXISTS `audience`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `audience` (
  `id` int NOT NULL AUTO_INCREMENT,
  `number` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `audience`
--

LOCK TABLES `audience` WRITE;
/*!40000 ALTER TABLE `audience` DISABLE KEYS */;
INSERT INTO `audience` VALUES (1,'D201'),(2,'F304'),(3,'D110');
/*!40000 ALTER TABLE `audience` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `curators`
--

DROP TABLE IF EXISTS `curators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `curators` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `surname` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `curators`
--

LOCK TABLES `curators` WRITE;
/*!40000 ALTER TABLE `curators` DISABLE KEYS */;
INSERT INTO `curators` VALUES (1,'Dave','McQueen'),(2,'Jack','Underhill'),(3,'Tommy ','Hilfiger');
/*!40000 ALTER TABLE `curators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `departments`
--

DROP TABLE IF EXISTS `departments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `departments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `building` int NOT NULL,
  `financing` float(10,2) unsigned NOT NULL DEFAULT '0.00',
  `name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `facultyId` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `departments_ibfk_1_idx` (`facultyId`),
  CONSTRAINT `departments_ibfk_1` FOREIGN KEY (`facultyId`) REFERENCES `faculties` (`id`),
  CONSTRAINT `departments_chk_1` CHECK ((`building` between 1 and 5))
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `departments`
--

LOCK TABLES `departments` WRITE;
/*!40000 ALTER TABLE `departments` DISABLE KEYS */;
INSERT INTO `departments` VALUES (1,1,100.50,'Software Development',1),(2,2,50.00,'Electrician Development',2),(3,2,200.00,'Languages ',4);
/*!40000 ALTER TABLE `departments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculties`
--

DROP TABLE IF EXISTS `faculties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculties` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculties`
--

LOCK TABLES `faculties` WRITE;
/*!40000 ALTER TABLE `faculties` DISABLE KEYS */;
INSERT INTO `faculties` VALUES (1,'Computer Science'),(3,'Energy Institute'),(2,'Institute for the Humanities'),(4,'Ukrainian-Spanish Institute');
/*!40000 ALTER TABLE `faculties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groups` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `year` int NOT NULL,
  `departmentId` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  KEY `departmentId` (`departmentId`),
  CONSTRAINT `groups_ibfk_1` FOREIGN KEY (`departmentId`) REFERENCES `departments` (`id`),
  CONSTRAINT `groups_chk_1` CHECK ((`year` between 1 and 5))
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
INSERT INTO `groups` VALUES (1,'281',2,1),(2,'462',4,2),(3,'331',1,1),(4,'522',5,1);
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups_curators`
--

DROP TABLE IF EXISTS `groups_curators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groups_curators` (
  `id` int NOT NULL AUTO_INCREMENT,
  `curatorId` int NOT NULL,
  `groupId` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `curatorId` (`curatorId`),
  KEY `groupId` (`groupId`),
  CONSTRAINT `groups_curators_ibfk_1` FOREIGN KEY (`curatorId`) REFERENCES `curators` (`id`),
  CONSTRAINT `groups_curators_ibfk_2` FOREIGN KEY (`groupId`) REFERENCES `groups` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups_curators`
--

LOCK TABLES `groups_curators` WRITE;
/*!40000 ALTER TABLE `groups_curators` DISABLE KEYS */;
INSERT INTO `groups_curators` VALUES (1,1,1),(2,1,2),(3,2,3),(4,2,4),(5,1,4);
/*!40000 ALTER TABLE `groups_curators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups_lectures`
--

DROP TABLE IF EXISTS `groups_lectures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groups_lectures` (
  `id` int NOT NULL AUTO_INCREMENT,
  `groupId` int NOT NULL,
  `lectureId` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `groupId` (`groupId`),
  KEY `lectureId` (`lectureId`),
  CONSTRAINT `groups_lectures_ibfk_1` FOREIGN KEY (`groupId`) REFERENCES `groups` (`id`),
  CONSTRAINT `groups_lectures_ibfk_2` FOREIGN KEY (`lectureId`) REFERENCES `lectures` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups_lectures`
--

LOCK TABLES `groups_lectures` WRITE;
/*!40000 ALTER TABLE `groups_lectures` DISABLE KEYS */;
INSERT INTO `groups_lectures` VALUES (1,1,1),(2,1,2),(3,2,3),(4,3,4),(5,4,5),(6,4,6);
/*!40000 ALTER TABLE `groups_lectures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups_students`
--

DROP TABLE IF EXISTS `groups_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groups_students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `groupId` int NOT NULL,
  `studentId` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `groupId` (`groupId`),
  KEY `studentId` (`studentId`),
  CONSTRAINT `groups_students_ibfk_1` FOREIGN KEY (`groupId`) REFERENCES `groups` (`id`),
  CONSTRAINT `groups_students_ibfk_2` FOREIGN KEY (`studentId`) REFERENCES `students` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups_students`
--

LOCK TABLES `groups_students` WRITE;
/*!40000 ALTER TABLE `groups_students` DISABLE KEYS */;
INSERT INTO `groups_students` VALUES (1,1,1),(2,1,2),(3,2,3),(4,2,4),(5,3,5),(6,4,6),(7,4,7);
/*!40000 ALTER TABLE `groups_students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `lectures`
--

DROP TABLE IF EXISTS `lectures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `lectures` (
  `id` int NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `subjectId` int NOT NULL,
  `teacherId` int NOT NULL,
  `audienceId` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `subjectId` (`subjectId`),
  KEY `teacherId` (`teacherId`) /*!80000 INVISIBLE */,
  KEY `audienceId` (`audienceId`),
  CONSTRAINT `lectures_ibfk_1` FOREIGN KEY (`subjectId`) REFERENCES `subjects` (`id`),
  CONSTRAINT `lectures_ibfk_2` FOREIGN KEY (`teacherId`) REFERENCES `teachers` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `lectures`
--

LOCK TABLES `lectures` WRITE;
/*!40000 ALTER TABLE `lectures` DISABLE KEYS */;
INSERT INTO `lectures` VALUES (1,'2023-03-03',1,1,1),(2,'2023-03-03',2,2,1),(3,'2023-03-02',1,3,2),(4,'2023-02-04',3,1,3),(5,'2023-03-08',4,1,3),(6,'2023-03-07',1,3,2);
/*!40000 ALTER TABLE `lectures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `students`
--

DROP TABLE IF EXISTS `students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `rating` int NOT NULL,
  `surname` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `students_chk_1` CHECK ((`rating` between 1 and 5))
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `students`
--

LOCK TABLES `students` WRITE;
/*!40000 ALTER TABLE `students` DISABLE KEYS */;
INSERT INTO `students` VALUES (1,'Alex',4,'Kinth'),(2,'Mariya',3,'Kenzi'),(3,'Deker',1,'Smoth'),(4,'Ben',5,'Almond'),(5,'Kevin',2,'Mobius'),(6,'Ide',1,'Morzi'),(7,'Dinkan',4,'Rob');
/*!40000 ALTER TABLE `students` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subjects`
--

DROP TABLE IF EXISTS `subjects`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `subjects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subjects`
--

LOCK TABLES `subjects` WRITE;
/*!40000 ALTER TABLE `subjects` DISABLE KEYS */;
INSERT INTO `subjects` VALUES (4,'english'),(3,'literature'),(1,'mathematics'),(2,'physics');
/*!40000 ALTER TABLE `subjects` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `teachers`
--

DROP TABLE IF EXISTS `teachers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `teachers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `IsProfessor` bit(1) NOT NULL DEFAULT b'0',
  `name` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  `salary` float(10,2) unsigned NOT NULL DEFAULT '0.00',
  `surname` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `teachers`
--

LOCK TABLES `teachers` WRITE;
/*!40000 ALTER TABLE `teachers` DISABLE KEYS */;
INSERT INTO `teachers` VALUES (1,_binary '\0','Dave',100.00,'McQueen'),(2,_binary '','Tommy ',500.00,'Hilfiger'),(3,_binary '','Jack',300.00,'Underhill');
/*!40000 ALTER TABLE `teachers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-03-10 22:22:17
