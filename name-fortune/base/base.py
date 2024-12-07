import pandas

imi = [
    "",
    "飛躍を表す根源数",
    "物質面や精神面が不安定",
    "感性で才能が開花",
    "努力が報われない",
    "行動力で信頼を得る",
    "大業を成せる",
    "目標を掲げ幸福に",
    "努力で成果を得る",
    "感情の浮沈で急変",
    "精神面が不安定",
    "堅実で人生が安定",
    "積極性や決断に欠ける",
    "あふれる魅力で成功",
    "不平不満が多い",
    "幸運を呼び込み安泰",
    "富と名声を得る",
    "一途な信念で目標達成",
    "努力と積極性で勝利",
    "流されやすく急変",
    "誘惑に弱く急変",
    "精神力で飛躍",
    "何事も中途挫折",
    "順調に躍進",
    "人気運と金運を持つ",
    "意志が頑固な実力派",
    "言動のムラが仇となる",
    "頑固さが孤立を呼ぶ",
    "融通がきかない",
    "芸術分野で才能を発揮",
    "独善的な態度が仇となる",
    "努力が着実に実を結ぶ",
    "富と名声を築く",
    "行動力のある野心家",
    "流されやすく急変",
    "温厚さと実力で幸福に",
    "志持つが中途挫折",
    "末広がりに努力が実る",
    "芸術方面で才能を発揮",
    "逆境を乗り越え躍進",
    "虚栄心から急変",
    "運と実力で早くから飛躍",
    "人任せで急変",
    "内情の激しさが悪化させる",
    "急変しやすい",
    "広い分野で活躍",
    "人にだまされやすい",
    "交際範囲がカギ",
    "天賦の才能を生かせる",
    "善し悪しが交差する",
    "浮き沈みを繰り返す",
    "繊細でマイペース",
    "信頼が強く飛躍",
    "目標達成しにくい",
    "気苦労が絶えない",
    "強引さが仇となる",
    "精神面がもろい",
    "困難を乗り越える",
    "強い精神力で飛躍",
    "世間から遠ざかる",
    "情緒不安定",
    "努力が実を結ぶ",
    "努力むなしく空振り",
    "順風満帆な人生に",
    "金銭問題が出る",
    "財を築き繁栄",
    "四面楚歌の状態になる",
    "周囲からの支持を受ける",
    "思慮深く幸運を招く",
    "精神的に困窮",
    "怠惰が運気を落とす",
    "いばらの道を切り開く",
    "悩みが絶えない",
    "下積みは長いが幸福に",
    "困難がつきまとう",
    "堅実で幸福な人生に",
    "自暴自棄で中途挫折",
    "善し悪しの差がはっきり",
    "孤軍奮闘して成功",
    "理想の世界に入り込む",
    "気力を失ってしまう",
    "幸福を一身に集める",
]
kikkyou = {
    1: "大吉",
    2: "凶",
    3: "大吉",
    4: "凶",
    5: "大吉",
    6: "大吉",
    7: "吉",
    8: "吉",
    9: "凶",
    10: "凶",
    11: "大吉",
    12: "凶",
    13: "大吉",
    14: "凶",
    15: "大吉",
    16: "大吉",
    17: "吉",
    18: "吉",
    19: "凶",
    20: "凶",
    21: "大吉",
    22: "凶",
    23: "大吉",
    24: "大吉",
    25: "大吉",
    26: "凶",
    27: "吉凶混合",
    28: "凶",
    29: "大吉",
    30: "吉凶混合",
    31: "大吉",
    32: "大吉",
    33: "大吉",
    34: "凶",
    35: "吉",
    36: "吉凶混合",
    37: "大吉",
    38: "吉",
    39: "大吉",
    40: "吉凶混合",
    41: "大吉",
    42: "吉凶混合",
    43: "凶",
    44: "凶",
    45: "大吉",
    46: "凶",
    47: "大吉",
    48: "大吉",
    49: "凶",
    50: "凶",
    51: "吉凶混合",
    52: "大吉",
    53: "吉凶混合",
    54: "凶",
    55: "吉凶混合",
    56: "凶",
    57: "吉",
    58: "吉",
    59: "凶",
    60: "凶",
    61: "吉",
    62: "凶",
    63: "大吉",
    64: "凶",
    65: "大吉",
    66: "凶",
    67: "大吉",
    68: "大吉",
    69: "凶",
    70: "凶",
    71: "吉凶混合",
    72: "吉凶混合",
    73: "吉凶混合",
    74: "凶",
    75: "吉凶混合",
    76: "凶",
    77: "吉凶混合",
    78: "吉凶混合",
    79: "凶",
    80: "凶",
    81: "大吉",
}


