#urlopen形式获取网页数据
'''from urllib.request import urlopen
url ="http://baidu.com"
resp = urlopen(url)
with open("mybaidu.html",mode="w", encoding="utf-8") as f:
    f.write(resp.read().decode("utf-8"))
print("over!")
resp.close()'''

# 导入requests模板
import requests
query = input("请输入你要查询的明星名字")
url = f"https://www.sogou.com/web?query={query}"
dic ={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=dic)
print(resp.text)
resp.close()



