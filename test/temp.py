import re


SCHEMAS = [
    'gogamechen2_gamesvr_datadb_102',
    'gogamechen2_gamesvr_datadb_107',
    'gogamechen2_gamesvr_datadb_108',
    'gogamechen2_gamesvr_datadb_109',
    'gogamechen2_gamesvr_datadb_11',
    'gogamechen2_gamesvr_datadb_110',
    'gogamechen2_gamesvr_datadb_111',
    'gogamechen2_gamesvr_datadb_112',
    'gogamechen2_gamesvr_datadb_113',
    'gogamechen2_gamesvr_datadb_114',
    'gogamechen2_gamesvr_datadb_115',
    'gogamechen2_gamesvr_datadb_116',
    'gogamechen2_gamesvr_datadb_117',
    'gogamechen2_gamesvr_datadb_118',
    'gogamechen2_gamesvr_datadb_119',
    'gogamechen2_gamesvr_datadb_12',
    'gogamechen2_gamesvr_datadb_120',
    'gogamechen2_gamesvr_datadb_121',
    'gogamechen2_gamesvr_datadb_122',
    'gogamechen2_gamesvr_datadb_123',
    'gogamechen2_gamesvr_datadb_128',
    'gogamechen2_gamesvr_datadb_129',
    'gogamechen2_gamesvr_datadb_13',
    'gogamechen2_gamesvr_datadb_134',
    'gogamechen2_gamesvr_datadb_135',
    'gogamechen2_gamesvr_datadb_14',
    'gogamechen2_gamesvr_datadb_140',
    'gogamechen2_gamesvr_datadb_141',
    'gogamechen2_gamesvr_datadb_146',
    'gogamechen2_gamesvr_datadb_147',
    'gogamechen2_gamesvr_datadb_15',
    'gogamechen2_gamesvr_datadb_152',
    'gogamechen2_gamesvr_datadb_153',
    'gogamechen2_gamesvr_datadb_158',
    'gogamechen2_gamesvr_datadb_159',
    'gogamechen2_gamesvr_datadb_16',
    'gogamechen2_gamesvr_datadb_164',
    'gogamechen2_gamesvr_datadb_165',
    'gogamechen2_gamesvr_datadb_17',
    'gogamechen2_gamesvr_datadb_170',
    'gogamechen2_gamesvr_datadb_171',
    'gogamechen2_gamesvr_datadb_176',
    'gogamechen2_gamesvr_datadb_177',
    'gogamechen2_gamesvr_datadb_18',
    'gogamechen2_gamesvr_datadb_181',
    'gogamechen2_gamesvr_datadb_188',
    'gogamechen2_gamesvr_datadb_19',
    'gogamechen2_gamesvr_datadb_196',
    'gogamechen2_gamesvr_datadb_1_1',
    'gogamechen2_gamesvr_datadb_1_2',
    'gogamechen2_gamesvr_datadb_1_3',
    'gogamechen2_gamesvr_datadb_20',
    'gogamechen2_gamesvr_datadb_201',
    'gogamechen2_gamesvr_datadb_205',
    'gogamechen2_gamesvr_datadb_206',
    'gogamechen2_gamesvr_datadb_207',
    'gogamechen2_gamesvr_datadb_21',
    'gogamechen2_gamesvr_datadb_212',
    'gogamechen2_gamesvr_datadb_213',
    'gogamechen2_gamesvr_datadb_22',
    'gogamechen2_gamesvr_datadb_23',
    'gogamechen2_gamesvr_datadb_24',
    'gogamechen2_gamesvr_datadb_25',
    'gogamechen2_gamesvr_datadb_26',
    'gogamechen2_gamesvr_datadb_27',
    'gogamechen2_gamesvr_datadb_2_1',
    'gogamechen2_gamesvr_datadb_2_2',
    'gogamechen2_gamesvr_datadb_32',
    'gogamechen2_gamesvr_datadb_37',
    'gogamechen2_gamesvr_datadb_3_1',
    'gogamechen2_gamesvr_datadb_3_2',
    'gogamechen2_gamesvr_datadb_42',
    'gogamechen2_gamesvr_datadb_47',
    'gogamechen2_gamesvr_datadb_4_1',
    'gogamechen2_gamesvr_datadb_4_2',
    'gogamechen2_gamesvr_datadb_52',
    'gogamechen2_gamesvr_datadb_57',
    'gogamechen2_gamesvr_datadb_5_1',
    'gogamechen2_gamesvr_datadb_5_2',
    'gogamechen2_gamesvr_datadb_62',
    'gogamechen2_gamesvr_datadb_67',
    'gogamechen2_gamesvr_datadb_7',
    'gogamechen2_gamesvr_datadb_72',
    'gogamechen2_gamesvr_datadb_77',
    'gogamechen2_gamesvr_datadb_82',
    'gogamechen2_gamesvr_datadb_87',
    'gogamechen2_gamesvr_datadb_92',
    'gogamechen2_gamesvr_datadb_97',
    'gogamechen2_gamesvr_logdb_102',
    'gogamechen2_gamesvr_logdb_107',
    'gogamechen2_gamesvr_logdb_108',
    'gogamechen2_gamesvr_logdb_109',
    'gogamechen2_gamesvr_logdb_11',
    'gogamechen2_gamesvr_logdb_110',
    'gogamechen2_gamesvr_logdb_111',
    'gogamechen2_gamesvr_logdb_112',
    'gogamechen2_gamesvr_logdb_113',
    'gogamechen2_gamesvr_logdb_114',
    'gogamechen2_gamesvr_logdb_115',
    'gogamechen2_gamesvr_logdb_116',
    'gogamechen2_gamesvr_logdb_117',
    'gogamechen2_gamesvr_logdb_118',
    'gogamechen2_gamesvr_logdb_119',
    'gogamechen2_gamesvr_logdb_12',
    'gogamechen2_gamesvr_logdb_120',
    'gogamechen2_gamesvr_logdb_121',
    'gogamechen2_gamesvr_logdb_122',
    'gogamechen2_gamesvr_logdb_123',
    'gogamechen2_gamesvr_logdb_128',
    'gogamechen2_gamesvr_logdb_129',
    'gogamechen2_gamesvr_logdb_13',
    'gogamechen2_gamesvr_logdb_134',
    'gogamechen2_gamesvr_logdb_135',
    'gogamechen2_gamesvr_logdb_14',
    'gogamechen2_gamesvr_logdb_140',
    'gogamechen2_gamesvr_logdb_141',
    'gogamechen2_gamesvr_logdb_146',
    'gogamechen2_gamesvr_logdb_147',
    'gogamechen2_gamesvr_logdb_15',
    'gogamechen2_gamesvr_logdb_152',
    'gogamechen2_gamesvr_logdb_153',
    'gogamechen2_gamesvr_logdb_158',
    'gogamechen2_gamesvr_logdb_159',
    'gogamechen2_gamesvr_logdb_16',
    'gogamechen2_gamesvr_logdb_164',
    'gogamechen2_gamesvr_logdb_165',
    'gogamechen2_gamesvr_logdb_17',
    'gogamechen2_gamesvr_logdb_170',
    'gogamechen2_gamesvr_logdb_171',
    'gogamechen2_gamesvr_logdb_176',
    'gogamechen2_gamesvr_logdb_177',
    'gogamechen2_gamesvr_logdb_18',
    'gogamechen2_gamesvr_logdb_181',
    'gogamechen2_gamesvr_logdb_188',
    'gogamechen2_gamesvr_logdb_19',
    'gogamechen2_gamesvr_logdb_196',
    'gogamechen2_gamesvr_logdb_20',
    'gogamechen2_gamesvr_logdb_201',
    'gogamechen2_gamesvr_logdb_205',
    'gogamechen2_gamesvr_logdb_206',
    'gogamechen2_gamesvr_logdb_207',
    'gogamechen2_gamesvr_logdb_21',
    'gogamechen2_gamesvr_logdb_212',
    'gogamechen2_gamesvr_logdb_213',
    'gogamechen2_gamesvr_logdb_218',
    'gogamechen2_gamesvr_logdb_219',
    'gogamechen2_gamesvr_logdb_22',
    'gogamechen2_gamesvr_logdb_224',
    'gogamechen2_gamesvr_logdb_225',
    'gogamechen2_gamesvr_logdb_23',
    'gogamechen2_gamesvr_logdb_230',
    'gogamechen2_gamesvr_logdb_231',
    'gogamechen2_gamesvr_logdb_236',
    'gogamechen2_gamesvr_logdb_237',
    'gogamechen2_gamesvr_logdb_24',
    'gogamechen2_gamesvr_logdb_242',
    'gogamechen2_gamesvr_logdb_243',
    'gogamechen2_gamesvr_logdb_248',
    'gogamechen2_gamesvr_logdb_249',
    'gogamechen2_gamesvr_logdb_25',
    'gogamechen2_gamesvr_logdb_254',
    'gogamechen2_gamesvr_logdb_255',
    'gogamechen2_gamesvr_logdb_26',
    'gogamechen2_gamesvr_logdb_260',
    'gogamechen2_gamesvr_logdb_27',
    'gogamechen2_gamesvr_logdb_32',
    'gogamechen2_gamesvr_logdb_37',
    'gogamechen2_gamesvr_logdb_42',
    'gogamechen2_gamesvr_logdb_47',
    'gogamechen2_gamesvr_logdb_52',
    'gogamechen2_gamesvr_logdb_57',
    'gogamechen2_gamesvr_logdb_62',
    'gogamechen2_gamesvr_logdb_67',
    'gogamechen2_gamesvr_logdb_7',
    'gogamechen2_gamesvr_logdb_72',
    'gogamechen2_gamesvr_logdb_77',
    'gogamechen2_gamesvr_logdb_82',
    'gogamechen2_gamesvr_logdb_87',
    'gogamechen2_gamesvr_logdb_92',
    'gogamechen2_gamesvr_logdb_97',
    'gogamechen2_gmsvr_datadb_1',
    'gogamechen2_gmsvr_datadb_5',
    'gogamechen2_gmsvr_datadb_9',
    'gogamechen2_publicsvr_datadb_10',
    'gogamechen2_publicsvr_datadb_2',
    'gogamechen2_publicsvr_datadb_6',
]


