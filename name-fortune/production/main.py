import json
import pathlib


def print_dbg(msg):
    """プリントデバッグ用

    Args:
        msg (_type_): デバッグしたい関数名
    """

    print(msg)
    print(type(msg))


def read_json(kanji_dir: pathlib, kana_dir: pathlib, result_dir: pathlib) -> list:
    """文字と画数が入ったjsonファイルを読み込む

    Args:
        dir (pathlib): jsonのパス

    Returns:
        list: 文字カラムのデータ
        list: 画数カラムのデータ
        list: 結果のデータ
    """
    print("jsonファイルを読み込みます。少々お待ちください。")

    try:
        with kanji_dir.open("r", encoding="utf-8") as f:
            json_kanji_data: list = json.load(f)

        with kana_dir.open("r", encoding="utf-8") as f:
            json_kana_data: list = json.load(f)

        with result_dir.open("r", encoding="utf-8") as f:
            json_result_data: list = json.load(f)

    except FileNotFoundError as e:
        print(
            "エラー！jsonファイルが見つかりませんでした。パスとファイル名を確認してください。"
        )
        raise

    return json_kanji_data, json_kana_data, json_result_data


def kakushu_check(sei: str, mei: str, kanji_list: list, kana_list: list) -> list:
    """画数をチェックする

    Args:
        sei (str): 画数を知りたい姓
        mei (str): 画数を知りたい名
        kanji_list (list): read_jsonで取得した漢字データ
        kana_list (list): read_jsonで取得したかなデータ

    Raises:
        ValueError: 文字データの中に該当する文字がなかった場合（姓）
        ValueError: 文字データの中に該当する文字がなかった場合（名）

    Returns:
        list: 姓の画数データ
        list: 名の画数データ
    """
    result_sei: list = []
    result_mei: list = []

    # 画数の取得
    print("画数を取得しています。")

    try:
        for a in range(len(sei)):
            found: bool = False
            for i in range(len(kanji_list)):
                if sei[a] == kanji_list[i]["kanji"]:
                    result_sei.append(kanji_list[i]["kakusu"])
                    found = True
            for i in range(len(kana_list)):
                if sei[a] == kana_list[i]["kanji"]:
                    result_sei.append(kana_list[i]["kakusu"])
                    found = True
            if not found:
                raise ValueError(f"姓の文字「{sei[a]}」が見つかりませんでした。")

        for a in range(len(mei)):
            found: bool = False
            for i in range(len(kanji_list)):
                if mei[a] == kanji_list[i]["kanji"]:
                    result_mei.append(kanji_list[i]["kakusu"])
                    found = True
            for i in range(len(kana_list)):
                if mei[a] == kana_list[i]["kanji"]:
                    result_mei.append(kana_list[i]["kakusu"])
                    found = True
            if not found:
                raise ValueError(f"名の文字「{mei[a]}」が見つかりませんでした。")

    except ValueError as e:
        raise

    return result_sei, result_mei


def calc_tenkaku(sei: list) -> int:
    """地角を計算

    Args:
        sei (list): kakushu_check()で取得した姓の画数

    Returns:
        int: 画数の合計
        str: 吉凶
        str: メッセージ
    """
    calc_sei: int = 0

    for a in range(len(sei)):
        calc_sei += sei[a][0]

    return calc_sei


def calc_chikaku(mei: list) -> int:
    """地格を計算

    Args:
        mei (list): kakushu_check()で取得した名の画数

    Returns:
        int: 画数の合計
    """
    calc_mei: int = 0

    for a in range(len(mei)):
        calc_mei += mei[a][0]

    return calc_mei


def calc_soukaku(sei: int, mei: int) -> int:
    """総画を計算

    Args:
        sei (int): 姓の合計数（calc_tenkaku）
        mei (int): 名の合計数（calc_chikaku）

    Returns:
        int: 姓+名の合計（総画）
    """
    calc_sokaku: int = sei + mei
    return calc_sokaku


def calc_zinkaku(sei: list, mei: list) -> int:
    """人格を計算

    Args:
        sei (list): kakushu_check()で取得した姓の画数
        mei (list): kakushu_check()で取得した名の画数

    Returns:
        int: 姓の最後と名の最初を合計
    """
    calc_zinkaku: int = sei[-1][0] + mei[0][0]
    return calc_zinkaku


def calc_gaikaku(sei: list, mei: list) -> int:
    """外格を計算

    Args:
        sei (list): kakushu_check()で取得した姓の画数
        mei (list): kakushu_check()で取得した名の画数

    Returns:
        _int: 姓の最初と名の最後を合計
    """
    calc_gaikaku: int = sei[0][0] + mei[-1][0]
    return calc_gaikaku


def get_kikkyo(kaku_count: int, result_list: list) -> str:
    """吉凶のテキストを取得

    Args:
        kaku_count (int): 画数
        result_list (list): 結果リスト

    Returns:
        str: 吉凶のテキスト
    """
    kikkyo: str = result_list[kaku_count]["kikkyo"]
    return kikkyo


def get_msg(kaku_count: int, result_list: list):
    """結果のテキストを取得

    Args:
        kaku_count (int): 画数
        result_list (list): 結果リスト

    Returns:
        str: 結果のテキスト
    """
    msg: str = result_list[kaku_count]["message"]
    return msg


def main():
    input_sei: str = "相戸"
    input_mei: str = "ゆづな"

    print(f"あなたの名前は「{input_sei} {input_mei}」ですね。")

    kanji_json_dir: pathlib = pathlib.Path(
        "Z:/マイドライブ/python/junkbox/name-fortune/production/kanji-kakusu.json"
    )
    kana_json_dir: pathlib = pathlib.Path(
        "Z:/マイドライブ/python/junkbox/name-fortune/production/kana-kakusu.json"
    )

    result_json_dir: pathlib = pathlib.Path(
        "Z:/マイドライブ/python/junkbox/name-fortune/production/result-data.json"
    )

    result_kanji_list, result_kakusyu_list, result_json_list = read_json(
        kanji_json_dir, kana_json_dir, result_json_dir
    )

    result_sei, result_mei = kakushu_check(
        input_sei, input_mei, result_kanji_list, result_kakusyu_list
    )

    tenkaku_count: int = calc_tenkaku(result_sei)
    chikaku_count: int = calc_chikaku(result_mei)
    sokaku_count: int = calc_soukaku(tenkaku_count, chikaku_count)
    zinkaku_count: int = calc_zinkaku(result_sei, result_mei)
    gaikaku_count: int = calc_gaikaku(result_sei, result_mei)

    print("\n結果")
    print(
        f"天格（姓）：{tenkaku_count}画・{get_kikkyo(tenkaku_count,result_json_list)}・{get_msg(tenkaku_count,result_json_list)}"
    )

    print(
        f"地格（名）：{chikaku_count}画・{get_kikkyo(chikaku_count,result_json_list)}・{get_msg(chikaku_count,result_json_list)}"
    )
    print(
        f"総格（姓+名）：{sokaku_count}画・{get_kikkyo(sokaku_count,result_json_list)}・{get_msg(sokaku_count,result_json_list)}"
    )
    print(
        f"人格（姓の一番下・名の上）：{zinkaku_count}画・{get_kikkyo(zinkaku_count,result_json_list)}・{get_msg(zinkaku_count,result_json_list)}"
    )
    print(
        f"外格（姓の一番上・名の下）：{gaikaku_count}画・{get_kikkyo(gaikaku_count,result_json_list)}・{get_msg(gaikaku_count,result_json_list)}"
    )


if __name__ == "__main__":
    main()
