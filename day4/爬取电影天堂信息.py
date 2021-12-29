import requests
import re

url = "https://dytt89.com/"

head = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}
recom = re.compile(r'<div class="title_all"><p><span style="float:left;">2021必看热片</span>'
                   r'.*?<ul>(?P<content>.*?)</ul>',re.S)
recom2 = re.compile(r"<li><a href='(?P<name>.*?)'",re.S)
recom3 = re.compile(r'<div class="title_all">.*?《(?P<name>.*?)》.*?<td style=.*?'
                    r'<a href="(?P<download>.*?)&tr=http:',re.S)
resp = requests.get(url,headers=head,verify=False)  # verify=False是为了解决防火墙问题
resp.encoding = 'gb2312'  # 指定字符集
content = recom.finditer(resp.text)
with open('url.txt',mode='w',encoding='utf-8') as f:
    for i in content:
        f.write(i.group('content').strip())
with open('url.txt',mode='r',encoding='utf-8') as f:
    content = f.read()
    concate = recom2.finditer(content)
list1 = []
for i in concate:
    # print(i.group('name'))
    list1.append(url+i.group('name').lstrip('/'))
print(list1)

with open('downloadurl.txt',mode='w',encoding='utf-8') as f:
    for i in list1:
        print(i)
        resp = requests.get(i, headers=head, verify=False)
        resp.encoding = 'gb2312'
        download_url = recom3.search(resp.text)
        # print(download_url.group('name'),download_url.group('download'))
        f.write(download_url.group('name')+'    '+download_url.group('download') + '\n')
        # print(download_url)
        # print(resp.text)
        # break