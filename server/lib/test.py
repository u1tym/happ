import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

from db import Db

def main() -> None:
    mydb: Db = Db("127.0.0.1", 5432, "nbsdb", "nbs1", "nbs100")

    res: bool = mydb.connect()
    print("connect", res)
    print(mydb.last_error)

    res2 = mydb.fetchall("select * from bzz_section_mst")
    if res2 == False:
        print("select error")
        print(mydb.last_error)
    else:
        print(res2)

    mydb.disconnect()

    return


if __name__ == '__main__':
    main()
