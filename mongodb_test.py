import MongoClient
url = "mongodb+srv://admin:<password>@cluster0.iicnuuo.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
print(db.list_collection_names)