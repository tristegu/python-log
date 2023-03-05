import re
s = '''
<div class='jay'><span id='1'>周杰伦</span></div>
<div class='jj'><span id='2'>林俊杰</span></div>
<div class='guo'><span id='3'>郭麒麟</span></div>
<div class='fan'><span id='4'>范思哲</span></div>
<div class='lv'><span id='5'>路易威登</span></div>
'''
# (?P<分组名字>正则)可以单独从正则匹配的内容中进一步提取内容
obj = re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>", re.S)  # re.S能够让.匹配到换行符
result = obj.finditer(s)
name = []
id = []
for item in result:
    name.append(item.group("name"))
    id.append(item.group("id"))
    dic = dict(zip(id, name))
print(dic)
    # dic = item.groupdict()
    # for key in dic:
        # print(key, ":", dic[key])
    # print(item.group("name"))
    # print(item.group("id"))
