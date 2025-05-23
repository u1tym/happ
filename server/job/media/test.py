import sys
import warnings

sys.dont_write_bytecode = True
warnings.filterwarnings('ignore')

from media import Media

def main():
    test1()


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