qiuting = re.compile('\d+?_\d')


qts = []
drops = []
dumps = []
copys = []

loads = []


tables = [
    """CREATE TABLE `log_item` (
  `user_id` varchar(255) DEFAULT NULL,
  `server_id` int(11) DEFAULT NULL,
  `real_svr_id` int(11) DEFAULT NULL,
  `player_id` bigint(20) DEFAULT NULL,
  `player_name` varchar(32) DEFAULT NULL,
  `platform_type` int(11) DEFAULT NULL,
  `channel` varchar(64) DEFAULT NULL,
  `device` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `vip` int(11) DEFAULT NULL,
  `recharge_amount` int(11) DEFAULT NULL,
  `money` bigint(20) DEFAULT NULL,
  `gold` int(11) DEFAULT NULL,
  `gold_gm` int(11) DEFAULT NULL,
  `gold_recharge` int(11) DEFAULT NULL,
  `oper_type` int(11) DEFAULT NULL,
  `item_id` int(11) DEFAULT NULL,
  `num` int(11) DEFAULT NULL,
  `change_num` int(11) DEFAULT NULL,
  `oper_time` datetime DEFAULT NULL,
  `reason` int(11) DEFAULT NULL,
  `item_type` int(11) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8""",

    """CREATE TABLE `log_player_event` (
  `user_id` varchar(255) DEFAULT NULL,
  `server_id` int(11) DEFAULT NULL,
  `real_svr_id` int(11) DEFAULT NULL,
  `player_id` bigint(20) DEFAULT NULL,
  `player_name` varchar(32) DEFAULT NULL,
  `platform_type` int(11) DEFAULT NULL,
  `channel` varchar(64) DEFAULT NULL,
  `device` varchar(255) DEFAULT NULL,
  `level` int(11) DEFAULT NULL,
  `vip` int(11) DEFAULT NULL,
  `recharge_amount` int(11) DEFAULT NULL,
  `login_days` int(11) DEFAULT NULL,
  `money` bigint(20) DEFAULT NULL,
  `gold` int(11) DEFAULT NULL,
  `gold_gm` int(11) DEFAULT NULL,
  `gold_recharge` int(11) DEFAULT NULL,
  `oper_time` datetime DEFAULT NULL,
  `reason` int(11) DEFAULT NULL,
  `param1` bigint(20) DEFAULT NULL,
  `param2` bigint(20) DEFAULT NULL,
  `param3` varchar(512) DEFAULT NULL,
  `third_type` varchar(255) DEFAULT NULL,
  `third_id` varchar(255) DEFAULT NULL
) ENGINE=MyISAM DEFAULT CHARSET=utf8"""
]


