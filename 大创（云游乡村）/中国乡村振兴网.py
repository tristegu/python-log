import requests
import re
import csv

# 中国乡村振兴网
# 爬取乡村振兴板块内容


def searchcountryside(list_num):

    for page in range(1, 17):
        url = f"http://www.zxqyj.org.cn/?list-{list_num}-{page}.html"
        resp = requests.get(url)
        # print(resp.text)
        # 获取页面源代码
        page_content = resp.text

        # 解析数据
        # 预加载正则表达式
        obj = re.compile(r'<li>.*?<div class="img">.*?<div class="text">'
                         r'.*?<a href="(?P<href>.*?)".*?>(?P<title>.*?)</a>'
                         r'.*?<span class="lab">(?P<times>.*?)</span>'
                         r'.*?<span class="lab">(?P<time>.*?)</span>', re.S)

        # 开始匹配
        result = obj.finditer(page_content)

        # 创建数据存储文件
        f = open(f"countryside_{page}.csv", mode="w")
        csvwriter = csv.writer(f)
        for it in result:
            # print(it.group("href"))
            # print(it.group("title"))
            # print(it.group("times"))
            # print(it.group("time"))
            dic = it.groupdict()
            csvwriter.writerow(dic.values())
    print("over！")

# 爬取政策新闻板块


def searchpolicy(list_num):

    for page in range(1, 19):
        url = f"http://www.zxqyj.org.cn/?list-{list_num}-{page}.html"
        resp = requests.get(url)
        # print(resp.text)
        # 获取页面源代码
        page_content = resp.text

        # 解析数据
        # 预加载正则表达式
        obj = re.compile(r'<li>.*?<div class="img">.*?<div class="text">'
                         r'.*?<a href="(?P<href>.*?)".*?>(?P<title>.*?)</a>'
                         r'.*?<span class="lab">(?P<times>.*?)</span>'
                         r'.*?<span class="lab">(?P<time>.*?)</span>', re.S)

        # 开始匹配
        result = obj.finditer(page_content)

        # 创建数据存储文件
        f = open(f"policy_{page}.csv", mode="w")
        csvwriter = csv.writer(f)
        for it in result:
            # print(it.group("href"))
            # print(it.group("title"))
            # print(it.group("times"))
            # print(it.group("time"))
            dic = it.groupdict()
            csvwriter.writerow(dic.values())
    print("over！")

# 爬取政府招商板块


def searchbusiness(list_num):

    for page in range(1, 6):
        url = f"http://www.zxqyj.org.cn/?list-{list_num}-{page}.html"
        resp = requests.get(url)
        # print(resp.text)
        # 获取页面源代码
        page_content = resp.text

        # 解析数据
        # 预加载正则表达式
        obj = re.compile(r'<li>.*?<div class="img">.*?<div class="text">'
                         r'.*?<a href="(?P<href>.*?)".*?>(?P<title>.*?)</a>'
                         r'.*?<span class="lab">(?P<times>.*?)</span>'
                         r'.*?<span class="lab">(?P<time>.*?)</span>', re.S)

        # 开始匹配
        result = obj.finditer(page_content)

        # 创建数据存储文件
        f = open(f"business_{page}.csv", mode="w")
        csvwriter = csv.writer(f)
        for it in result:
            # print(it.group("href"))
            # print(it.group("title"))
            # print(it.group("times"))
            # print(it.group("time"))
            dic = it.groupdict()
            csvwriter.writerow(dic.values())
    print("over！")

# 爬取国家扶持资金


def searchfinance(list_num):

    for page in range(1, 7):
        url = f"http://www.zxqyj.org.cn/?list-{list_num}-{page}.html"
        resp = requests.get(url)
        # print(resp.text)
        # 获取页面源代码
        page_content = resp.text

        # 解析数据
        # 预加载正则表达式
        obj = re.compile(r'<li>.*?<div class="img">.*?<div class="text">'
                         r'.*?<a href="(?P<href>.*?)".*?>(?P<title>.*?)</a>'
                         r'.*?<span class="lab">(?P<times>.*?)</span>'
                         r'.*?<span class="lab">(?P<time>.*?)</span>', re.S)

        # 开始匹配
        result = obj.finditer(page_content)

        # 创建数据存储文件
        f = open(f"finance_{page}.csv", mode="w")
        csvwriter = csv.writer(f)
        for it in result:
            # print(it.group("href"))
            # print(it.group("title"))
            # print(it.group("times"))
            # print(it.group("time"))
            dic = it.groupdict()
            csvwriter.writerow(dic.values())
    print("over！")


if __name__ == '__main__':
    # searchcountryside(1856)
    # searchpolicy(1866)
    # searchbusiness(1901)
    searchfinance(1865)