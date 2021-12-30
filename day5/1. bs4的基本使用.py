# 爬取 北京新发地 的菜品
# 1.拿到页面源代码
# 2.使用bs4解析
import bs4
from bs4 import BeautifulSoup
import requests

url = 'http://www.xinfadi.com.cn/index.html'
resp = requests.get(url)
# print(resp.text)

# 1.解析数据：把页面源代码交给Beautifulsoup进行处理，生成beautifulsoup对象

page = BeautifulSoup(resp.text,'html.parser')  # 如果不指定内容类型的话，会出警告，因为BeautifulSoup并不知道你给我的是什么类型，
#                                               我就要去猜,我们告诉他是什么类型的他就不会有问题了
# print(page)

# 2.从bs对象中查找数据，总共就俩操作
# find（标签，属性=值）  找第一个出现的数据
# find_all（标签，属性=值）找所有出现的数据

# table = page.find("table",class_="tbl-body")
# 这里如果直接写class会报错，因为class是一个关键字，直接写会报错的，所以加个_当作保留字

table = page.find("div",attrs={'class':'tbl-body'})  # 这个和上面那个是一个含义，都是从page中找标签table
#                                                                                  属性class值为hq_table
print(table)
tablehead = table.find_all('th')
list1 = []
for i in tablehead:
    print(i.text)  # .text 表示拿标签标记的内容,并且不能直接从find_all返回的列表中直接拿，要从其中的元素获取
    list1.append(i.text)

print(list1)