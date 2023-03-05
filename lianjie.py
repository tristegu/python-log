import pymysql
db = pymysql.connect("localhost", "root", "root", "studypython")
cursor = db.cursor()
cursor.execute("select version")
data = cursor.fetchone()
print(data)
cursor.close()
db.close()

arr=[]
for i in range(4) :
    arr.append([])
    for j in range(4):
        arr[i].append(j)
print(arr)
print(arr[1][3])
r = [[j for j in range(4)] for i in range(4)]
print(r)