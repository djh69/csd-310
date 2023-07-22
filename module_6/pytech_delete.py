import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:<password>@cluster0.iicnuuo.mongodb.net/?retryWrites=true&w=majority")
db = client["pytech"]
collection = db["students"]
#
#################################################### pytech_delete
################################################### uncomment value and collection lines
value = {"_id": 1013}
collection.delete_one(value)

