import pymongo
from config import config

myclient = pymongo.MongoClient(
    config.MONGO_URI)

# check if db exists
# dblist = myclient.list_database_names()
# if "bookmark_db" in dblist:
#     print("The database exists.")

mydb = myclient["bookmark_db"]
mycol = mydb["customers"]

mydict = {"name": "Peter", "address": "Lowstreet 27"}

x = mycol.insert_one(mydict)

print(x.inserted_id)

print(mydb.list_collection_names())
