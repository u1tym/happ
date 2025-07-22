# media.pyのMediaクラスと同じようなAmountクラス

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../lib")))

from ppsqldb import Db
#from ppsqldb import TableType

from plog import Log

from typing import Optional

class Amount:
    _db: Optional[Db] = None
    _lg: Log
    last_error: str

    # コンストラクタを書いて
    def __init__(self, db: Optional[Db] = None, logger: Optional[Log] = None):
        if db is not None:
            self._db = db
        else:
            self._db = Db("127.0.0.1", 5432, "amtdb", "amtusr", "AMTAMT")  # Dbのデフォルトコンストラクタを使う場合

        if logger is not None:
            self._lg = logger
        else:
            self._lg = Log(0, "amount", ".")  # Logのデフォルトコンストラクタを使う場合

        self.last_error = ""
