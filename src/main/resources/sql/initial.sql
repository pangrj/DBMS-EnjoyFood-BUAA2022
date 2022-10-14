use databasetest;
drop TABLE IF EXISTS `menu`;
CREATE TABLE IF NOT EXISTS `student`
(
    `s_id`       bigint(32)  NOT NULL COMMENT '学号',
    `s_password` varchar(20) NOT NULL COMMENT 'password',
    `s_name`     varchar(20) DEFAULT NULL COMMENT '姓名',
    `s_dorm`     varchar(30) DEFAULT NULL COMMENT '宿舍',
    `s_gender`   varchar(30) DEFAULT NULL COMMENT '性别',
    PRIMARY KEY (`s_id`)
    );
truncate table `student`;

INSERT INTO `student` (s_id, s_password)
VALUES (1, '123'),
       (2, '121');

CREATE table IF NOT EXISTS `dish`
(
    `d_id`       bigint(32)  NOT NULL COMMENT '菜品编号',
    `d_name`     varchar(20) NOT NULL COMMENT '菜品名称',
    `d_category` varchar(20) NOT NULL COMMENT '种类',
    `d_cuisine`  varchar(20) DEFAULT NULL COMMENT '菜系',
    `d_calories` bigint(32)  NOT NULL COMMENT '热量',
    `d_price`    bigint(32)  DEFAULT NULL COMMENT '价格',
    PRIMARY KEY (`d_id`)
    );

truncate table `dish`;
INSERT INTO `dish` (d_id, d_name, d_category, d_cuisine, d_calories, d_price)
VALUES (123456, '卤肉饭', '套饭', '粤菜', 413, 12),
       (123457, '宫爆鸡丁', '荤菜', '川菜', 213, 8),
       (123458, '烤冷面', '小食', '东北菜', 160, 8),
       (123459, '麻婆豆腐', '素菜', '川菜', 100, 5),
       (123460, '冬阴功汤', '汤菜', '泰式', 200, 10);

CREATE table IF NOT EXISTS `chose_menu`
(
    `id`    bigint(32) NOT NULL COMMENT '编码',
    `s_id`  bigint(32) NOT NULL COMMENT '学号',
    `d_id`  bigint(32) NOT NULL COMMENT '菜品编号',
    `score` bigint(32) DEFAULT NULL COMMENT '评分'
    );
truncate table `chose_menu`;