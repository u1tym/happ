# media.pyのMediaクラスと同じようなAmountクラス

import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

#import os
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../lib")))

from datetime import datetime as dtm

from ppsqldb import Db
#from ppsqldb import TableType

from plog import Log

from typing import Optional
from typing import Self
from typing import TypedDict

class CardInfo(TypedDict):
    cname: str
    due: int
    pay_month: int
    pay_day: int

class PayInfo(TypedDict):
    st: dtm
    ed: dtm
    amount: int

class AmountRec(TypedDict):
    aid: Optional[str]
    yymmdd: dtm
    useful: str
    cname: str
    amount: int

class Amount:
    _db: Optional[Db] = None
    _lg: Log
    last_error: str

    # コンストラクタを書いて
    def __init__(self: Self, db: Optional[Db] = None, logger: Optional[Log] = None):
        if db is not None:
            self._db = db
        else:
            self._db = Db("127.0.0.1", 5432, "amtdb", "amtusr", "AMTAMT")  # Dbのデフォルトコンストラクタを使う場合

        if logger is not None:
            self._lg = logger
        else:
            self._lg = Log(0, "amount", ".")  # Logのデフォルトコンストラクタを使う場合

        self.last_error = ""

    def _connect(self: Self) -> bool:
        if self._db is None:
            return False

        res = self._db.connect()
        if res != True:
            return False

        return True

    def get_card_list(self: Self) -> list[CardInfo]:
        """ cardリストの取得 """
        result: list[CardInfo] = []

        if self._db is None:
            return result

        return result

    def add_amount(self: Self, rec: AmountRec) -> bool:
        """ amountの追加 """
        return False

    def update_amount(self: Self, rec: AmountRec) -> bool:
        """ amountの更新 """
        return False

    def delete_amount(self: Self, aid: int) -> bool:
        """ amountの削除 """
        return False

    def get_amount_list(self: Self, st: dtm, ed: dtm) -> list[AmountRec]:
        """ amountの取得 """
        result: list[AmountRec] = []
        return result

    def get_payment(self: Self, base: dtm) -> list[PayInfo]:
        """ payment情報の取得 """
        result: list[PayInfo] = []
        return result
