/*
 Navicat Premium Data Transfer

 Source Server         : localTestMySQL8.0
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : localhost:3306
 Source Schema         : cov

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 06/05/2021 20:11:39
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for details
-- ----------------------------
DROP TABLE IF EXISTS `details`;
CREATE TABLE `details`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `update_time` datetime(0) NULL DEFAULT NULL,
  `province` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `city` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `confirm` int(11) NULL DEFAULT NULL,
  `confirm_add` int(11) NULL DEFAULT NULL,
  `heal` int(11) NULL DEFAULT NULL,
  `dead` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2724 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for fakes
-- ----------------------------
DROP TABLE IF EXISTS `fakes`;
CREATE TABLE `fakes`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `href` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for history
-- ----------------------------
DROP TABLE IF EXISTS `history`;
CREATE TABLE `history`  (
  `ds` datetime(5) NOT NULL COMMENT '日期',
  `confirm` int(11) NULL DEFAULT NULL COMMENT '累积确诊',
  `confirm_add` int(11) NULL DEFAULT NULL,
  `suspect` int(11) NULL DEFAULT NULL,
  `suspect_add` int(11) NULL DEFAULT NULL,
  `heal` int(11) NULL DEFAULT NULL,
  `heal_add` int(11) NULL DEFAULT NULL,
  `dead` int(11) NULL DEFAULT NULL,
  `dead_add` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`ds`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for hotsearch
-- ----------------------------
DROP TABLE IF EXISTS `hotsearch`;
CREATE TABLE `hotsearch`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dt` datetime(0) NOT NULL ON UPDATE CURRENT_TIMESTAMP(0),
  `content` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`, `dt`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 83 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for oversea
-- ----------------------------
DROP TABLE IF EXISTS `oversea`;
CREATE TABLE `oversea`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `href` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for recent_news
-- ----------------------------
DROP TABLE IF EXISTS `recent_news`;
CREATE TABLE `recent_news`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `href` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 30 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
