from fastapi import FastAPI
from modules import mongodb
import json
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/bookmark")
async def add_bookmark(url: str, label: str = None):
    # get current date and time
    now = datetime.now()
    dt = now.strftime("%d/%m/%Y %H:%M:%S")
    now = datetime.now()
    mydict = {"url": url, "label": label, "date": dt}
    x = mongodb.mycol.insert_one(mydict)
    print(x.inserted_id)
    return {"objId": str(x.inserted_id)}


@app.get("/view-bookmark")
async def send_bookmarks():
    bookmarks = []
    for x in mongodb.mycol.find({}, {"_id": 0}):
        bookmarks.append(x)
        # print(x)
    print(bookmarks)
    return bookmarks
