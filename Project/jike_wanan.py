# coding=utf-8
import requests
from lxml import etree
from pymongo import *
import re


def get_collection():
    client = MongoClient()
    db = client["xcc"]
    return db["xcc"]


def insert_db(ref, name):
    get_collection().insert({
        "url": "http://music.163.com" + ref,
        "name": name
    })


url = 'http://music.163.com/playlist?id=581223402'
headers = {'Host': 'music.163.com',
           'Origin': 'http://music.163.com',
           'Referer': 'http://music.163.com/',
           'User-Agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
r = requests.get(url, headers)
# print r.text + '\n'
html = etree.HTML(r.text)

# 歌名字
song_names = html.xpath('//ul[@class="f-hide"]/li/a')

# 歌的链接
song_refs = html.xpath('//ul[@class="f-hide"]/li/a/@href')

# <textarea style="display:none;">
singers = html.xpath('//div[@id="song-list-pre-cache"]/textarea[@style="display:none;"]')[0]

pattern = re.compile(r'<textarea style="display:none;">(.*?)</textarea>')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.search(r.text).group(1)

print match
# print singers.text



#
# for (ref, name) in zip(song_refs, song_names):
#     insert_db(ref, name.text)
