# 用户登录网站过程
# 首先用户输入自己的用户名以及密码，然后向服务器发送请求，服务器收到用户名密码之后会检查用户名和密码
# 对不对，如果是对的，那么服务器会向浏览器的cookie中写入一串服务器可以识别的代码
# 然后，浏览器再向服务器发送请求，带着之前的cookie。服务器看到cookie之后，就知道是什么情况了
# 就会将该用户的账户内的信息以及资源返回给浏览器

# 登录 -> 得到cookie
# 带着cookie去请求到书架url -> 书架上的内容

# 必须把上面那两个操作连起来
# session会记录下来cookie，不会丢失信息，但是request不行
import requests

url = 'https://passport.17k.com/ck/user/login'

date = {
    'loginName': '起个名字真寄吧难',
    'password': 'lzlz210206...'
}

cookies = 'accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F09%252F89%252F91%252F87649189.jpg-88x88%253Fv%253D1641033606000%26id%3D87649189%26nickname%3D%25E8%25B5%25B7%25E4%25B8%25AA%25E5%2590%258D%25E5%25AD%2597%25E7%259C%259F%25E5%25AF%2584%25E5%2590%25A7%25E9%259A%25BE%26e%3D1656586468%26s%3D95ba83dc7a8dd80d; expires=Thu, 30-Jun-2022 10:54:28 GMT; Max-Age=15552000; path=/; domain=17k.com'

url2 = 'https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919'

# 登录
session = requests.session()
resp = session.post(url,data=date)
# print(resp.text)

# 拿书架上的数据
resp2 = session.get(url2)  # 默认是带着cookie的
print(resp2.json())