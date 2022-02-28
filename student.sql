-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 28, 2022 at 01:53 PM
-- Server version: 10.4.22-MariaDB
-- PHP Version: 8.1.2

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `student`
--

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `ROLL` int(11) NOT NULL,
  `NAME` varchar(100) NOT NULL,
  `GENDER` varchar(100) NOT NULL,
  `CONTACT` varchar(100) NOT NULL,
  `DOB` date NOT NULL,
  `ADDRESS` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`ROLL`, `NAME`, `GENDER`, `CONTACT`, `DOB`, `ADDRESS`) VALUES
(1234, 'Rafie', 'Male', '82111360417', '2021-08-21', 'Bintara'),
(1245, 'Akmal', 'Male', '82345656577', '2021-08-22', 'Bintara'),
(1246, 'Pandu', 'Male', '82545657886', '2021-08-22', 'Cikarang'),
(1247, 'Bob', 'Male', '82353646755', '2021-08-23', 'Cakung'),
(1248, 'Agus', 'Female', '82353646767', '2021-08-23', 'Depok');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
