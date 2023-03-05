# 1.如何提取单个页面的数据
# 2.上线程池，多个页面同时抓取

import requests
from lxml import etree


def download_one_page(url):
    # 拿到页面源代码
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    table = html.xpath('//*[@id="bbs"]/div/div/div/div[4]/div[1]/div/table')[0]
    trs = table.xpath("./tr")
    # 拿到每一个tr
    print(trs)

# html/body/div[2]/div/div/div/div[4]/div[1]/div/table


if __name__ == '__main__':
    download_one_page("http://www.xinfadi.com.cn/priceDetail.html")

