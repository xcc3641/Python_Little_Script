# coding=utf-8
from pymongo import *

client = MongoClient()
# xcc 是数据库的名字
db = client["xcc"]
#  xcc_colleciton 需要进行操作类似 Android cursor 
collection = db.xcc_collection

for i in collection.find({"name": "三弟"}):
    print i["name"]
