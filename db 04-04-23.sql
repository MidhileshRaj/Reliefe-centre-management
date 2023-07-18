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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `allocate_manager` */

insert  into `allocate_manager`(`alct_id`,`manager_lid`,`centre_id`,`status`) values 
(1,0,0,'active');

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
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `guest` */

insert  into `guest`(`guest_id`,`guest_lid`,`name`,`email`,`phone`,`place`,`post`,`pin`,`district`,`photo`) values 
(1,0,'\"++\"','\"++\"','\"++\"','\"++\"','\"++\"',0,'\"++\"','\"++\"');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(25) NOT NULL,
  `password` varchar(25) NOT NULL,
  `type` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`username`,`password`,`type`) values 
(1,'\"++\"','\"++\"','guest'),
(2,'admin','1234','admin');

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `managers` */

/*Table structure for table `notifications` */

DROP TABLE IF EXISTS `notifications`;

CREATE TABLE `notifications` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(200) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `time` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notifications` */

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
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `relief_center` */

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
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `request` */

/*Table structure for table `volunteer` */

DROP TABLE IF EXISTS `volunteer`;

CREATE TABLE `volunteer` (
  `vol_id` int(11) NOT NULL AUTO_INCREMENT,
  `vol_lid` int(11) NOT NULL,
  `rcentre_id` int(11) DEFAULT NULL,
  `status` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`vol_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `volunteer` */

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
