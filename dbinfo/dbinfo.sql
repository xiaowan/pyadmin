# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.5.41)
# Database: authdb
# Generation Time: 2018-03-02 10:27:36 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table py_auth
# ------------------------------------------------------------

DROP TABLE IF EXISTS `py_auth`;

CREATE TABLE `py_auth` (
  `id` varchar(32) NOT NULL DEFAULT '' COMMENT '主键',
  `name` varchar(50) DEFAULT NULL COMMENT '权限名称',
  `code` varchar(50) DEFAULT NULL COMMENT '权限code',
  `create_time` int(11) DEFAULT '0' COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `py_auth_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='系统所有权限表';

LOCK TABLES `py_auth` WRITE;
/*!40000 ALTER TABLE `py_auth` DISABLE KEYS */;

INSERT INTO `py_auth` (`id`, `name`, `code`, `create_time`)
VALUES
	('0bdc2bf3-ff15-4d04-beac-9a37d831','所有权限点','/auth/list',1519982802),
	('155c641b-f6d5-4f47-b1d4-b2c7e6fd','添加角色','/role/add',1519982722),
	('25c091d6-8247-48fc-91f4-992ac507','查看所有数据库','/tool/dbs',1519982766),
	('33732867-9a62-4bdc-9d1a-49a8fcf6','获取用户信息','/user/info',1519982636),
	('355ac6a6-b81d-4987-9956-d3b4ab1f','允许用户登陆','/user/allow',1519982657),
	('40dd07bc-c1e2-44ce-b925-b5f19aa6','所有未被添加到系统中的权限点','/auth/newauths',1519982859),
	('44a8ddd4-6c51-4194-aa70-944316af','为角色分配权限点','/role/auth/add',1519982744),
	('56176f3c-e092-4ffd-8002-6e013899','用户列表','/user/list',1519982643),
	('5a9661b6-5dd8-402f-bdd9-b619752c','指定角色的所有权限点','/role/auths',1519982732),
	('755a761f-69e1-4089-bea0-c159be2f','禁用用户','/user/forbid',1519982650),
	('823d7256-ff41-4720-a9c2-5d6bef30','所有角色列表','/role/list',1519982705),
	('8eab6301-418f-48a8-b850-313d4843','所有可以分配给角色的权限点','/auth/canassign',1519982822),
	('a3a70073-151b-4f32-9297-09ccbeb4','用户退出','/user/logout',1519982629),
	('a8c847a6-52c0-450b-80cd-477f2d33','用户登陆','/user/login',1519982622),
	('b149b833-ca2e-4885-9a6e-8056562b','为用户分配角色','/user/role/add',1519982676),
	('b1707c7b-8a60-41aa-8548-de4c3c5d','为角色移除权限点','/role/auth/del',1519982754),
	('c3151931-cb0f-499c-8b4e-285d585a','添加权限点','/auth/add',1519982829),
	('e744041f-11c8-4d86-9d99-85fa16a7','查看指定数据库的所有表','/tool/tables',1519982781),
	('e82ac681-7a4d-4b6c-9917-a14d8254','为用户移除角色','/user/role/del',1519982687),
	('ea4edf95-94d3-4548-9246-43d0816f','指定用户的所有角色','/user/roles',1519982696),
	('eccb5570-5d2b-4c6d-8930-8b40981e','查看指定数据表的schema','/tool/schema',1519982791),
	('f596882d-d60d-40e1-8477-5b285e70','添加用户','/user/add',1519982664);

/*!40000 ALTER TABLE `py_auth` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table py_role
# ------------------------------------------------------------

DROP TABLE IF EXISTS `py_role`;

CREATE TABLE `py_role` (
  `id` varchar(32) NOT NULL DEFAULT '' COMMENT '????',
  `name` varchar(50) DEFAULT NULL COMMENT '????',
  `role` varchar(30) DEFAULT NULL COMMENT '?????',
  `create_time` int(11) DEFAULT '0' COMMENT '记录创建时间',
  `desc` text COMMENT '这里是职位描述',
  PRIMARY KEY (`id`),
  UNIQUE KEY `py_role_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='系统角色';

LOCK TABLES `py_role` WRITE;
/*!40000 ALTER TABLE `py_role` DISABLE KEYS */;

INSERT INTO `py_role` (`id`, `name`, `role`, `create_time`, `desc`)
VALUES
	('a23ee073-9b2a-4020-9094-55a73d7b','上帝视角','god',1519982612,NULL),
	('e4ef9a75-183b-4905-80b9-fe6a5100','普通职员','common',1519982887,NULL),
	('ee35fd8c-60f4-47f1-b241-f29e380b','开发人员','developer',1519982936,NULL);

/*!40000 ALTER TABLE `py_role` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table py_role_auths
# ------------------------------------------------------------

DROP TABLE IF EXISTS `py_role_auths`;

CREATE TABLE `py_role_auths` (
  `id` varchar(40) NOT NULL DEFAULT '' COMMENT '????',
  `role` varchar(40) NOT NULL DEFAULT '' COMMENT '??id',
  `auth_id` varchar(40) NOT NULL DEFAULT '' COMMENT '??id',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `py_role_auths_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='角色与权限关联表';

LOCK TABLES `py_role_auths` WRITE;
/*!40000 ALTER TABLE `py_role_auths` DISABLE KEYS */;

INSERT INTO `py_role_auths` (`id`, `role`, `auth_id`, `create_time`)
VALUES
	('023b69d9-8e15-4b7c-8ed7-e06f804e72a1','god','0bdc2bf3-ff15-4d04-beac-9a37d831',1519985177),
	('060399a8-05b3-4bc3-b6cb-7e5313e9ec7a','common','a3a70073-151b-4f32-9297-09ccbeb4',1519982906),
	('1527803a-7855-45cf-9bbe-0afe11bb1b7d','god','823d7256-ff41-4720-a9c2-5d6bef30',1519985177),
	('4744eb27-24f5-45c0-ae86-df1520866838','developer','e744041f-11c8-4d86-9d99-85fa16a7',1519982945),
	('55e7414a-aec1-45ec-b765-0d64277480d1','god','ea4edf95-94d3-4548-9246-43d0816f',1519985177),
	('761098ef-68f3-4359-be3e-f70d2796481c','god','5a9661b6-5dd8-402f-bdd9-b619752c',1519985177),
	('79e6c670-53dd-482c-a08d-564e7c1b49ff','common','33732867-9a62-4bdc-9d1a-49a8fcf6',1519985159),
	('7a101d37-5ea3-49d0-b59d-2e94f1f3bbd3','god','40dd07bc-c1e2-44ce-b925-b5f19aa6',1519985177),
	('961ba693-df4d-45da-a1cb-b4733828d97d','developer','eccb5570-5d2b-4c6d-8930-8b40981e',1519982945),
	('9b544548-acc7-4a38-9b68-87030527ef47','god','44a8ddd4-6c51-4194-aa70-944316af',1519985177),
	('a0c995cf-21a5-4dd4-8efc-d42a1f42adda','common','a8c847a6-52c0-450b-80cd-477f2d33',1519982902),
	('a1f495d6-372b-415d-ab47-32a9ef7ead09','god','56176f3c-e092-4ffd-8002-6e013899',1519985177),
	('ba916714-4474-406f-b552-588d2c81c873','god','f596882d-d60d-40e1-8477-5b285e70',1519985177),
	('bfc4e29e-4e9f-4991-825b-9d5b77b6f5f8','god','e82ac681-7a4d-4b6c-9917-a14d8254',1519985177),
	('c093116f-a274-473e-a955-ad0be4616709','god','155c641b-f6d5-4f47-b1d4-b2c7e6fd',1519985177),
	('ce909e00-40de-4278-95b5-126fc951cf29','god','755a761f-69e1-4089-bea0-c159be2f',1519985177),
	('db4ba3a4-22d5-4bde-ac5b-9065c3f47a94','god','b149b833-ca2e-4885-9a6e-8056562b',1519985177),
	('dd894e60-2e1c-45e3-be6b-35bdc216682a','god','355ac6a6-b81d-4987-9956-d3b4ab1f',1519985177),
	('df4bf00a-0e3a-4e47-b72e-e6c7222d5dac','god','c3151931-cb0f-499c-8b4e-285d585a',1519985177),
	('ef5a8381-9d99-47ed-8a8c-1a06a5158e2d','god','b1707c7b-8a60-41aa-8548-de4c3c5d',1519985177),
	('f036c40f-56d6-4c2d-a92b-bc0db60d8140','developer','25c091d6-8247-48fc-91f4-992ac507',1519982945),
	('f1a0c466-07c7-43f6-b404-a8fdc05fd5bd','god','8eab6301-418f-48a8-b850-313d4843',1519985177);

/*!40000 ALTER TABLE `py_role_auths` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table py_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `py_user`;

CREATE TABLE `py_user` (
  `id` varchar(32) NOT NULL DEFAULT '' COMMENT '主键',
  `nickname` varchar(50) DEFAULT NULL COMMENT '昵称',
  `loginname` varchar(50) DEFAULT NULL COMMENT '登录名',
  `password` varchar(50) DEFAULT NULL COMMENT '密码',
  `avatar` varchar(255) DEFAULT '/static/img/avatar.png' COMMENT '头像',
  `token` varchar(32) DEFAULT NULL COMMENT '用户token',
  `is_valid` varchar(10) DEFAULT 'yes' COMMENT '是否允许登陆',
  `create_time` int(11) DEFAULT '0' COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `py_user_id_uindex` (`id`),
  UNIQUE KEY `py_user_token_uindex` (`token`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='所有系统用户';

LOCK TABLES `py_user` WRITE;
/*!40000 ALTER TABLE `py_user` DISABLE KEYS */;

INSERT INTO `py_user` (`id`, `nickname`, `loginname`, `password`, `avatar`, `token`, `is_valid`, `create_time`)
VALUES
	('0eb1e985-d9d7-4725-b108-3e9bb599','开发人员','developer','e10adc3949ba59abbe56e057f20f883e','/static/img/avatar.png',NULL,'yes',1519985218),
	('1fa9687b-551d-44a9-8bfc-c8b6cb8a','上帝','root','e10adc3949ba59abbe56e057f20f883e','/static/img/avatar.png','85bbba1c-1e03-11e8-829a-6c40089a','yes',1519982580),
	('a661d2db-21bd-4a59-b732-325fce94','网站编辑','seven','e10adc3949ba59abbe56e057f20f883e','/static/img/avatar.png',NULL,'yes',1519985747);

/*!40000 ALTER TABLE `py_user` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table py_user_role
# ------------------------------------------------------------

DROP TABLE IF EXISTS `py_user_role`;

CREATE TABLE `py_user_role` (
  `id` varchar(32) NOT NULL DEFAULT '' COMMENT '????',
  `uid` varchar(32) NOT NULL DEFAULT '' COMMENT '??id',
  `role` varchar(32) NOT NULL DEFAULT '' COMMENT '??ID',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `py_user_roles_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT=' 用户角色关联表';

LOCK TABLES `py_user_role` WRITE;
/*!40000 ALTER TABLE `py_user_role` DISABLE KEYS */;

INSERT INTO `py_user_role` (`id`, `uid`, `role`, `create_time`)
VALUES
	('07ee2b20-39dd-4a60-9a26-64787dc5','1fa9687b-551d-44a9-8bfc-c8b6cb8a','god',1519983275),
	('2da69415-1d73-4439-ad30-c4b3ef6e','a661d2db-21bd-4a59-b732-325fce94','common',1519985773),
	('54b59841-58bd-4103-8769-71fc5bc1','1fa9687b-551d-44a9-8bfc-c8b6cb8a','common',1519984666),
	('740d05ac-44ed-49ab-b32f-c3ff9ecc','1fa9687b-551d-44a9-8bfc-c8b6cb8a','developer',1519985937),
	('7f25b5c0-d069-4f3d-af7e-229d1063','0eb1e985-d9d7-4725-b108-3e9bb599','developer',1519985424),
	('b1816d3e-1d6d-4b6e-8826-75814512','0eb1e985-d9d7-4725-b108-3e9bb599','common',1519985990);

/*!40000 ALTER TABLE `py_user_role` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
