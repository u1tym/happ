import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

from media import Media

def main():
    test6()


def test6():
    media = Media()
    res = media.select_person2("M0000002")
    print(res)


def test5():
    media = Media()
    res = media.select_media2("P0000002")
    print(res)

def test4():
    media = Media()
    media.regist({"pname":"悠木碧", "mname":"CD", "title":"妖精夜行", "release_date":"2024/10/1", "own":True, "code":"PRCL-10256-7", "note":""})
    media.regist({"pname":"悠木碧", "mname":"CD", "title":"ぐだふわエブリデー", "release_date":"2021/4/7", "own":False, "code":"COZC-1728-9", "note":""})
    media.regist({"pname":"悠木碧", "mname":"CD", "title":"Unbreakable", "release_date":"2020/1/15", "own":True, "code":"COZC-1609-10", "note":""})
    media.regist({"pname":"悠木碧", "mname":"CD", "title":"帰る場所があるということ", "release_date":"2018/4/25", "own":True, "code":"COZC-1432-3", "note":""})
    media.regist({"pname":"悠木碧", "mname":"CD", "title":"永遠ラビリンス", "release_date":"2017/11/1", "own":True, "code":"COZC-1383-4", "note":""})
    media.regist({"pname":"悠木碧", "mname":"CD", "title":"ボイスサンプル", "release_date":"2019/6/12", "own":True, "code":"COZX-1549-50", "note":""})

def test3():
    media = Media()

    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase MUSIC CLIP BOX 2",                   "release_date":"2025/06/18", "own":False, "code":"KIXM-627", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase MUSIC CLIP BOX",                     "release_date":"2019.06.26", "own":False, "code":"KIXM-379", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase LIVE TOUR HELLO HORIZON",            "release_date":"2022.02.23", "own":False, "code":"KIXM-493", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase 5th ANNIVERSARY LIVE Starry Wishes", "release_date":"2021.03.24", "own":False, "code":"KIXM-449", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase LIVE TOUR Catch the Rainbow!",       "release_date":"2019.10.23", "own":False, "code":"KIXM-398", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase LIVE TOUR heart bookmark",           "release_date":"2025.03.12", "own":False, "code":"KIXM-618～9", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase LIVE TOUR SCRAP ART",                "release_date":"2024.03.06", "own":False, "code":"KIXM-578〜9", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase LIVE TOUR glow",                     "release_date":"2023.04.19", "own":False, "code":"KIXM-536", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase LIVE TOUR BLUE COMPASS",             "release_date":"2018.10.17", "own":False, "code":"KIXM-340", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"BD", "title":"Inori Minase 1st LIVE Ready Steady Go!",          "release_date":"2018.04.04", "own":False, "code":"KIXM-315", "note":""})

    media.regist({"pname":"水瀬いのり", "mname":"CD", "title":"スクラップアート", "release_date":"2023.09.13", "own":False, "code":"KICM-2138", "note":"12th Single"})
    media.regist({"pname":"水瀬いのり", "mname":"CD", "title":"アイオライト",     "release_date":"2023.04.19", "own":False, "code":"KICM-2128", "note":"11th Single"})
    media.regist({"pname":"水瀬いのり", "mname":"配信", "title":"REAL-EYES",     "release_date":"2022.01.09", "own":False, "code":"", "note":""})
    media.regist({"pname":"水瀬いのり", "mname":"CD", "title":"HELLO HORIZON",     "release_date":"2021.07.21", "own":False, "code":"KICM-2092", "note":"10th Single"})
    media.regist({"pname":"水瀬いのり", "mname":"CD", "title":"Starlight Museum",     "release_date":"2020.12.02", "own":False, "code":"KICM-2065", "note":"9th Single"})
    media.regist({"pname":"水瀬いのり", "mname":"CD", "title":"ココロソマリ",     "release_date":"2020.02.05", "own":False, "code":"KICM-2029", "note":"8th Single"})
    media.regist({"pname":"水瀬いのり", "mname":"CD", "title":"Wonder Caravan!",     "release_date":"2019.01.23", "own":False, "code":"KICM-1914", "note":"7th Single"})
    media.regist({"pname":"水瀬いのり", "mname":"CD", "title":"TRUST IN ETERNITY!",     "release_date":"2018.10.17", "own":False, "code":"KICM-1890", "note":"6th Single"})

    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(1)",  "release_date":"2021.04.24", "own":True,  "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(2)",  "release_date":"",           "own":False, "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(3)",  "release_date":"",           "own":True,  "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(4)",  "release_date":"",           "own":True,  "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(5)",  "release_date":"",           "own":True,  "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(6)",  "release_date":"",           "own":True,  "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(7)",  "release_date":"",           "own":True,  "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(8)",  "release_date":"",           "own":False, "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(9)",  "release_date":"",           "own":False, "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(10)", "release_date":"",           "own":False, "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(11)", "release_date":"",           "own":False, "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(12)", "release_date":"",           "own":False, "code":"", "note":""})
    media.regist({"pname":"福田晋一", "mname":"COMIC", "title":"その着せ替え人形は恋をする(13)", "release_date":"",           "own":False, "code":"", "note":""})


