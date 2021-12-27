import requests
url = 'https://fanyi.baidu.com/sug'

val = input('请输入你所要查询的单词')
dat = {
    'kw':val
}

# 发送post请求，发送的数据必须放在字典里，通过data参数进行传递
resp = requests.post(url, data=dat)
print(resp.json())  # 将服务器返回的内容直接处理成json 在python中就是 => 字典

resp.close()
