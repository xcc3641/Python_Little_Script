# coding=utf-8
import requests
from lxml import etree
from pymongo import *
import re
import json

db_music = "music"


def get_collection(name):
    client = MongoClient()
    db = client["xcc"]
    return db[name]


def insert_data():
    url = 'http://music.163.com/playlist?id=581223402'
    headers = {'Host': 'music.163.com',
               'Origin': 'http://music.163.com',
               'Referer': 'http://music.163.com/',
               'User-Agen': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    r = requests.get(url, headers)

    '''
    发现有 json 数据直接获取
    html = etree.HTML(r.text)

    # 歌名字
    song_names = html.xpath('//ul[@class="f-hide"]/li/a')

    # 歌的链接
    song_refs = html.xpath('//ul[@class="f-hide"]/li/a/@href')

    '''

    # <textarea style="display:none;">
    pattern = re.compile(r'<textarea style="display:none;">(.*?)</textarea>')

    # 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
    match = pattern.search(r.text).group(1)
    j = json.loads(match)
    print type(j), j
    get_collection(db_music).insert_many(j)


def get_artist_name(cursor):
    return cursor["artists"][0]["name"]


def query():
    song_list = []
    for i in get_collection(db_music).find():
        data = {
            "name": i["name"],
            "id": i["id"],
            "artists": get_artist_name(i),
        }
        song_list.append(data)
    return song_list


# get_collection("test").insert_many(query())


def ishan(text):
    return all(u'\u4e00' <= char <= u'\u9fff' for char in text)


for i in get_collection("test").find():
    print i["name"], ishan(i["name"])
