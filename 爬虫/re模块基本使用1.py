import re

# 匹配字符串中所有符合正则的内容
a = re.findall(r"\d+", "我的电话号码是：10086，倪博洋的电话号码是：10010")
print(a)

# finditer：匹配字符串中所有内容[返回的是迭代器],从迭代器中拿到内容需要.group()
it = re.finditer(r"\d+", "我的电话号码是：10086，倪博洋的电话号码是：10010")
for i in it:
    print(i.group())

# search找到一个结果就返回，返回的结果是match对象，要想拿到数据需要.group()
s = re.search(r"\d+", "我的电话号码是：10086，倪博洋的电话号码是：10010")
print(s.group())

# match是从头开始匹配
'''t = re.match(r"\d+", "我的电话号码是：10086，倪博洋的电话号码是：10010")
print(t.group())'''

# 预加载正则表达式(预加载其实就是先将正则表达式固定，其次在输入含有目标对象的字符串)
# 很重要，基本上re解析都是使用预加载的形式
obj = re.compile(r"\d+")

ret = obj.finditer("我的电话号码是：10086，倪博洋的电话号码是：10010")
for it in ret:
    print(it.group())

hello = obj.findall("啦啦啦啦啦878787")
for item in hello:
    print(item.group())