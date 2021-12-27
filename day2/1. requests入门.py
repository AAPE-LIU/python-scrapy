import requests
url = 'https://www.sogou.com/web?query=周杰伦'
# 有了url之后我们要去请求url
# 所有的在地址栏中的url都要使用get方法提交

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62"
           }  # 搞成一个字典的形式，用于伪装

resp = requests.get(url, headers=headers)  # 发出过请求，人家会给你一个响应，用resp来接收响应
print(resp)  # <Response [200]>  200代表正常收到请求
print(resp.request)  # <PreparedRequest [GET]>
print(resp.text)  # 直接这样访问会出错
# 所以我们需要把我们伪装的像一个用户访问，这就需要用到User-Ageent,把它放到headers中，然后在请求的时候当作头部传进去

resp.close()


