import requests

url = 'https://movie.douban.com/typerank'

par = {
    'type': 24,
    'interval_id': '100:90',
    'action': '',
    'start': 0,
    'limit': 20,
}

head = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'
}
resp = requests.get(url, params=par, headers=head)

print(resp.request.url)

print(resp.text)

resp.close()
