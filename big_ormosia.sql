/*
 Navicat MySQL Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 80015
 Source Host           : localhost:3306
 Source Schema         : big_ormosia

 Target Server Type    : MySQL
 Target Server Version : 80015
 File Encoding         : 65001

 Date: 30/10/2020 09:37:54
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for alembic_version
-- ----------------------------
DROP TABLE IF EXISTS `alembic_version`;
CREATE TABLE `alembic_version`  (
  `version_num` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`version_num`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of alembic_version
-- ----------------------------
INSERT INTO `alembic_version` VALUES ('7e32bcb82ce8');

-- ----------------------------
-- Table structure for category
-- ----------------------------
DROP TABLE IF EXISTS `category`;
CREATE TABLE `category`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `one_category_id` int(11) NULL DEFAULT NULL,
  `grop_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `type_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `two_category_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for color
-- ----------------------------
DROP TABLE IF EXISTS `color`;
CREATE TABLE `color`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `yanse` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `m` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `x` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `xl` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `xxl` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `code` int(11) NOT NULL,
  `s` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1002 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of color
-- ----------------------------
INSERT INTO `color` VALUES (1, '白色', '100', '100', '100', '100', 1001, '10');
INSERT INTO `color` VALUES (2, '黑色', '100', '100', '100', '100', 1001, '10');
INSERT INTO `color` VALUES (3, '绿色', '100', '100', '100', '100', 1001, '10');
INSERT INTO `color` VALUES (4, '白色', '100', '100', '100', '100', 1002, '10');
INSERT INTO `color` VALUES (5, '褐色', '100', '100', '100', '100', 1002, '10');
INSERT INTO `color` VALUES (6, '粉色', '100', '100', '100', '100', 1002, '10');
INSERT INTO `color` VALUES (7, '白色', '100', '100', '100', '100', 1003, '10');
INSERT INTO `color` VALUES (8, '黑不拉几色', '100', '100', '100', '100', 1003, '10');

-- ----------------------------
-- Table structure for flow
-- ----------------------------
DROP TABLE IF EXISTS `flow`;
CREATE TABLE `flow`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uid` int(11) NULL DEFAULT NULL,
  `goods_id` int(11) NULL DEFAULT NULL,
  `num` int(11) NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `update_time` datetime(0) NULL DEFAULT NULL,
  `color` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `size` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `prices` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `product_id` int(11) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `product_id`(`product_id`) USING BTREE,
  CONSTRAINT `flow_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of flow
-- ----------------------------
INSERT INTO `flow` VALUES (10, 1, 1003, 1, '2020-10-29 17:36:19', '2020-10-29 17:36:19', '黑不拉几色', 'M   ', '99.99', 1);
INSERT INTO `flow` VALUES (11, 1, 1003, 1, '2020-10-29 20:30:36', '2020-10-29 20:30:41', '黑不拉几色', 'M', '99.99', 1);
INSERT INTO `flow` VALUES (12, 1, 1001, 1, '2020-10-30 08:04:38', '2020-10-30 08:04:38', '黑色', 'M', '99.99', 1);

-- ----------------------------
-- Table structure for pro_sup
-- ----------------------------
DROP TABLE IF EXISTS `pro_sup`;
CREATE TABLE `pro_sup`  (
  `category_id` int(11) NOT NULL,
  `supplier_id` int(11) NOT NULL,
  PRIMARY KEY (`category_id`, `supplier_id`) USING BTREE,
  INDEX `supplier_id`(`supplier_id`) USING BTREE,
  CONSTRAINT `pro_sup_ibfk_1` FOREIGN KEY (`category_id`) REFERENCES `product` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `pro_sup_ibfk_2` FOREIGN KEY (`supplier_id`) REFERENCES `supplier` (`id`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dress_code` int(11) NOT NULL,
  `dress_brand` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dress_info` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dress_price` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dress_img_url` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `dress_date` datetime(0) NULL DEFAULT NULL,
  `dress_status` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `one_category_id` int(11) NULL DEFAULT NULL,
  `two_category_id` int(11) NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 4 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (1, 1001, 'big_ormosia', '2019新版短袖', '99.99', 'http://qhr70s0hx.hn-bkt.clouddn.com/7367_thumb_G_1430938073402.jpg', '2020-10-29 08:24:39', '1', 100, 1000);
INSERT INTO `product` VALUES (2, 1002, 'big_ormosia', '2019新版短袖', '99.00', 'http://qhr70s0hx.hn-bkt.clouddn.com/7367_thumb_G_1430938073402.jpg', '2020-10-29 08:48:47', '1', 100, 1000);
INSERT INTO `product` VALUES (3, 1003, 'big_ormosia', '2019新版短袖', '58.98', 'http://qhr70s0hx.hn-bkt.clouddn.com/8424_thumb_G_1458862954873.jpg', '2020-10-29 15:16:46', '1', 100, 1000);

-- ----------------------------
-- Table structure for supplier
-- ----------------------------
DROP TABLE IF EXISTS `supplier`;
CREATE TABLE `supplier`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `factory_number` int(11) NOT NULL,
  `factory_name` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `factory_person` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `factory_phone` int(11) NOT NULL,
  `factory_address` varchar(64) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for supply
-- ----------------------------
DROP TABLE IF EXISTS `supply`;
CREATE TABLE `supply`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dress_code` int(11) NOT NULL,
  `factory_number` int(11) NOT NULL,
  `pricing` int(11) NOT NULL,
  `supply_num` int(11) NOT NULL,
  `supply_date` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `nick_name` varchar(32) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `password_hash` varchar(128) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `mobile` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `avatar_url` varchar(256) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `create_time` datetime(0) NULL DEFAULT NULL,
  `last_login` datetime(0) NULL DEFAULT NULL,
  `is_admin` tinyint(1) NULL DEFAULT NULL,
  `signature` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `postal` int(11) NULL DEFAULT NULL,
  `address` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `address_info` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `email` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES (1, '主帅', '保安', '111', '111', 'http://qhr70s0hx.hn-bkt.clouddn.com/25397025d88b755758953b010d4b1c4f.jpg', '2020-10-29 08:21:23', '2020-10-29 08:21:23', 0, '保护不了任何人', 50000, '河北省承德市丰宁满族自治县', '大阁镇嘉西村', '110@119.com');

-- ----------------------------
-- Table structure for user_message
-- ----------------------------
DROP TABLE IF EXISTS `user_message`;
CREATE TABLE `user_message`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_grade` int(11) NULL DEFAULT NULL,
  `user_mobile` varchar(11) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_title` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_files_url` varchar(100) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `user_message` varchar(512) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
