import pymongo
from pymongo import MongoClient

client = MongoClient ("mongodb+srv://admin:admin@cluster0.iicnuuo.mongodb.net/?retryWrites=true&w=majority")
db = client ["pytech"]
collection = db["students"]
print(db.list_collection_names)
################################################### pytech_insert
################################################### uncomment the post lines and the collection
post1 = {"_id": 1010, "First Name": "Chicken", "Last Name": "Wings"}
post2 = {"_id": 1011, "First Name": "Mongolian", "Last Name": "Beef"}
post3 = {"_id": 1013, "First Name": "Test", "Last Name": "Data"}
collection.insert_many([post1, post2, post3])