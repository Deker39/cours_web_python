create database `academy`;
create table if not exists `academy`.`curators`(`id` int auto_increment primary key not null,
												`name` nvarchar(255) not null,
												`surname` nvarchar(255) not null);
create table if not exists `academy`.`faculties`(`id` int auto_increment primary key not null,
												`name` nvarchar(100) not null unique);										
create table if not exists `academy`.`departments`(`id` int auto_increment primary key not null,
												`building` int(5) not null ,
												`financing` float(10,2) unsigned default 0 not null,
												`name` nvarchar(100) not null unique,
												`facultyId` int not null,
												check(`building` between 1 and 5),
												foreign key (`facultyId`) references `faculties`(`id`));
create table if not exists `academy`.`groups`(`id` int auto_increment primary key not null,
												`name` nvarchar(10) not null unique,
                                                `year` int not null,
                                                `departmentId` int not null, 
                                                check(`year` between 1 and 5),
                                                foreign key (`departmentId`) references `departments`(`id`));
create table if not exists `academy`.`subjects`(`id` int auto_increment primary key not null,
												`name` nvarchar(100) unique not null);        
create table if not exists `academy`.`students`(`id` int auto_increment primary key not null,
												`name` nvarchar(255) not null,
                                                `rating` int not null,
                                                `surname` nvarchar(255) not null, 
                                                check(`rating` between 1 and 5));	  
create table if not exists `academy`.`teachers`(`id` int auto_increment primary key not null,
												`IsProfessor` bit default 0 not null,
                                                `name` nvarchar(255) not null,
												`salary` float(10,2) unsigned default 0 not null,
												`surname` nvarchar(255) not null);	
create table if not exists `academy`.`audience`(`id` int auto_increment primary key not null,
												`number` nvarchar(100) not null);
create table if not exists `academy`.`lectures`(`id` int auto_increment primary key not null,
												`date` date not null,
                                                `subjectId` int not null,
                                                `teacherId` int not null, 
                                                `audienceId` int not null, 
                                                foreign key (`subjectId`) references `subjects`(`id`),
                                                foreign key (`teacherId`) references `teachers`(`id`),
                                                foreign key (`audienceId`) references `audience`(`id`));		
create table if not exists `academy`.`groups_curators`(`id` int auto_increment primary key not null,
												`curatorId` int not null,
                                                `groupId` int not null,
                                                foreign key (`curatorId`) references `curators`(`id`),
                                                foreign key (`groupId`) references `groups`(`id`));		
create table if not exists `academy`.`groups_lectures`(`id` int auto_increment primary key not null,
												`groupId` int not null,
                                                `lectureId` int not null,
                                                foreign key (`groupId`) references `groups`(`id`),
                                                foreign key (`lectureId`) references `lectures`(`id`));		
create table if not exists `academy`.`groups_students`(`id` int auto_increment primary key not null,
												`groupId` int not null,
                                                `studentId` int not null,
                                                foreign key (`groupId`) references `groups`(`id`),
                                                foreign key (`studentId`) references `students`(`id`));	
                                                 
                                                 
-- Query 1.1
SELECT  count(*) FROM academy.groups_lectures  
join academy.groups on groups_lectures.groupId = academy.groups.id 
join academy.departments on academy.groups.id  = academy.departments.id
join academy.lectures on groups_lectures.lectureId = academy.lectures.id
join academy.teachers on academy.lectures.teacherId = teachers.id where departments.name = "Software Development" 
-- Query 1.2
select count(*) from academy.lectures
join academy.teachers on academy.lectures.teacherId = academy.teachers.id 
where academy.teachers.name = "Dave" and  academy.teachers.surname = "McQueen"
-- Query 1.3
SELECT count(*) FROM academy.lectures
join academy.audience on academy.lectures.audienceId = academy.audience.id
where academy.audience.number = "D201"
-- Query 1.4
SELECT academy.audience.number, count( academy.audience.id)  as count  FROM academy.lectures
join academy.audience on academy.lectures.audienceId = academy.audience.id group by academy.audience.number
-- Query 1.5
select academy.teachers.name, academy.teachers.surname, count(academy.students.id) as count from academy.groups_lectures
join academy.groups on groups_lectures.groupId = academy.groups.id 
join academy.groups_students on academy.groups.id = academy.groups_students.groupId
join academy.students on academy.groups_students.studentId = academy.students.id
join academy.lectures on groups_lectures.lectureId = academy.lectures.id
join academy.teachers on academy.lectures.teacherId = academy.teachers.id 
where academy.teachers.name = "Jack" and  academy.teachers.surname = "Underhill" 
-- Query 1.6
SELECT  academy.faculties.name, avg(academy.teachers.salary) as avg_salary FROM academy.groups_lectures  
join academy.groups on groups_lectures.groupId = academy.groups.id 
join academy.departments on academy.groups.id  = academy.departments.id
join academy.lectures on groups_lectures.lectureId = academy.lectures.id
join academy.teachers on academy.lectures.teacherId = academy.teachers.id 
join academy.faculties on academy.departments.facultyId = academy.faculties.id
where academy.faculties.name = "Computer Science"
-- Query 1.7
select  min(amount) as min_students, max(amount) as max_students, count(name) as amount_groups from (
SELECT academy.groups.name, count(*) as amount FROM academy.groups_students
join academy.students on  academy.groups_students.studentId = academy.students.id
join academy.groups on  academy.groups_students.groupId = academy.groups.id  group by academy.groups.name
) t 
-- Query 1.8
SELECT avg(academy.departments.financing) FROM academy.departments;
-- Query 1.9
select academy.teachers.name, academy.teachers.surname, count(academy.lectures.teacherId) as count from academy.lectures
join academy.teachers on academy.lectures.teacherId = academy.teachers.id 
group by academy.teachers.id
-- Query 1.10
SELECT DAYNAME(date) AS day, COUNT(*) AS count FROM academy.lectures GROUP BY day
-- Query 1.11
SELECT academy.audience.number, count(academy.groups.departmentId) FROM academy.lectures
join academy.audience on academy.lectures.audienceId = academy.audience.id
join academy.groups_lectures on academy.lectures.id = academy.groups_lectures.lectureId
join academy.groups on academy.groups.id = academy.groups_lectures.groupId
join academy.departments on academy.departments.id = academy.groups.departmentId
group by academy.audience.number
-- Query 1.12
SELECT academy.faculties.name, count(academy.subjects.id) FROM academy.lectures
join academy.subjects on academy.subjects.id = academy.lectures.subjectId
join academy.groups_lectures on academy.lectures.id = academy.groups_lectures.lectureId
join academy.groups on  academy.groups.id = academy.groups_lectures.groupId
join academy.departments on academy.departments.id = academy.groups.departmentId
join academy.faculties on academy.faculties.id = academy.departments.facultyId group by academy.faculties.name
-- Query 1.13
SELECT academy.audience.number, count(academy.lectures.subjectId)  as lectures, count(academy.teachers.id) as teachers FROM academy.lectures
join academy.audience on academy.audience.id = academy.lectures.audienceId
join academy.teachers on academy.teachers.id = academy.lectures.teacherId
group by academy.audience.number