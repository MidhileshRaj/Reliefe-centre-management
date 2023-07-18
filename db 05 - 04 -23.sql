  /*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - rcm
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`rcm` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `rcm`;

/*Table structure for table `allocate_manager` */

DROP TABLE IF EXISTS `allocate_manager`;

CREATE TABLE `allocate_manager` (
  `alct_id` int(11) NOT NULL AUTO_INCREMENT,
  `manager_lid` int(11) NOT NULL,
  `centre_id` int(11) DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`alct_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `allocate_manager` */

insert  into `allocate_manager`(`alct_id`,`manager_lid`,`centre_id`,`status`) values 
(1,0,0,'active'),
(3,4,3,'active'),
(4,4,4,'active'),
(5,5,5,'active'),
(6,4,6,'active'),
(7,4,7,'active'),
(8,5,8,'active');

/*Table structure for table `bank` */

DROP TABLE IF EXISTS `bank`;

CREATE TABLE `bank` (
  `bank_id` int(11) NOT NULL AUTO_INCREMENT,
  `bank_name` varchar(25) DEFAULT NULL,
  `account_no` int(11) DEFAULT NULL,
  `ifcs_code` varchar(20) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `balance` int(11) DEFAULT NULL,
  PRIMARY KEY (`bank_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `bank` */

insert  into `bank`(`bank_id`,`bank_name`,`account_no`,`ifcs_code`,`pin`,`balance`) values 
(1,'SBI',11223344,'SBI1234',1212,100000);

/*Table structure for table `donation` */

DROP TABLE IF EXISTS `donation`;

CREATE TABLE `donation` (
  `donation_id` int(11) NOT NULL AUTO_INCREMENT,
  `amount` int(11) DEFAULT NULL,
  `account_no` int(11) DEFAULT NULL,
  `guest_lid` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`donation_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `donation` */

insert  into `donation`(`donation_id`,`amount`,`account_no`,`guest_lid`,`date`) values 
(1,0,0,0,'2023-04-06'),
(2,100000,11223344,8,'2023-04-06'),
(3,1234,11223344,8,'2023-04-06');

/*Table structure for table `feedback` */

DROP TABLE IF EXISTS `feedback`;

CREATE TABLE `feedback` (
  `feedback_id` int(11) NOT NULL AUTO_INCREMENT,
  `guest_lid` int(11) DEFAULT NULL,
  `feedback` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`feedback_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `feedback` */

/*Table structure for table `guest` */

DROP TABLE IF EXISTS `guest`;

CREATE TABLE `guest` (
  `guest_id` int(11) NOT NULL AUTO_INCREMENT,
  `guest_lid` int(11) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` varchar(10) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `post` varchar(25) DEFAULT NULL,
  `pin` int(7) DEFAULT NULL,
  `district` varchar(25) DEFAULT NULL,
  `photo` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`guest_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `guest` */

insert  into `guest`(`guest_id`,`guest_lid`,`name`,`email`,`phone`,`place`,`post`,`pin`,`district`,`photo`) values 
(1,0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"','\"++\"'),
(2,6,'G','g@gmaul.com','1234','place','[post',1234,'dis','/static/guest/20230405-022544.jpg'),
(3,7,'g2','g2@gmail.com','1234','oo','oo',111,'d','/static/guest/20230405-022609.jpg'),
(4,8,' Guest',' g3@gmail.com',' 1111',' place',' post',0,' dis','/static/guest/20230406-004304.jpg');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `type` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'\"++\"','\"++\"','guest'),
(2,'admin','1234','admin'),
(4,'m@gmail.com','1234','manager'),
(5,'m2@gmail.com','1234','manager'),
(6,'g@gmail.com','1234','volunteer'),
(7,'g2@gmail.com','1234','volunteer'),
(8,' g3@gmail.com','1111','guest');

/*Table structure for table `managers` */

DROP TABLE IF EXISTS `managers`;

CREATE TABLE `managers` (
  `manager_id` int(11) NOT NULL AUTO_INCREMENT,
  `lid` int(11) NOT NULL,
  `name` varchar(25) DEFAULT NULL,
  `dob` varchar(25) DEFAULT NULL,
  `gender` varchar(25) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `phone` bigint(11) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `post` varchar(25) DEFAULT NULL,
  `district` varchar(25) DEFAULT NULL,
  `photo` varchar(300) DEFAULT NULL,
  PRIMARY KEY (`manager_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `managers` */

insert  into `managers`(`manager_id`,`lid`,`name`,`dob`,`gender`,`email`,`phone`,`place`,`post`,`district`,`photo`) values 
(3,4,'manager','2023-04-04','Male','m@gmail.com',1234,'place','post','dis','/static/manager/20230405-015205.jpg'),
(4,5,'manager2','2023-04-06','Female','m2@gmail.com',1234,'place','post','dis','/static/manager/20230405-015234.jpg');

/*Table structure for table `notifications` */

DROP TABLE IF EXISTS `notifications`;

CREATE TABLE `notifications` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `notifications` */

insert  into `notifications`(`notification_id`,`notification`,`date`,`time`) values 
(3,'new','2023-04-05','02:14:43');

/*Table structure for table `public_donation` */

DROP TABLE IF EXISTS `public_donation`;

CREATE TABLE `public_donation` (
  `did` int(11) NOT NULL AUTO_INCREMENT,
  `account_no` int(11) DEFAULT NULL,
  `amount` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`did`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `public_donation` */

insert  into `public_donation`(`did`,`account_no`,`amount`,`date`) values 
(1,0,0,'2023-04-06');

/*Table structure for table `refugees` */

DROP TABLE IF EXISTS `refugees`;

CREATE TABLE `refugees` (
  `rid` int(11) NOT NULL AUTO_INCREMENT,
  `rname` varchar(25) DEFAULT NULL,
  `gender` varchar(25) DEFAULT NULL,
  `address` varchar(100) DEFAULT NULL,
  `age` int(11) DEFAULT NULL,
  `vol_lid` int(11) DEFAULT NULL,
  PRIMARY KEY (`rid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `refugees` */

insert  into `refugees`(`rid`,`rname`,`gender`,`address`,`age`,`vol_lid`) values 
(1,'\"++\"','\"++\"','\"++\"',0,0),
(3,'wqs','Male','wrfg',66,6),
(4,'dd','Other','dqa',33,6);

/*Table structure for table `relief_center` */

DROP TABLE IF EXISTS `relief_center`;

CREATE TABLE `relief_center` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(25) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `post` varchar(25) DEFAULT NULL,
  `district` varchar(25) DEFAULT NULL,
  `fecilities` varchar(25) DEFAULT NULL,
  `no_of_volunteers` int(11) DEFAULT NULL,
  `pin` varchar(25) DEFAULT NULL,
  `max_occupancy` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `relief_center` */

insert  into `relief_center`(`id`,`name`,`place`,`post`,`district`,`fecilities`,`no_of_volunteers`,`pin`,`max_occupancy`) values 
(7,'rc2','pla','','','',0,'',0),
(8,'rc3','pla','kn','h','jhb',10,'kkj',1111);

/*Table structure for table `request` */

DROP TABLE IF EXISTS `request`;

CREATE TABLE `request` (
  `req_id` int(11) NOT NULL AUTO_INCREMENT,
  `item` varchar(25) DEFAULT NULL,
  `type` varchar(25) DEFAULT NULL,
  `details` varchar(25) DEFAULT NULL,
  `manager_lid` int(11) DEFAULT NULL,
  `rcentre_id` int(11) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`req_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `request` */

insert  into `request`(`req_id`,`item`,`type`,`details`,`manager_lid`,`rcentre_id`,`date`,`status`) values 
(1,'\"++\"','\"++\"','\"++\"',0,0,'2023-04-05','pending'),
(2,'dress','kids and women','ghfwhsgqvjhsv',4,6,'2023-04-05','pending'),
(3,'medicine','sugar patient','gfhgfh',4,6,'2023-04-05','pending');

/*Table structure for table `task` */

DROP TABLE IF EXISTS `task`;

CREATE TABLE `task` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vol_lid` int(11) NOT NULL,
  `task` varchar(100) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `task` */

insert  into `task`(`id`,`vol_lid`,`task`,`date`,`status`) values 
(1,0,'\"++\"','2023-04-05','pending'),
(2,7,'xsasx','2023-04-05','pending'),
(4,6,'jgv','2023-04-05','Task completed');

/*Table structure for table `volunteer` */

DROP TABLE IF EXISTS `volunteer`;

CREATE TABLE `volunteer` (
  `vol_id` int(11) NOT NULL AUTO_INCREMENT,
  `vol_lid` int(11) NOT NULL,
  `rcentre_id` int(11) DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`vol_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `volunteer` */

insert  into `volunteer`(`vol_id`,`vol_lid`,`rcentre_id`,`status`) values 
(1,6,6,'approved'),
(2,7,7,'approved'),
(3,8,6,'pending');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
