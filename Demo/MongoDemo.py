# coding=utf-8
from pymongo import *
from bson.objectid import ObjectId

client = MongoClient()
# xcc 是数据库的名字
db = client["xcc"]

# 查看全部聚集名称
print db.collection_names()

# 需要进行操作类似 Android cursor
# 连接聚集
collection = db["xcc"]


def query():
    # 查看聚集的一条记录
    print collection.find_one({"name": "三弟"})["_id"]

    # 查看聚集的多条记录
    for i in collection.find():
        print i["name"]


def insert():
    collection.insert({"name": "三弟"})
    document = ({"name": "三弟",
                 "age": 22,
                 "sex": "男"
                 })
    collection.insert(document)


def update():
    # 根据 mongo 自带的 id 查找的话，需要用 ObjectId 包裹
    collection.update({"_id": ObjectId("589b39db2fc7f0b180633400")}, {"$set": {"name": "四弟"}})
