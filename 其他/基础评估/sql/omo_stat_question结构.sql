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

 Date: 13/12/2019 12:05:04
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for omo_stat_question
-- ----------------------------
DROP TABLE IF EXISTS `omo_stat_question`;
CREATE TABLE `omo_stat_question`  (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '' COMMENT '问题标题',
  `state` tinyint(1) NOT NULL DEFAULT 0 COMMENT '状态：0禁止，1正常',
  `sort` int(11) NOT NULL DEFAULT 0 COMMENT '排序',
  `gender` tinyint(1) NOT NULL DEFAULT 0 COMMENT '性别：1男，2女',
  `age_min` int(11) NOT NULL DEFAULT 0 COMMENT '最低年龄',
  `age_max` int(11) NOT NULL DEFAULT 0 COMMENT '最高年龄',
  `group_id` int(11) UNSIGNED NOT NULL COMMENT '小组ID',
  `question_type` int(11) UNSIGNED NOT NULL COMMENT '类型，1=填空题，2选择题',
  `updated` int(11) NOT NULL DEFAULT 0 COMMENT '修改时间',
  `created` int(11) NOT NULL DEFAULT 0 COMMENT '创建时间',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 111 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci COMMENT = '问题表' ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
