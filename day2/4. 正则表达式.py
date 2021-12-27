import re

ret = re.compile('<span.*?>(?P<name>.*?)</span>', re.S)  # 让 . 能够匹配换行符

s = '''
<div class='jay'><span id='1'>刘秀达</span></div>
<div class='jay'><span id='2'>刺客信条</span></div>
<div class='jay'><span id='3'>壁纸引擎</span></div>
<div class='jay'><span id='4'>大宝大宝小思思</span></div>
<div class='jay'><span id='5'>武大博士生来咯</span></div>
'''
content = ret.finditer(s)
for i in content:
    print(i.group(1))  # 默认group内的参数是0，为0代表取整个匹配的内容，
    # 想取对应组内的内容还得指定序号，序号从1开始一路往后排

    # 还有一种方法就是给组起名字，然后匹配到的内容就会被起的那个名字接收，取内容的时候直接按照名字索引就可以
    print(i.group('name'))