-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Nov 12, 2012 at 12:33 PM
-- Server version: 5.5.20
-- PHP Version: 5.3.10

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `inloc2`
--

-- --------------------------------------------------------

--
-- Table structure for table `loc`
--

DROP TABLE IF EXISTS `loc`;
CREATE TABLE IF NOT EXISTS `loc` (
  `LOC_id` int(11) NOT NULL AUTO_INCREMENT,
  `LOC_URI` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `language` varchar(2) COLLATE utf8_unicode_ci DEFAULT NULL,
  `created` date DEFAULT NULL,
  `modified` date DEFAULT NULL,
  `issued` datetime DEFAULT NULL,
  `validity_start` datetime DEFAULT NULL,
  `validity_end` datetime DEFAULT NULL,
  `version` double DEFAULT NULL,
  `is_structure` char(1) COLLATE utf8_unicode_ci DEFAULT 'N',
  `primary_structure` int(11) DEFAULT NULL,
  PRIMARY KEY (`LOC_id`),
  UNIQUE KEY `LOC_URI_UNIQUE` (`LOC_URI`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci AUTO_INCREMENT=1414 ;

--
-- Dumping data for table `loc`
--

INSERT INTO `loc` (`LOC_id`, `LOC_URI`, `language`, `created`, `modified`, `issued`, `validity_start`, `validity_end`, `version`, `is_structure`, `primary_structure`) VALUES
(1, 'http://purl.org/net/inloc/cefr/cefr', 'EN', '2007-06-22', NULL, NULL, NULL, NULL, 1, 'Y', NULL),
(2, 'http://purl.org/net/inloc/cefr/cefr-understanding', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(3, 'http://purl.org/net/inloc/cefr/cefr-understanding-reading', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(4, 'http://purl.org/net/inloc/cefr/cefr-understanding-reading-A1', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(5, 'http://purl.org/net/inloc/cefr/cefr-understanding-reading-A2', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(6, 'http://purl.org/net/inloc/cefr/cefr-understanding-reading-B1', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(7, 'http://purl.org/net/inloc/cefr/cefr-understanding-reading-B2', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(8, 'http://purl.org/net/inloc/cefr/cefr-understanding-reading-C1', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(9, 'http://purl.org/net/inloc/cefr/cefr-understanding-reading-C2', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(10, 'http://purl.org/net/inloc/cefr/cefr-understanding-listening', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(11, 'http://purl.org/net/inloc/cefr/cefr-understanding-listening-A1', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(12, 'http://purl.org/net/inloc/cefr/cefr-understanding-listening-A2', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(13, 'http://purl.org/net/inloc/cefr/cefr-understanding-listening-B1', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(14, 'http://purl.org/net/inloc/cefr/cefr-understanding-listening-B2', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(15, 'http://purl.org/net/inloc/cefr/cefr-understanding-listening-C1', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(16, 'http://purl.org/net/inloc/cefr/cefr-understanding-listening-C2', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 1),
(17, 'http://example.eu/ids/ecf', 'EN', '2010-09-01', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 2, 'Y', NULL),
(18, 'http://example.co.uk/ids/A', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(19, 'http://example.co.uk/ids/A.2', 'FR', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(20, 'http://example.co.uk/ids/A.2_L3', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(21, 'http://example.co.uk/ids/A.2_L4', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(22, 'http://example.co.uk/ids/A.2_K1', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(23, 'http://example.co.uk/ids/A.2_K2', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(24, 'http://example.co.uk/ids/A.2_K3', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(25, 'http://example.co.uk/ids/A.2_K4', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(26, 'http://example.co.uk/ids/A.2_K5', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(27, 'http://example.co.uk/ids/A.2_S1', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(28, 'http://example.co.uk/ids/A.2_S2', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(29, 'http://example.co.uk/ids/A.2_S3', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(30, 'http://example.co.uk/ids/A.2_S4', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(31, 'http://example.co.uk/ids/A.2_S5', '', '0000-00-00', '0000-00-00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', '0000-00-00 00:00:00', 0, 'N', 17),
(51, 'http://www.eummena.org/inloc/51', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(52, 'http://www.eummena.org/inloc/52', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(53, 'http://www.eummena.org/inloc/53', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(70, 'http://www.eummena.org/inloc/70', 'DE', NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(71, 'http://www.eummena.org/inloc/71', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(72, 'http://www.eummena.org/inloc/72', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(77, 'http://www.eummena.org/inloc/77', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(78, 'http://www.eummena.org/inloc/78', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(79, 'http://www.eummena.org/inloc/79', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(85, 'http://www.eummena.org/inloc/85', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(86, 'http://www.eummena.org/inloc/86', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(87, 'http://www.eummena.org/inloc/87', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(88, 'http://www.eummena.org/inloc/88', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(89, 'http://www.eummena.org/inloc/89', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(226, 'http://www.eummena.org/inloc/226', 'EN', NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(228, 'http://www.eummena.org/inloc/228', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(229, 'http://www.eummena.org/inloc/229', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(230, 'http://www.eummena.org/inloc/230', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(231, 'http://www.eummena.org/inloc/231', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(232, 'http://www.eummena.org/inloc/232', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(233, 'http://www.eummena.org/inloc/233', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(234, 'http://www.eummena.org/inloc/234', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(235, 'http://www.eummena.org/inloc/235', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(236, 'http://www.eummena.org/inloc/236', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(237, 'http://www.eummena.org/inloc/237', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(238, 'http://www.eummena.org/inloc/238', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(239, 'http://www.eummena.org/inloc/239', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(240, 'http://www.eummena.org/inloc/240', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(241, 'http://www.eummena.org/inloc/241', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(242, 'http://www.eummena.org/inloc/242', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(243, 'http://www.eummena.org/inloc/243', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(244, 'http://www.eummena.org/inloc/244', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(245, 'http://www.eummena.org/inloc/245', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(246, 'http://www.eummena.org/inloc/246', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(247, 'http://www.eummena.org/inloc/247', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(248, 'http://www.eummena.org/inloc/248', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(249, 'http://www.eummena.org/inloc/249', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(250, 'http://www.eummena.org/inloc/250', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(251, 'http://www.eummena.org/inloc/251', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(252, 'http://www.eummena.org/inloc/252', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(253, 'http://www.eummena.org/inloc/253', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(254, 'http://www.eummena.org/inloc/254', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(255, 'http://www.eummena.org/inloc/255', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(256, 'http://www.eummena.org/inloc/256', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(279, 'http://www.eummena.org/inloc/279', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(280, 'http://www.eummena.org/inloc/280', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(282, 'http://www.eummena.org/inloc/282', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(283, 'http://www.eummena.org/inloc/283', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(284, 'http://www.eummena.org/inloc/284', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(285, 'http://www.eummena.org/inloc/285', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(286, 'http://www.eummena.org/inloc/286', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(287, 'http://www.eummena.org/inloc/287', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(288, 'http://www.eummena.org/inloc/288', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(289, 'http://www.eummena.org/inloc/289', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(290, 'http://www.eummena.org/inloc/290', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(291, 'http://www.eummena.org/inloc/291', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(292, 'http://www.eummena.org/inloc/292', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(293, 'http://www.eummena.org/inloc/293', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(294, 'http://www.eummena.org/inloc/294', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(295, 'http://www.eummena.org/inloc/295', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(296, 'http://www.eummena.org/inloc/296', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(297, 'http://www.eummena.org/inloc/297', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(298, 'http://www.eummena.org/inloc/298', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(299, 'http://www.eummena.org/inloc/299', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(300, 'http://www.eummena.org/inloc/300', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(302, 'http://www.eummena.org/inloc/302', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(303, 'http://www.eummena.org/inloc/303', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(332, 'http://www.eummena.org/inloc/332', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(333, 'http://www.eummena.org/inloc/333', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(334, 'http://www.eummena.org/inloc/334', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(335, 'http://www.eummena.org/inloc/335', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(336, 'http://www.eummena.org/inloc/336', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(337, 'http://www.eummena.org/inloc/337', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(338, 'http://www.eummena.org/inloc/338', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(339, 'http://www.eummena.org/inloc/339', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(340, 'http://www.eummena.org/inloc/340', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(341, 'http://www.eummena.org/inloc/341', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(342, 'http://www.eummena.org/inloc/342', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(343, 'http://www.eummena.org/inloc/343', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(344, 'http://www.eummena.org/inloc/344', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(345, 'http://www.eummena.org/inloc/345', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(346, 'http://www.eummena.org/inloc/346', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(347, 'http://www.eummena.org/inloc/347', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(348, 'http://www.eummena.org/inloc/348', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(349, 'http://www.eummena.org/inloc/349', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(350, 'http://www.eummena.org/inloc/350', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(351, 'http://www.eummena.org/inloc/351', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(352, 'http://www.eummena.org/inloc/352', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(353, 'http://www.eummena.org/inloc/353', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(354, 'http://www.eummena.org/inloc/354', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(355, 'http://www.eummena.org/inloc/355', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(356, 'http://www.eummena.org/inloc/356', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(357, 'http://www.eummena.org/inloc/357', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(358, 'http://www.eummena.org/inloc/358', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(359, 'http://www.eummena.org/inloc/359', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(360, 'http://www.eummena.org/inloc/360', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(361, 'http://www.eummena.org/inloc/361', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(362, 'http://www.eummena.org/inloc/362', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(363, 'http://www.eummena.org/inloc/363', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(364, 'http://www.eummena.org/inloc/364', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(365, 'http://www.eummena.org/inloc/365', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(366, 'http://www.eummena.org/inloc/366', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(367, 'http://www.eummena.org/inloc/367', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(368, 'http://www.eummena.org/inloc/368', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(369, 'http://www.eummena.org/inloc/369', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(370, 'http://www.eummena.org/inloc/370', NULL, NULL, NULL, NULL, NULL, NULL, NULL, 'N', 1330),
(1330, 'http://www.eummena.org/inloc/1330', 'EN', '2012-06-13', '2012-06-16', '2012-02-01 00:00:00', NULL, NULL, 2013, 'Y', NULL);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
