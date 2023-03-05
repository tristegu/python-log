# xpath解析相比于re和BeautifulSoup解析更加高效，写起来也更加容易，相当于文件夹的路径，html中的每个标签相当于一个节点
# xpath是在XML文档中搜索内容的一门语言，html是xml的一个子集
# 安装lxml模块
# 导入lxml模块
from lxml import etree

xml = """
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">周大强</nick>
        <nick id="10010">周芷若</nick>
        <nick class="jay">周杰伦</nick>
        <nick class="jolin">蔡依林</nick>
        <div>
            <nick>热热热热1</nick>
        </div>
        <span>
            <nick>热热热热2</nick>
        </span>
    </author>
    
    <partner>
        <nick id="ppc">胖胖陈</nick>
        <nick id="ppbc">胖胖不陈</nick>
    </partner>
</book>
"""
tree = etree.XML(xml)
# result = tree.xpath("/book")  # /表示层级关系，第一个/是根节点
# result = tree.xpath("/book/name/text()")  # text()拿文本
# result = tree.xpath("/book/author//nick/text()")   # //可以找到后代
# result = tree.xpath("/book/author/*/nick/text()")   # *表示任意的节点，通配符，拿到div和span的nick文本
result = tree.xpath("/book//nick/text()")   # 拿到book标签内的所有nick文本
print(result)