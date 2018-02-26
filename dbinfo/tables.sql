# ************************************************************
# Sequel Pro SQL dump
# Version 4541
#
# http://www.sequelpro.com/
# https://github.com/sequelpro/sequelpro
#
# Host: 127.0.0.1 (MySQL 5.5.41)
# Database: authdb
# Generation Time: 2018-02-26 10:10:50 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table apy_auth
# ------------------------------------------------------------

CREATE TABLE `apy_auth` (
  `id` varchar(32) NOT NULL DEFAULT '' COMMENT '主键',
  `name` varchar(50) DEFAULT NULL COMMENT '权限名称',
  `code` varchar(50) DEFAULT NULL COMMENT '权限code',
  `create_time` int(11) DEFAULT '0' COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `py_auth_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='系统所有权限表';

LOCK TABLES `apy_auth` WRITE;
/*!40000 ALTER TABLE `apy_auth` DISABLE KEYS */;

INSERT INTO `apy_auth` (`id`, `name`, `code`, `create_time`)
VALUES
	('06fcb479-2cc2-4faa-83ac-d541f142','查看所有用户','/user/list',1504962015),
	('0987cc3f-2099-4846-8eaf-2efd51f5','获取所有数据库','/tool/dbs',1504972074),
	('2bac8bd2-2649-4588-9983-954bd6ce','新增权限','/auth/add',1504961840),
	('38a3485c-3672-4434-a238-efc3a2f3','获取数据表信息','/tool/schema',1504972115),
	('5e51226c-4772-4054-a027-075c9f7d','为角色新增权限','/role/auth/add',1504961924),
	('609d2ca1-2305-431d-aa16-092c1b47','允许用户登陆','/user/allow',1504962048),
	('7836917b-8363-46c1-9c72-497b7e53','退出登陆','/user/logout',1504962007),
	('80119256-455e-4b9c-9d11-3c4035e1','为角色删除权限','/role/auth/del',1504961937),
	('81b155bb-06f9-4962-ae0d-d0dd51bc','查看自己信息','/user/me',1504968656),
	('8b07ddb4-3bb9-46c8-b5ad-a5b0c097','获取数据库所有表','/tool/tables',1504972098),
	('954b246a-cc72-4d53-a209-e4362c05','添加用户','/user/add',1504962024),
	('9c3faeaa-26b9-4933-8184-6fefc4b0','禁止用户登陆','/user/forbidden',1504962038),
	('a7344785-516b-469f-bfb6-731c21c3','新增角色','/role/add',1504961880),
	('bdbd2146-51c6-4594-bd8d-9c77ab9c','为指定用户添加角色','/user/role/add',1504962065),
	('dcc114e8-01f1-4bb1-816f-0de4f1fc','获取指定用户信息','/user/info',1504961992),
	('e1e4ff00-95c8-4fb0-8eab-8ac8903f','所有角色列表','/role/list',1504961864),
	('ead3d9d3-785f-449e-a08d-9557ad0a','指定角色的所有权限','/role/auths',1504961906),
	('fcda6759-fb72-40d2-9229-2cdd437a','为指定用户删除角色','/user/role/del',1504962080),
	('ff4a75b9-f4fa-498e-8f71-ebd08ece','查看所有权限','/auth/list',1504961832);

/*!40000 ALTER TABLE `apy_auth` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table apy_role
# ------------------------------------------------------------

CREATE TABLE `apy_role` (
  `id` varchar(32) NOT NULL DEFAULT '' COMMENT '????',
  `name` varchar(50) DEFAULT NULL COMMENT '????',
  `code` varchar(30) DEFAULT NULL COMMENT '?????',
  `create_time` int(11) DEFAULT '0' COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `py_role_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='系统角色';

LOCK TABLES `apy_role` WRITE;
/*!40000 ALTER TABLE `apy_role` DISABLE KEYS */;

INSERT INTO `apy_role` (`id`, `name`, `code`, `create_time`)
VALUES
	('76aafca5-056d-4005-bffc-be70a34b','开发者','developer',1504972043),
	('f132f851-7eb3-45f3-a702-f0c3c6a7','上帝','admin',0);

/*!40000 ALTER TABLE `apy_role` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table apy_role_auths
# ------------------------------------------------------------

CREATE TABLE `apy_role_auths` (
  `id` varchar(32) NOT NULL DEFAULT '' COMMENT '????',
  `role` varchar(32) NOT NULL DEFAULT '' COMMENT '??id',
  `auth_id` varchar(32) NOT NULL DEFAULT '' COMMENT '??id',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `py_role_auths_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='角色与权限关联表';

LOCK TABLES `apy_role_auths` WRITE;
/*!40000 ALTER TABLE `apy_role_auths` DISABLE KEYS */;

INSERT INTO `apy_role_auths` (`id`, `role`, `auth_id`, `create_time`)
VALUES
	('193e9636-b38c-45a1-b00f-9ba9b448','admin','a7344785-516b-469f-bfb6-731c21c3',1504971511),
	('1b2daa68-f7df-44fc-8e6b-b8e77a18','developer','8b07ddb4-3bb9-46c8-b5ad-a5b0c097',1504972127),
	('22704fb7-4fb0-469c-bb38-d00f52c0','admin','2bac8bd2-2649-4588-9983-954bd6ce',1504970646),
	('22704fb7-4fb0-469c-bb38-d00f52ce','admin','5e51226c-4772-4054-a027-075c9f7d',1504971463),
	('5488c444-b7c3-49ff-a9c7-a38b7cb2','admin','ff4a75b9-f4fa-498e-8f71-ebd08ece',1504961945),
	('58a8670a-dfcb-496b-90d7-da0e0a2e','admin','609d2ca1-2305-431d-aa16-092c1b47',1504970709),
	('6bfe21dd-5518-41ef-abc0-cdc8569f','admin','81b155bb-06f9-4962-ae0d-d0dd51bc',1504968656),
	('72f4f1c4-071c-4613-a549-dc791531','admin','7836917b-8363-46c1-9c72-497b7e53',1504962085),
	('877de450-1f61-41f5-aa77-18d6c18a','admin','fcda6759-fb72-40d2-9229-2cdd437a',1504962085),
	('9390deff-c48b-444a-b6a3-8807cc9a','admin','80119256-455e-4b9c-9d11-3c4035e1',1504961945),
	('c4fa8c6e-4815-4ae9-84c3-325984cf','developer','7836917b-8363-46c1-9c72-497b7e53',1504972429),
	('c598fca2-77d2-4822-b3e5-8b23a348','admin','954b246a-cc72-4d53-a209-e4362c05',1504962085),
	('c9f8eca5-954c-4e4c-a4e2-34ea4ea7','admin','9c3faeaa-26b9-4933-8184-6fefc4b0',1504970697),
	('d39a0856-d764-4bb5-8359-d3bda344','admin','dcc114e8-01f1-4bb1-816f-0de4f1fc',1504962085),
	('d4398a54-4a20-4a9c-87b2-22c5f4be','admin','bdbd2146-51c6-4594-bd8d-9c77ab9c',1504962085),
	('e2ed4db9-69d9-4801-a115-8367617c','developer','0987cc3f-2099-4846-8eaf-2efd51f5',1504972127),
	('ebd6c135-6f72-4322-b50e-9559ff0e','admin','06fcb479-2cc2-4faa-83ac-d541f142',1504971269),
	('ec91c0f8-3603-43a7-8410-68b4e2b4','developer','38a3485c-3672-4434-a238-efc3a2f3',1504972179),
	('ecbd3468-4501-4250-acc4-5b9d73d3','admin','e1e4ff00-95c8-4fb0-8eab-8ac8903f',1504961945),
	('ef249bc7-ba8d-46e4-be53-d4fe3cbd','developer','81b155bb-06f9-4962-ae0d-d0dd51bc',1504972244),
	('f6d7433e-0e7b-48a9-bb8c-618e3bac','admin','ead3d9d3-785f-449e-a08d-9557ad0a',1504961945);

/*!40000 ALTER TABLE `apy_role_auths` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table apy_user
# ------------------------------------------------------------

CREATE TABLE `apy_user` (
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

LOCK TABLES `apy_user` WRITE;
/*!40000 ALTER TABLE `apy_user` DISABLE KEYS */;

INSERT INTO `apy_user` (`id`, `nickname`, `loginname`, `password`, `avatar`, `token`, `is_valid`, `create_time`)
VALUES
	('7ae75ea9-ae15-4190-a9e8-d6a78bd0','开发一枚','kaifa','63a9f0ea7bb98050796b649e85481845','/static/img/avatar.png','f11a9838-96d5-11e7-b93a-6c40089a','yes',1504972212),
	('e72c4cd3-e69a-4fad-9aae-d29ac552','上帝视角','root','63a9f0ea7bb98050796b649e85481845','/static/img/avatar.png','d6c8ee0a-9708-11e7-a69e-6c40089a','yes',1504961501);

/*!40000 ALTER TABLE `apy_user` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table apy_user_roles
# ------------------------------------------------------------

CREATE TABLE `apy_user_roles` (
  `id` varchar(32) NOT NULL DEFAULT '' COMMENT '????',
  `uid` varchar(32) NOT NULL DEFAULT '' COMMENT '??id',
  `role` varchar(32) NOT NULL DEFAULT '' COMMENT '??ID',
  `create_time` int(11) NOT NULL DEFAULT '0' COMMENT '记录创建时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `py_user_roles_id_uindex` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT=' 用户角色关联表';

LOCK TABLES `apy_user_roles` WRITE;
/*!40000 ALTER TABLE `apy_user_roles` DISABLE KEYS */;

INSERT INTO `apy_user_roles` (`id`, `uid`, `role`, `create_time`)
VALUES
	('5f8d47eb-d53c-4736-b025-b9b2b6ae','e72c4cd3-e69a-4fad-9aae-d29ac552','developer',1504974222),
	('dc1b8f67-f30c-4990-b4eb-61e0688f','7ae75ea9-ae15-4190-a9e8-d6a78bd0','developer',1504972348),
	('e67f5d75-b1b6-424a-aede-b3588db1','e72c4cd3-e69a-4fad-9aae-d29ac552','admin',1504962092);

/*!40000 ALTER TABLE `apy_user_roles` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
