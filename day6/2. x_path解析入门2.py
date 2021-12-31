from lxml import etree

tree = etree.parse('xml.html')  # 使用etree.parse读取html文件

result1 = tree.xpath('/html/body/ul/li/a/text()')  # ['百度', '⾕歌', '搜狗']

result2 = tree.xpath('/html/body/ul/li[1]/a/text()')  # ['百度']
# []代表索引，索引是从1开始的

result3 = tree.xpath('/html/body/ol/li/a/text()')  # ['飞机', '⼤炮', '⽕⻋']

result4 = tree.xpath('/html/body/ol/li/a[@href="dapao"]/text()')  # ['⼤炮']
# 使用[@属性=值]来指定特定的节点

# 如果我想遍历ol中的a元素呢？
ol_list = tree.xpath('/html/body/ol/li')
for i in ol_list:
    result5 = i.xpath('./a/text()')
    print(result5)
    result6 = i.xpath('./a/@href')
    print(result6)

print(tree.xpath('/html/body/ul/li/a/@href'))

# 有这样一种可能性，如果你想拿到某个元素的内容，但是他的路径可能会很复杂，那么我们想拿到他该怎么办呢？
# 解决方法：用浏览器打开 -> 右键检查 -> 点击弹出来的窗口的左上角的那个小标志 -> 找到对应的元素 -> 右键复制xpath
print(tree.xpath('/html/body/div[1]/text()'))
print(tree.xpath('/html/body/div[2]/text()'))
