import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "./job/media")))

from media import Media

from fastapi import FastAPI
#from pydantic import BaseModel
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


@app.get("/")
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

