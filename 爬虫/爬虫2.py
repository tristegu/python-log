# 使用post请求访问网站数据
import requests
url = "https://fanyi.baidu.com/sug"

s = input("请输入你要翻译的单词：")
dat = {
    'kw': s
}
# 发送post请求
# 使用data参数传递
response = requests.post(url, data=dat)
print(response.json())  # 将服务器返回的内容直接处理成json（） =》dic（字典形式）
response.close()