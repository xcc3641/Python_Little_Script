import requests
from lxml import etree

url = 'http://music.163.com/playlist?id=581223402'
headers = {'Host': 'music.163.com',
           'Origin': 'http://music.163.com',
           'Referer': 'http://music.163.com/',
           'User-Agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get(url, headers)
print r.text+'\n'
html = etree.HTML(r.text)

results = html.xpath('//ul[@class="f-hide"]/li/a')


for item in results:
    print item.text