def check(myoji="山田", namae="太郎"):
    tenkaku = 0
    tenkaku_kekka = ""

    tikaku = 0
    tikaku_kekka = ""

    jinkaku = 0
    jinkaku_kekka = ""

    soukaku = 0
    soukaku_kekka = ""

    gaikaku = 0
    gaikaku_kekka = ""

    text = pandas.read_csv("http://ktu.iinaa.net/kanji-kakusu.csv", encoding="utf-8")
    kanji = text.loc[:, "kanji"]
    kakusu = text.loc[:, "kakusu"]

    # 天格
    for a in range(len(myoji)):
        for i in range(len(kanji)):
            if myoji[a] == kanji[i]:
                tenkaku = tenkaku + kakusu[i]

    tenkaku_kekka = imi[int(tenkaku)]

    # 地格
    for a in range(len(namae)):
        for i in range(len(kanji)):
            if namae[a] == kanji[i]:
                tikaku = tikaku + kakusu[i]

    tikaku_kekka = imi[int(tikaku)]

    # 総画
    for a in range(len(myoji)):
        for i in range(len(kanji)):
            if myoji[a] == kanji[i]:
                soukaku = soukaku + kakusu[i]

    for a in range(len(namae)):
        for i in range(len(kanji)):
            if namae[a] == kanji[i]:
                soukaku = soukaku + kakusu[i]

    soukaku_kekka = imi[int(soukaku)]

    # 人格
    for i in range(len(kanji)):
        if myoji[-1] == kanji[i]:
            jinkaku = jinkaku + kakusu[i]
            break

    for i in range(len(kanji)):
        if namae[0] == kanji[i]:
            jinkaku = jinkaku + kakusu[i]
            break

    jinkaku_kekka = imi[int(jinkaku)]

    # 外格
    for i in range(len(kanji)):
        if myoji[0] == kanji[i]:
            gaikaku = gaikaku + kakusu[i]
            break
    for i in range(len(kanji)):
        if namae[-1] == kanji[i]:
            gaikaku = gaikaku + kakusu[i]
            break

    gaikaku_kekka = imi[int(gaikaku)]

    return f"""〜{myoji} {namae}さんの姓名判断占い結果〜

総画:{round(soukaku)}画、結果:「{soukaku_kekka}」、吉凶:「{kikkyou[soukaku]}」
        姓と名の画数を合計したもので全体運・生涯運で一生を通じた運を表す

地格:{round(tikaku)}画、結果:「{tikaku_kekka}」、吉凶:「{kikkyou[tikaku]}」
        名に当たる画数でその人の基本的な部分を表す

天格:{round(tenkaku)}画、結果:「{tenkaku_kekka}」、吉凶:「{kikkyou[tenkaku]}」
        姓にあたる部分で先祖から与えられた天運を表す

人格:{round(jinkaku)}画、結果:「{jinkaku_kekka}」、吉凶:「{kikkyou[jinkaku]}」
        姓の最後と名の頭文字の画数を足したものでその人の内面を表す
                
外格:{round(gaikaku)}画、結果:「{gaikaku_kekka}」、吉凶:「{kikkyou[gaikaku]}」
        総格から人格を引いたもので対人関係や対外的な要素を表す
        
※あくまでこれは、占いの結果に過ぎません※"""


x = check("", "")  # 一番目が名字、二番目が名前

with open("占い/結果.txt", "w", encoding="utf-8") as file:
    file.write(x)
