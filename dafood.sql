-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Apr 17, 2023 at 04:21 PM
-- Server version: 10.4.28-MariaDB
-- PHP Version: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `food`
--

-- --------------------------------------------------------

--
-- Table structure for table `dafood`
--

CREATE TABLE `dafood` (
  `food_ID` varchar(10) NOT NULL,
  `food_Name` varchar(20) NOT NULL,
  `country_F` varchar(15) NOT NULL,
  `food_Price` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_general_ci;

--
-- Dumping data for table `dafood`
--

INSERT INTO `dafood` (`food_ID`, `food_Name`, `country_F`, `food_Price`) VALUES
('DF01', 'Pad Vietna', 'Vietnam', '50.00'),
('DF02', 'Pad Thai', 'Thailand', '55.00'),
('DF03', 'Pad China', 'England', '60.00'),
('DF04', 'Pad Turkey', 'Turkey', '45.00');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `dafood`
--
ALTER TABLE `dafood`
  ADD PRIMARY KEY (`food_ID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