def test2():
    media = Media()

    res = media.select_person()
    print(res)

def test1():
    media = Media()

    res = media.regist({"pname":"田村ゆかり", "mname":"CD", "title":"Felice",                                   "release_date":"2025/06/18", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE 2024 *Honey bunny*",           "release_date":"2025/01/29", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE 2023 *with me?*",              "release_date":"2024/03/27", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE 2022 *Meet Me?*",              "release_date":"2023/03/31", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"Acoustic Tour 2022 *Soundrops*",           "release_date":"2022/11/30", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE 2021 *Airy-Fairy Twintail*",   "release_date":"2022/04/20", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE 2019 *Twilight ♡ Chandelier*", "release_date":"2022/04/20", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"ゆかりっくFes’18 in Japan",                 "release_date":"2019/08/12", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"BIRTHDAY ♡ LIVE 2018 *Tricolore ♡ Plaisir*", "release_date":"2018/12/26", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"20th Anniversary LOVE ♡ LIVE 2017 *Crescendo ♡ Carol*", "release_date":"2018/05/23", "own":False, "code":"", "note":""})

    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE *Sunny side Lily*", "release_date":"2015/11/25", "own":False, "code":"", "note":""})

    res = media.regist({"pname":"田村ゆかり", "mname":"DVD", "title":"sweet chick girl", "release_date":"2002/10/23", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"DVD", "title":"Peachy Cherry Pie", "release_date":"2004/04/07", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"DVD", "title":"さまぁらいぶ☆2004 *Sugar Time Trip*", "release_date":"2004/12/08", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"DVD", "title":"*Cutie♡Cutie Concert * 2005", "release_date":"2006/03/08", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"DVD", "title":"LIVE 2006-2007 *Pinkle Twinkle ☆ Milky Way*", "release_date":"2007/12/24", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"DVD", "title":"LOVE ♡ LIVE *Chelsea Girl*", "release_date":"2008/07/23", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE *Dreamy Maple Crown*", "release_date":"2009/08/07", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE *Princess á la mode*", "release_date":"2010/06/16", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE *Mary Rose* ＆ *STARRY☆CANDY☆STRIPE*", "release_date":"2011/08/24", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE *I Love Rabbit*", "release_date":"2012/06/27", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE *Fall in Love*", "release_date":"2013.05.29", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"17才だよ?!ゆかりちゃん祭り!!", "release_date":"2013.07.24", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE *Cute’n ♡ Cute’n Heart*", "release_date":"2014.01.15", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE *Fruits Fruits ♡ Cherry* & *Caramel Ribbon*", "release_date":"2014.08.20", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"神楽坂ゆか ファーストコンサート～初めてだから…ね？お熱にサマーキッス♡～", "release_date":"2015.02.14", "own":False, "code":"", "note":""})
    res = media.regist({"pname":"田村ゆかり", "mname":"BD", "title":"LOVE ♡ LIVE *Lantana in the Moonlight*", "release_date":"2015.07.29", "own":False, "code":"", "note":""})

    print(res)

    return

if __name__ == '__main__':
    main()
