# 安装bs4
import requests
from bs4 import BeautifulSoup
import csv

# 获取目标网页的源代码
url = "http://wsjkw.sh.gov.cn/yqfk2020/"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=header)
f = open("news.csv", mode="w")
csvwriter = csv.writer(f)

# 将页面源代码交给BeautifulSoup处理，并生成bs对象
page = BeautifulSoup(resp.text, "html.parser")

# 从bs对象中查找数据
# find(标签，属性=值) 只能找到一个
# find_all(标签，属性=值) 可以找到多个数据，其中碰到class，可以使用class_的方式避免python关键字的问题
result1 = page.find("ul", class_="uli16 nowrapli border")
result2 = result1.find_all("li")
a = result2[0].text
b = result2[1].text
c = result2[2].text
d = result2[3].text
e = result2[4].text
csvwriter.writerow([a, b, c, d, e])
f.close()
print("over!!")