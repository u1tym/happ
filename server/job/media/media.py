# -*- coding: utf-8 -*-

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../libs")))

from db import Db

from typing import Self

class Media:

    def __init__(self: Self) -> None:
        db = Db("127.0.0.1", 5432, "mdadb", "mdbusr", "MEDIAMEDIA")
        res: bool = db.connect()
        if res != False:
            self._db = db

        return
