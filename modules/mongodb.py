import pymongo
from config import config

myclient = pymongo.MongoClient(
    config.MONGO_URI)

mydb = myclient["bookmark_db"]
mycol = mydb["bookmarks"]
