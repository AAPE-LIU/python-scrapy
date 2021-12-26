# 需求：用程序模拟浏览器，输入一个网址，从该网志中获取到资源或者内容
# python搞定以上需求，特别简单
from urllib.request import urlopen  # request是啥意思？是请求啊。我们回车，鼠标点击都是请求
url = "http://www.baidu.com"
# print(123)
resp = urlopen(url)  # 在这里urlopen就可以当作是一个浏览器，url就是网址，你打开这个网址之后是不要返回一个东西啊
# 用resp接收一下,其实就是得到一个响应
# print(resp.read())  # 这里有一个坑，你这样直接读取的话，汉字不会显示，会变成字节形式，因此要解码
# print(resp.read().decode('utf-8'))
# 但是目前我们拿到的东西他是一堆让人看起来很不爽的字符码，我们该怎么做呢？
with open('mybaidu.html',mode='w',encoding='utf-8') as f:
    f.write(resp.read().decode('utf-8'))
print('ok')
# 其实网页的本质就是html

