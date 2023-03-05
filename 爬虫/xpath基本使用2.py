from lxml import etree

tree = etree.parse("b.html")
# result = tree.xpath('/html/body/*/li[2]/a/text()')  # []表示索引，可以设置选取第几个li标签
result = tree.xpath("/html/body/ol/li/a[@href='dapao']/text()")  # @href表示href这个属性
# [@xxx=xxx]表示属性的筛选
# print(ol_li_list)
ol_li_list = tree.xpath("/html/body/ol/li")

for li in ol_li_list:
    # 从每个li中提取到文字信息
    result1 = li.xpath("./a/text()")  # 在li中继续查找，相对查找  ./表示当前节点
    print(result1)
    result2 = li.xpath("./a/@href")  # 拿到属性值：@属性
    print(result2)
print(tree.xpath("/html/body/*/li/a/@href"))
print(tree.xpath("/html/body/div[1]/text()"))