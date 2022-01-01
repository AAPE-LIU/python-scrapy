from lxml import etree
import requests

url = 'https://hubei.zbj.com/search/f/?kw=saas'
resp = requests.get(url)
# print(resp.text)
tree = etree.HTML(resp.text)
path = '/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div'
# 拿到每一个服务商的div
result1 = tree.xpath(path)
for div in result1:  # 每一个服务商的信息
    price = div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip('¥')
    num = div.xpath('./div/div/a[2]/div[2]/div[1]/span[2]/text()')[0]
    title = 'saas'.join(div.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))
    company = div.xpath('./div/div/a[1]/div[1]/p/text()')[1].strip()
    locate = div.xpath('./div/div/a[1]/div[1]/div/span/text()')
    print(price,num,title,company,locate)



