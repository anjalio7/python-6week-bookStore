-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Aug 26, 2022 at 01:23 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `book_shop`
--

-- --------------------------------------------------------

--
-- Table structure for table `addbooks`
--

CREATE TABLE `addbooks` (
  `id` int(50) NOT NULL,
  `BookName` varchar(50) NOT NULL,
  `BookCategory` int(255) NOT NULL,
  `BookAuthor` varchar(50) NOT NULL,
  `BookPrice` int(50) NOT NULL,
  `RackNoColumn` int(255) NOT NULL,
  `Stock` int(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addbooks`
--

INSERT INTO `addbooks` (`id`, `BookName`, `BookCategory`, `BookAuthor`, `BookPrice`, `RackNoColumn`, `Stock`) VALUES
(8, 'pytossd', 2, 'rere', 60, 2, 10),
(9, 'python0', 2, 'rere', 55, 2, 66),
(12, 'Beloved', 3, 'Toni Morris', 110, 2, 8);

-- --------------------------------------------------------

--
-- Table structure for table `addemployee`
--

CREATE TABLE `addemployee` (
  `id` int(11) NOT NULL,
  `Name` varchar(50) NOT NULL,
  `Email` varchar(50) NOT NULL,
  `PhoneNo` int(12) NOT NULL,
  `UserName` varchar(50) NOT NULL,
  `Password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addemployee`
--

INSERT INTO `addemployee` (`id`, `Name`, `Email`, `PhoneNo`, `UserName`, `Password`) VALUES
(2, 'japjeet', 'japjeet@gmail.com', 2147483647, 'japjeet', '12345678'),
(4, 'sourav', 'sourav@gmail.com', 1234567899, 'sourav', '123456');

-- --------------------------------------------------------

--
-- Table structure for table `addracks`
--

CREATE TABLE `addracks` (
  `id` int(11) NOT NULL,
  `RackName` varchar(50) NOT NULL,
  `NoOfRows` int(11) NOT NULL,
  `TotalCapacity` int(11) NOT NULL,
  `CapacityPerRow` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `addracks`
--

INSERT INTO `addracks` (`id`, `RackName`, `NoOfRows`, `TotalCapacity`, `CapacityPerRow`) VALUES
(2, 'A', 5, 50, 10);

-- --------------------------------------------------------

--
-- Table structure for table `adminlogin`
--

CREATE TABLE `adminlogin` (
  `id` int(11) NOT NULL,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `adminlogin`
--

INSERT INTO `adminlogin` (`id`, `username`, `password`) VALUES
(1, 'admin', '12345678');

-- --------------------------------------------------------

--
-- Table structure for table `categories`
--

CREATE TABLE `categories` (
  `id` int(11) NOT NULL,
  `Categories` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` (`id`, `Categories`) VALUES
(1, 'FICTION'),
(2, 'HORROR'),
(3, 'fiction'),
(4, 'fii'),
(5, 'Historical'),
(6, 'Political');

-- --------------------------------------------------------

--
-- Table structure for table `orderdetails`
--

CREATE TABLE `orderdetails` (
  `id` int(11) NOT NULL,
  `orderId` int(11) NOT NULL,
  `bookId` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orderdetails`
--

INSERT INTO `orderdetails` (`id`, `orderId`, `bookId`, `quantity`) VALUES
(2, 3, 8, 2),
(4, 4, 9, 2);

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `id` int(11) NOT NULL,
  `customerName` varchar(100) NOT NULL,
  `customerPhone` varchar(100) NOT NULL,
  `totalCost` int(11) NOT NULL,
  `addedBy` varchar(50) NOT NULL,
  `orderDate` date NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`id`, `customerName`, `customerPhone`, `totalCost`, `addedBy`, `orderDate`) VALUES
(3, 'user', '1234567899', 275, 'admin', '2022-08-22'),
(4, 'user3', '123456789', 275, '[4, \"sourav\"]', '2022-08-26');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `addbooks`
--
ALTER TABLE `addbooks`
  ADD PRIMARY KEY (`id`),
  ADD KEY `categoriesid` (`BookCategory`),
  ADD KEY `racksid` (`RackNoColumn`);

--
-- Indexes for table `addemployee`
--
ALTER TABLE `addemployee`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `addracks`
--
ALTER TABLE `addracks`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `adminlogin`
--
ALTER TABLE `adminlogin`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `categories`
--
ALTER TABLE `categories`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `orderdetails`
--
ALTER TABLE `orderdetails`
  ADD PRIMARY KEY (`id`),
  ADD KEY `orderID` (`orderId`),
  ADD KEY `bookId` (`bookId`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `addbooks`
--
ALTER TABLE `addbooks`
  MODIFY `id` int(50) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT for table `addemployee`
--
ALTER TABLE `addemployee`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `addracks`
--
ALTER TABLE `addracks`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `adminlogin`
--
ALTER TABLE `adminlogin`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `categories`
--
ALTER TABLE `categories`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `orderdetails`
--
ALTER TABLE `orderdetails`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `addbooks`
--
ALTER TABLE `addbooks`
  ADD CONSTRAINT `categoriesid` FOREIGN KEY (`BookCategory`) REFERENCES `categories` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `racksid` FOREIGN KEY (`RackNoColumn`) REFERENCES `addracks` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `orderdetails`
--
ALTER TABLE `orderdetails`
  ADD CONSTRAINT `bookId` FOREIGN KEY (`bookId`) REFERENCES `addbooks` (`id`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `orderID` FOREIGN KEY (`orderId`) REFERENCES `orders` (`id`) ON DELETE CASCADE ON UPDATE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
