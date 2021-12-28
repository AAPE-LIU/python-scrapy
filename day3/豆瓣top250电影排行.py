import requests
import re

url = 'https://movie.douban.com/top250'

head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}

ret = re.compile(r'<li>.*?<em class="">(?P<rank>.*?)</em>.*?<span class="title">(.*?)</span>'
                 r'.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                 r'.*?<span>(?P<num_people>.*?)人评价</span>', re.S)
# 再python3中如果想完全契合正则表达式的规则，需要加上 re.A

with open('text.html',mode='w',encoding='utf-8') as f,open("title.txt",mode='w',encoding='utf-8') as t:
    for s in range(0, 250, 25):
        par = {
            'start': int(s),
            'filter': ''
        }
        resp = requests.get(url, headers=head, params=par)

        f.write(resp.text)
        content = ret.finditer(resp.text)
        for i in content:
            t.write(i.group('rank') + ',' + i.group('year').strip()+ ',' + i.group('score')+ ',' + i.group('num_people') + '\n')
resp.close()
