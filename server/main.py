import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "./job/media")))

from media import Media

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from typing import TypedDict
from typing import cast

class MediaSelector(TypedDict):
    mid: str
    mname: str

class PersonSelector(TypedDict):
    pid: str
    pname: str

class MediaItem(TypedDict):
    rid: str
    media: MediaSelector
    person: PersonSelector
    title: str
    release: str
    own: bool

class Selector(TypedDict):
    media: list[MediaSelector]
    person: list[PersonSelector]

server_ip = "localhost"
#server_ip = "192.168.0.250"
#server_ip = "ytym.sytes.net"

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    #allow_origins=["http://localhost:5173"],  # 許可するオリジン
    allow_origins=["http://" + server_ip + ":5173"],  # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],  # 許可するHTTPメソッド (GET, POSTなど)
    allow_headers=["*"],  # 許可するヘッダー
)

@app.get("/api/media/selector")
def read_root() -> Selector:
    print("selector")
    db = Media()
    m = db.select_media()
    p = db.select_person()

    m = cast(list[MediaSelector], m)
    p = cast(list[PersonSelector], p)
    result: Selector = {
        "media": m,
        "person": p,
    }
    return result

# IF media一覧取得要求
class IFReqMediaSelector(BaseModel):
    pid: str

# IF person一覧取得要求
class IFReqPersonSelector(BaseModel):
    mid: str

# IF item一覧取得要求
class IFReqMediaItem(BaseModel):
    mid: str
    pid: str

# IF item更新要求
class IFUpdItem(BaseModel):
    rid: str
    media: str
    person: str
    own: bool
    release: str
    title: str

# IF item削除要求
class IFDelItem(BaseModel):
    rid: str


@app.post("/api/media/media_selector")
def media_selector(req: IFReqMediaSelector):
    db = Media()

    if req.pid == "":
        m = db.select_media()
    else:
        m = db.select_media2(req.pid)
    m = cast(list[MediaSelector], m)
    return {"media": m}

@app.post("/api/media/person_selector")
def person_selector(req: IFReqPersonSelector):
    db = Media()

    if req.mid == "":
        p = db.select_person()
    else:
        p = db.select_person2(req.mid)
    p = cast(list[PersonSelector], p)
    return {"person": p}

@app.post("/api/media/select_item")
def select_item(req: IFReqMediaItem):
    db = Media()

    res: list[MediaItem] = []
    itm = db.select_item(req.mid, req.pid)
    if itm == False:
        pass
    else:
        for one in itm:
            add_one: MediaItem = {
                "rid": one["rid"],
                "media": one["media"],
                "person": one["person"],
                "own": one["own"],
                "release": one["release"],
                "title": one["title"]
            }
            res.append(add_one)

    return {"item": res}

@app.post("/api/media/update_item")
def update_item(req: IFUpdItem):
    print("update!!!")
    db = Media()

    res = db.update(
        req.rid,
        {
            "mname": req.media,
            "pname": req.person,
            "code": "",
            "title": req.title,
            "release": req.release,
            "own": req.own,
            "note": ""
        } )
    print(res)

    return {"result": res}

@app.post("/api/media/delete_item")
def delete_item(req: IFDelItem):
    db = Media()

    db.delete(req.rid)

    return {"result": True}
