import pymysql
db = pymysql.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='Ghr20020118',
            db='nby',
            charset='utf8')

cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print(data)
cursor.close()
db.close()
