# -*- coding: utf-8 -*-
import pymysql
db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='Ghr20020118',
            db='倪倪有限公司',
            charset='utf8')
cur = db.cursor()
'''cur.execute('create table 汽车(汽车牌照 nvarchar(50) primary key ,型号 char(10),颜色 char(5),车门数 int(2),座位数 int(2),汽车价值 int(8),购买日期 char(15),里程表数 char(10),驾驶员 char(5))')
cur.execute('create table 汽车合同(汽车牌照 nvarchar(50) primary key ,汽车类型 char(8),里程表数 char(10),激活费用 int(10),汽车供应商 char(5),合同编号 char(8))')
cur.execute('create table 汽车成本(汽车牌照 nvarchar(50) primary key ,费用类型 char(8),日期 char(15))')
cur.execute('create table 汽车燃油记录(汽车牌照 nvarchar(50) primary key ,升 float(5),单价 float(5),总价 float(7))')
cur.execute('create table 汽车里程表(汽车牌照 nvarchar(50) primary key ,日期 char(15),里程表数 char(10))')
cur.execute('create table 汽车服务日志(汽车牌照 nvarchar(50) primary key ,服务类型 char(8),里程表数 char(10),日期 char(15),金额总计 float(8))')'''

'''data = [
    ("沪A676G3", "宝马", "红色", 2, 2, 2000000, "2020年6月7日", "100.76km", "倪博洋"),
    ("沪AH565V", "奥斯汀", "银色", 2, 2, 1960000, "2021年10月3日", "84.89km", "陈灏天"),
    ("沪L47B9O", "AudiA1", "白色", 4, 4, 900000, "2020年12月23日", "56.08km", "顾浩然"),
    ("沪KNY986", "宾利", "蓝色", 4, 4, 1200000, "2022年1月15日", "187.42km", "沈奕扬"),
    ("沪C56A80", "玛莎拉蒂", "白色", 4, 4, 3000000, "2020年9月30日", "76.84km", "焦琪"),
]
cur.executemany('insert into 汽车(汽车牌照,型号,颜色,车门数,座位数,汽车价值,购买日期,里程表数,驾驶员) value (%s, %s, %s, %s, %s, %s, %s, %s, %s)', data)'''

'''data1 = [
    ("沪A676G3", "维修及保养", "2020年10月24日"),
    ("沪AH565V", "维修保养以及租赁", "2022年1月21日"),
    ("沪L47B9O", "租赁", "2021年7月8日"),
    ("沪KNY986", "维修保养以及租赁", "2022年4月19日"),
    ("沪C56A80", "维修及保养", "2022年6月22日"),
]
cur.executemany('insert into 汽车成本(汽车牌照,费用类型,日期) value (%s, %s, %s)', data1)'''

'''data2 = [
    ("沪A676G3", "维修及保养", "100.76km", "2020年10月24日", 1450),
    ("沪AH565V", "夏季轮胎", "84.89km", "2022年1月21日", 2000),
    ("沪L47B9O", "租赁", "56.08km", "2021年7月8日", 500),
    ("沪KNY986", "雪地胎", "187.42km", "2022年4月19日", 2400),
    ("沪C56A80", "维修及保养", "76.84km", "2022年6月22日", 3420),
]
cur.executemany('insert into 汽车服务日志(汽车牌照,服务类型,里程表数,日期,金额总计) value (%s, %s, %s, %s, %s)',data2)'''

'''data3 = [
    ("沪A676G3", "宝马", "100.76km", 400, "倪博洋", "X12C3"),
    ("沪AH565V", "奥斯汀", "84.89km", 700, "陈灏天", "V35B1"),
    ("沪L47B9O", "AudiA1", "56.08km", 500, "顾浩然", "H56K8"),
    ("沪KNY986", "宾利", "187.42km", 550, "沈奕扬", "P98A3"),
    ("沪C56A80", "玛莎拉蒂", "76.84km", 600, "焦琪", "O86Y5"),
]
cur.executemany('insert into 汽车合同(汽车牌照,汽车类型,里程表数,激活费用,汽车供应商,合同编号) value (%s, %s, %s, %s, %s, %s)',data3)'''

'''data4 = [
    ("沪A676G3", "2020年10月24日", "100.76km"),
    ("沪AH565V", "2022年1月21日", "84.89km"),
    ("沪L47B9O", "2021年7月8日", "56.08km"),
    ("沪KNY986", "2022年4月19日", "187.42km"),
    ("沪C56A80", "2022年6月22日", "76.84km"),
]
cur.executemany('insert into 汽车里程表(汽车牌照,日期,里程表数) value (%s, %s, %s)', data4)'''

data5 = [
    ("沪A676G3", 70, 10.43, 730.1),
    ("沪AH565V", 64.5, 10.43, 672.735),
    ("沪L47B9O", 57.5, 10.43, 599.725),
    ("沪KNY986", 45, 10.43, 469.35),
    ("沪C56A80", 60, 10.43, 625.8),
]
cur.executemany('insert into 汽车燃油记录(汽车牌照,升,单价,总价) value (%s, %s, %s, %s)', data5)
cur.close()
db.commit()
db.close()