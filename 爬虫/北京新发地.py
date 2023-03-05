import requests
# 导入numpy库，实现二维列表的换行输出
import numpy as np
from concurrent.futures import ThreadPoolExecutor


def down_one_page():
    url = "http://www.xinfadi.com.cn/getPriceData.html"
    global page
    page = 1
    param = {
        "limit": 20,
        "current": page,
        "pubDateStartTime": "",
        "pubDateEndTime": "",
        "prodPcatid": "",
        "prodCatid": "",
        "prodName": ""
    }
    for page in range(3):
        resp = requests.post(url, params=param)
        dic = resp.json()
        information_list = dic["list"]
        all_list = []
        Data = ["prodCat", "prodName", "lowPrice", "highPrice", "avgPrice", "pubDate"]
        # 创建二维列表，利用双重循环查找索引i和key
        page = page + 1
        for i in range(0, 20):
            all_list.append([])
            for key in Data:
                all_list[i].append(information_list[i][key])
    print(np.array(all_list))   # 二维列表的换行输出


if __name__ == '__main__':
    down_one_page()