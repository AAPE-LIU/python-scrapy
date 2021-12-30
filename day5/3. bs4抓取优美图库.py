# 1. 拿到主页面的源码，然后提取到子页面的链接地址
from bs4 import BeautifulSoup
import requests
import os
import time

url = 'https://umei.cc/'
resp = requests.get(url)
resp.encoding = 'utf-8'
# print(resp.text)
sub_content = BeautifulSoup(resp.text,'html.parser')
sub_link = sub_content.find_all('div',attrs={'class':'PicListTxt'})
list1 = []
for content in sub_link:
    url_link = content.find_all('li')
    for x in url_link:
        whole_url = url + x.find('a').get('href')  # bs4中拿到标签的属性值，直接用 .get 方法
        list1.append(whole_url)
print(list1)
list2 = []
i = 0
for img_url in list1:
    child_page = requests.get(img_url)
    child_page.encoding = 'utf-8'
    child_page_text = child_page.text
    bs_resp = BeautifulSoup(child_page_text,'html.parser')
    div_content = bs_resp.find('div',attrs={'class':'ImageBody'})
    fin_url_link = div_content.find('img').get('src')
    list2.append(fin_url_link)

    # 下载图片：请求到网址之后，交给requests，然后返回回来的东西是响应，拿到响应的字节内容，
    # 你将字节写到文件中去，不就是图片了吗？
    resp = requests.get(fin_url_link)
    content = resp.content
    cwd = os.getcwd()
    if not os.path.exists(cwd + 'image'):
        os.mkdir(cwd + 'image')
    name =os.path.join(cwd + 'image', str(i) + '.jpg')
    with open(name,mode='wb') as f:
        f.write(content)
    i+=1
    print(i)
    time.sleep(1)
# print(list2)
print('over')