for schema in SCHEMAS:
    if re.findall(qiuting, schema):
        drops.append('mysql -uroot -pfdkjsa194dm10 -S../mysql.sock -e"drop database %s"' % schema)
        qts.append(
            'mysqldump -R -uroot -pfdkjsa194dm10 -S../mysql.sock %s | gzip > %s.gz' % (schema, schema)
        )
    else:
        loads.append(
            'mysql -uroot -pfdkjsa194dm10 -S../mysql.sock -e"create database %s default character set utf8"' % schema
        )
        loads.append(
            'mysql -uroot -pfdkjsa194dm10 -S../mysql.sock %s < %s.gz' % (schema, schema)
        )
        if 'gamesvr_datadb' in schema:
            copys.append('cp %s.gz ../dbsync/' % schema)
            continue
        dumps.append(
            'mysqldump -R -uroot -pfdkjsa194dm10 -S../mysql.sock %s '
            '--ignore-table="%s.log_item" --ignore-table="%s.log_player_event"'
            ' | gzip > %s.gz' % (schema, schema, schema, schema)
        )

for script in copys:
    print script

print('-----------------------------')

for script in dumps:
    print script

# print('-----------------------------')
#
# for script in qts:
#     print script
#
# print('-----------------------------')
#
# for script in drops:
#     print script

print('-----------------------------')

for script in loads:
    print script
