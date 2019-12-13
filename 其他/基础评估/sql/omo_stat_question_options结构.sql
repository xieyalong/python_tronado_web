/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50714
 Source Host           : localhost:3306
 Source Schema         : jundui

 Target Server Type    : MySQL
 Target Server Version : 50714
 File Encoding         : 65001

 Date: 13/12/2019 12:05:19
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for omo_stat_question_options
-- ----------------------------
DROP TABLE IF EXISTS `omo_stat_question_options`;
CREATE TABLE `omo_stat_question_options`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_id` int(11) UNSIGNED NOT NULL COMMENT '问题ID',
  `option_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '选项文本',
  `option_score` int(11) NOT NULL DEFAULT 0 COMMENT '选项分数',
  `deleted` int(11) NOT NULL DEFAULT 0 COMMENT '删除时间',
  `updated` int(11) NOT NULL DEFAULT 0 COMMENT '修改时间',
  `created` int(11) NOT NULL DEFAULT 0 COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 518 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = '问题选项表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
