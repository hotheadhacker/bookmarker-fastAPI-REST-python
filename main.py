from fastapi import FastAPI
from modules import mongodb

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/bookmark")
def get_bookmark(url: str, label: str = None):
    mydict = {"url": url, "label": label}
    x = mongodb.mycol.insert_one(mydict)
    print(x.inserted_id)
    return {"objId": str(x.inserted_id)}
