import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../lib")))

from db import Db
from db import TableType

from log import Log

from typing import TypedDict
from typing import Optional
from typing import Union
from typing import Literal
from typing import Self
from typing import cast


class MediaRecord(TypedDict):
    pname: str
    mname: str
    title: str
    release: str
    own: bool
    code: str
    note: str


# === DB(内部) ===

# Person
class EntPRecord(TypedDict):
    pid: str
    pname: str

# Media
class EntMRecord(TypedDict):
    mid: str
    mname: str

# Item
class EntIRecord(TypedDict):
    rid: str
    person: EntPRecord
    media: EntMRecord
    title: str
    release: str
    note: str
    own: bool

class Media:
    _db: Optional[Db] = None
    _lg: Log
    last_error: str

    def __init__(self: Self, log: Optional[Log] = None) -> None:
        """
        コンストラクタ
        """

        try:
            # LOG設定
            if log is not None:
                self._lg = log
            else:
                self._lg = Log(0, "media", ".")

            # DB接続
            db = Db("127.0.0.1", 5432, "mdadb", "mdausr", "MEDIAMEDIA")
            res = db.connect()
            if res == False:
                self._lg.output("ERR", "DB接続異常")
                self._lg.output("ERR", db.last_error)
                return

            self._lg.output("DBG", "DB接続")
            self._db = db
        except Exception as e:
            self.last_error = str(e)
            self._lg.output("ERR", "処理異常")
            self._lg.output("ERR", self.last_error)

    def select_person(self: Self) -> Union[Literal[False], list[EntPRecord]]:
        """
        note:
            personの一覧 を取得する
        """
        if self._db is None:
            return False
        result: list[EntPRecord] = []

        rows = self._db.fetchall("select pid, pname from person")
        if rows != False:
            for row in rows:
                row = cast(dict[str, str], row)
                result.append({
                    "pid": row["pid"],
                    "pname": row["pname"]
                    })

        return result


    def select_person2(self: Self, mid: str) -> Union[Literal[False], list[EntPRecord]]:
        """
        note:
            指定した mid をもつ personの一覧 を取得する
        """
        if self._db is None:
            return False
        result: list[EntPRecord] = []

        sql: str = (
            "select p.pid as pid, p.pname as pname"
            + " from person as p"
            + " inner join mda_rec as r"
            + " on r.pid = p.pid"
            + " and r.mid = '" + mid + "'"
            + " group by p.pid, p.pname"
            + " order by p.pid"
        )

        rows = self._db.fetchall(sql)
        if rows != False:
            for row in rows:
                row = cast(dict[str, str], row)
                result.append({
                    "pid": row["pid"],
                    "pname": row["pname"]
                    })

        return result


    def select_media(self: Self) -> Union[Literal[False], list[EntMRecord]]:
        """
        note:
            mediaの一覧 を取得する
        """
        if self._db is None:
            return False
        result: list[EntMRecord] = []

        rows = self._db.fetchall("select mid, mname from media")
        if rows != False:
            for row in rows:
                row = cast(dict[str, str], row)
                result.append({
                    "mid": row["mid"],
                    "mname": row["mname"]
                })

        return result

    def select_media2(self: Self, pid: str) -> Union[Literal[False], list[EntMRecord]]:
        """
        note:
            指定した pid をもつ mediaの一覧 を取得する
        """
        if self._db is None:
            return False

        sql: str = (
            "select m.mid as mid, m.mname as mname"
            + " from media as m"
            + " inner join mda_rec as r"
            + " on r.mid = m.mid"
            + " and r.pid = '" + pid + "'"
            + " group by m.mid, m.mname"
            + " order by m.mid"
        )

        result: list[EntMRecord] = []

        rows = self._db.fetchall(sql)
        if rows != False:
            for row in rows:
                row = cast(dict[str, str], row)
                result.append({
                    "mid": row["mid"],
                    "mname": row["mname"]
                })

        return result


    def select_item(self: Self, mid: str, pid: str):
        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        sql: str = (
            "select"
            + " r.rid as rid,"
            + " r.pid as pid, p.pname as person,"
            + " r.mid as mid, m.mname as media,"
            + " r.title as title, r.release as release, r.own as own, r.note as note"
            + " from mda_rec as r"
            + " inner join media as m"
            + " on m.mid = r.mid"
            + ("" if mid == "" else " and m.mid = '" + mid + "'")
            + " inner join person as p"
            + " on p.pid = r.pid"
            + " and p.pid = '" + pid + "'"
            + " where r.delflg = False"
            + " order by r.release, r.title"
        )
        self._lg.output("DBG", sql)

        result: list[EntIRecord] = []

        rows = self._db.fetchall(sql)
        if rows != False:
            for row in rows:
                row = cast(dict[str, str], row)
                add_res: EntIRecord = {
                    "rid": row["rid"],
                    "person": {
                        "pid": row["pid"],
                        "pname": row["person"],
                    },
                    "media": {
                        "mid": row["mid"],
                        "mname": row["media"],
                    },
                    "own": cast(bool, row["own"]),
                    "release": row["release"],
                    "title": row["title"],
                    "note": row["note"]
                }
                result.append(add_res)

        return result


    def regist(self: Self, record: MediaRecord) -> bool:
        """
        登録処理
        """

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        res_p = self._regist_person(record["pname"])
        if res_p == False:
            return False

        res_m = self._regist_media(record["mname"])
        if res_m == False:
            return False

        isexist = self._is_exist_mda_rec(res_p, res_m, record["title"])
        if isexist:
            self._lg.output("INF", "既に存在")
            self._db.commit()
            return True

        res_rec = self._ins_mda_rec(res_p, res_m, record["code"], record["title"], record["note"], record["release"], record["own"])
        if res_rec == False:
            return False

        self._db.commit()

        return True


    def update(self: Self, rid: str, record: MediaRecord) -> bool:
        """
        更新処理
        """

        if rid == "":
            return self.regist(record)

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        res_p = self._regist_person(record["pname"])
        if res_p == False:
            self._lg.output("ERR", "person登録処理異常")
            return False

        res_m = self._regist_media(record["mname"])
        if res_m == False:
            self._lg.output("ERR", "media登録処理異常")
            return False

        res_u = self._upd_mda_rec(rid, res_p, res_m, record["code"], record["title"], record["note"], record["release"], record["own"])
        if res_u == False:
            self._lg.output("ERR", "mda_rec更新処理異常")
            return False

        self._db.commit()

        return True


    def delete(self: Self, rid: str) -> bool:
        """
        更新処理
        """

        if rid == "":
            return False

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        self._del_mda_rec(rid)

        self._db.commit()

        return True


    def test_get_pid(self: Self, pname: str) -> Union[Literal[False], None, None, str]:
        return self.__get_pid(pname)

    def test_ins_pid(self: Self, pname: str) -> Union[Literal[False], str]:
        return self.__ins_pid(pname)

    def test_regist_person(self: Self, pname: str) -> Union[Literal[False], str]:
        print("test_regist_person")
        return self._regist_person(pname)

    def test_regist_media(self: Self, mname: str) -> Union[Literal[False], str]:
        print("test_regist_media")
        return self._regist_media(mname)



    def _regist_person(self: Self, pname: str) -> Union[Literal[False], str]:
        """
        person登録処理
        """

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        # 登録済み確認
        isExist = self.__get_pid(pname)
        if isExist == False:
            self._lg.output("ERR", "登録済み確認処理時の処理異常")
            return False

        if isinstance(isExist, str):
            # 登録済み
            self._lg.output("DBG", "登録済み[" + isExist + "]")
            return isExist

        self._lg.output("DBG", "未登録のため、登録を実施")
        pid = self.__ins_pid(pname)
        if pid == False:
            self._lg.output("ERR", "登録処理異常")
            return False
        self._lg.output("DBG", "登録完了 [" + pid + "]")

        return pid


    def _regist_media(self: Self, mname: str) -> Union[Literal[False], str]:
        """
        media登録処理
        """

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        # 登録済み確認
        isExist = self.__get_mid(mname)
        if isExist == False:
            self._lg.output("ERR", "登録済み確認処理時の処理異常")
            return False

        if isinstance(isExist, str):
            # 登録済み
            self._lg.output("DBG", "登録済み[" + isExist + "]")
            return isExist

        self._lg.output("DBG", "未登録のため、登録を実施")
        mid = self.__ins_mid(mname)
        if mid == False:
           self._lg.output("ERR", "登録処理異常")
           return False
        self._lg.output("DBG", "登録完了 [" + mid + "]")

        return mid


    def __get_pid(self: Self, pname: str) -> Union[Literal[False], None, str]:
        """
        [内部] PIDの取得

        Args:
        pname (str): person名

        Returns:
        False: 処理異常
        None: 登録なし
        pid (str): 登録したPID
        """

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        sql: str = "select pid from person where pname = '" + pname + "'"
        res: Union[TableType, Literal[False]] = self._db.fetchall(sql)
        if res == False:
            self._lg.output("ERR", "fetchall()処理異常")
            self._lg.output("ERR", self._db.last_error)
            return False

        row = cast(list[dict[str, str]], res)
        if len(row) == 0:
            self._lg.output("ERR", "登録失敗")
            return None

        result: str = row[0]["pid"]

        self._lg.output("DBG", "取得完了 [" + result + "]")
        return result


    def __ins_pid(self: Self, pname: str) -> Union[Literal[False], str]:
        """
        [内部] personの登録

        Args:
        pname (str): person名

        Returns:
        False: 処理異常
        pid (str): 登録したPID
        """

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        sql: str = (
            "insert into person (pid, pname) values ("
            + "(select 'P' || LPAD((coalesce(max(substring(pid from 2)::integer), 0) + 1)::text, 7, '0') from person), "
            + "'" + pname + "'"
            + ") returning pid"
            )
        self._lg.output("DBG", sql)

        res = self._db.fetchall(sql)
        if res == False:
            self._lg.output("ERR", "fetchall()処理異常")
            self._lg.output("ERR", self._db.last_error)
            return False

        row = cast(list[dict[str, str]], res)
        if len(row) != 1:
            self._lg.output("ERR", "処理異常 件数=[" + str(len(row)) + "]")
            return False

        result: str = row[0]["pid"]
        self._lg.output("DBG", "登録完了 [" + result + "]")

        return result


    def __get_mid(self: Self, mname: str) -> Union[Literal[False], None, str]:
        """
        [内部] MIDの取得

        Args:
            pname (str): media名

        Returns:
            False: 処理異常
            None: 登録なし
            pid (str): 取得したMID
        """

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        sql: str = "select mid from media where mname = '" + mname + "'"
        self._lg.output("DBG", sql)

        res: Union[TableType, Literal[False]] = self._db.fetchall(sql)
        if res == False:
            self._lg.output("ERR", "fetchall()処理異常")
            self._lg.output("ERR", self._db.last_error)
            return False

        row = cast(list[dict[str, str]], res)
        if len(row) == 0:
            return None

        result: str = row[0]["mid"]
        return result


    def __ins_mid(self: Self, mname: str) -> Union[Literal[False], str]:
        """
        [内部] mediaの登録

        Args:
        mname (str): media名

        Returns:
        False: 処理異常
        mid (str): 登録したMID
        """

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        sql: str = (
            "insert into media (mid, mname) values ("
            + "(select 'M' || LPAD((coalesce(max(substring(mid from 2)::integer), 0) + 1)::text, 7, '0') from media),"
            + "'" + mname + "'"
            + ") returning mid"
        )
        self._lg.output("DBG", sql)

        res = self._db.fetchall(sql)
        if res == False:
            self._lg.output("ERR", "fetchall()処理異常")
            self._lg.output("ERR", self._db.last_error)
            return False

        row = cast(list[dict[str, str]], res)
        if len(row) != 1:
            return False

        return row[0]["mid"]


    def _is_exist_mda_rec(self: Self, pid: str, mid: str, title: str) -> bool:
        """
        Returns:
            True: 存在
            False: 存在を確認できない
        """

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        sql: str = (
            "select rid from mda_rec "
            + "where pid = '" + pid + "' "
            + "and mid = '" + mid + "' "
            + "and title = '" + title + "' "
            + "and delflg = " + str(False)
        )
        self._lg.output("DBG", sql)

        res = self._db.fetchall(sql)
        if res == False:
            self._lg.output("ERR", "fetchall()処理異常")
            self._lg.output("ERR", self._db.last_error)
            return False

        row = cast(list[dict[str, str]], res)
        if len(row) > 0:
            return True

        return False


    def _ins_mda_rec(
            self: Self,
            pid: str, mid: str,
            code: str,
            title: str,
            note: str,
            release: str,
            own: bool) -> Union[Literal[False], str]:

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        sql: str = (
            "insert into mda_rec (rid, pid, mid, title, release, code, note, own) values ( "
            "(select 'R' || LPAD((coalesce(max(substring(rid from 2)::integer), 0) + 1)::text, 7, '0') from mda_rec), "
            + "'" + pid + "', "
            + "'" + mid + "', "
            + "'" + title + "', "
            + ("null" if release == "" else "'" + release + "'") + ", "
            + "'" + code + "', "
            + "'" + note + "', "
            + str(own) + " "
            + ") returning rid"
        )
        self._lg.output("DBG", sql)

        res = self._db.fetchall(sql)
        if res == False:
            self._lg.output("ERR", "fetchall()処理異常")
            self._lg.output("ERR", self._db.last_error)
            return False

        row = cast(list[dict[str, str]], res)
        if len(row) != 1:
            self._lg.output("ERR", "処理異常 件数=[" + str(len(row)) + "]")
            return False

        result: str = row[0]["rid"]
        self._lg.output("DBG", "登録完了 [" + result + "]")
        return result

    def _upd_mda_rec(
            self: Self,
            rid: str,
            pid: str, mid: str,
            code: str,
            title: str,
            note: str,
            release: str,
            own: bool) -> Union[Literal[False], str]:

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        sql: str = (
            "update mda_rec"
            + " set "
            + " pid = '" + pid + "'"
            + ", mid = '" + mid + "'"
            + ", title = '" + title + "'"
            + ", release = " + ("null" if release == "" else "'" + release + "'")
            + ", code = '" + code + "'"
            + ", note = '" + note + "'"
            + ", own = " + str(own)
            + ", udate = now()"
            + " where rid = '" + rid + "'"
            + " returning rid"
        )
        self._lg.output("DBG", sql)

        res = self._db.fetchall(sql)
        if res == False:
            self._lg.output("ERR", "fetchall()処理異常")
            self._lg.output("ERR", self._db.last_error)
            return False

        row = cast(list[dict[str, str]], res)
        if len(row) != 1:
            self._lg.output("ERR", "処理異常 件数=[" + str(len(row)) + "]")
            return False

        result: str = row[0]["rid"]
        self._lg.output("DBG", "更新完了 [" + result + "]")
        return result

    def _del_mda_rec(
            self: Self,
            rid: str) -> bool:

        if self._db is None:
            self._lg.output("ERR", "DB未接続")
            return False

        sql: str = (
            "delete from mda_rec"
            + " where rid = '" + rid + "'"
            + " returning rid"
        )
        self._lg.output("DBG", sql)

        res = self._db.fetchall(sql)
        if res == False:
            self._lg.output("ERR", "fetchall()処理異常")
            self._lg.output("ERR", self._db.last_error)
            return False

        row = cast(list[dict[str, str]], res)
        if len(row) != 1:
            self._lg.output("ERR", "処理異常 件数=[" + str(len(row)) + "]")
            return False

        self._lg.output("DBG", "更新完了 [" + str(True) + "]")
        return True
