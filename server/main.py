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

class Selector(TypedDict):
    media: list[MediaSelector]
    person: list[PersonSelector]


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # 許可するオリジン
    allow_credentials=True,
    allow_methods=["*"],  # 許可するHTTPメソッド (GET, POSTなど)
    allow_headers=["*"],  # 許可するヘッダー
)

@app.get("/api/media/selector")
def read_root() -> Selector:
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

class ReqMediaSelector(BaseModel):
    pid: str

class ReqPersonSelector(BaseModel):
    mid: str

@app.post("/api/media/media_selector")
def media_selector(req: ReqMediaSelector):
    db = Media()

    if req.pid == "":
        m = db.select_media()
    else:
        m = db.select_media2(req.pid)
    m = cast(list[MediaSelector], m)
    return {"media": m}

@app.post("/api/media/person_selector")
def person_selector(req: ReqPersonSelector):
    db = Media()

    if req.mid == "":
        p = db.select_person()
    else:
        p = db.select_person2(req.mid)
    p = cast(list[PersonSelector], p)
    return {"person": p}
