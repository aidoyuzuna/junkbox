import pathlib
import pandas


def print_dbg(msg):
    """プリントデバッグ用

    Args:
        msg (_type_): デバッグしたい関数名
    """

    print(msg)
    print(type(msg))


def read_csv(dir: pathlib):
    """文字と画数が入ったCSVファイルを読み込む

    Args:
        dir (pathlib): CSVのパス

    Returns:
        list: 文字カラムのデータ
        list: 画数カラムのデータ
    """
    print("画数csvファイルを読み込みます。少々お待ちください。")

    try:
        csv_data: list = pandas.read_csv(dir, encoding="utf-8")

    except FileNotFoundError as e:
        print(
            "エラー！画数csvが見つかりませんでした。パスとファイル名を確認してください。"
        )
        raise

    moji_column = csv_data.loc[:, "moji"]
    kakusu_column = csv_data.loc[:, "kakusu"]
    return moji_column, kakusu_column


def kakushu_check(sei: str, mei: str, moji_list: list, kakusu_list: list) -> list:
    """画数をチェックする

    Args:
        sei (str): 画数を知りたい姓
        mei (str): 画数を知りたい名
        moji_list (list): read_csvで取得した文字カラムデータ
        kakusu_list (list): read_csvで取得した画数カラムデータ

    Raises:
        ValueError: 文字カラムデータの中に該当する文字がなかった場合（姓）
        ValueError: 文字カラムデータの中に該当する文字がなかった場合（名）

    Returns:
        list: 姓の画数データ
        list: 名の画数データ
    """
    result_sei = []
    result_mei = []

    # 画数の取得
    print("画数を取得しています。")

    try:
        for a in range(len(sei)):
            found = False
            for i in range(len(moji_list)):
                if sei[a] == moji_list[i]:
                    result_sei.append(kakusu_list[i])
                    found = True
            if not found:
                raise ValueError(f"姓の文字「{sei[a]}」が見つかりませんでした。")

        for a in range(len(mei)):
            found = False
            for i in range(len(moji_list)):
                if mei[a] == moji_list[i]:
                    result_mei.append(kakusu_list[i])
                    found = True
            if not found:
                raise ValueError(f"名の文字「{mei[a]}」が見つかりませんでした。")

    except ValueError as e:
        raise

    return result_sei, result_mei


def calc_kakusu(sei: list, mei: list):
    """画数を計算

    Args:
        sei (list): kakushu_check()で取得した姓の画数
        mei (list): kakushu_check()で取得した名の画数

    Returns:
        numpy.int64: 画数の合計
    """
    calc_sei = 0
    calc_mei = 0

    for a in range(len(sei)):
        calc_sei += sei[a]

    for a in range(len(mei)):
        calc_mei += mei[a]

    return calc_sei, calc_mei


def main():
    input_sei = "中川"
    input_mei = "しょうこ"

    print(f"あなたの名前は「{input_sei} {input_mei}」ですね。")

    dir_csv = pathlib.Path("D:/Git/name-fortune/production/kanji-kakusu.csv")
    # dir_csv = pathlib.Path("D:/kanji-kakusu.csv")

    result_moji_list, result_kakusyu_list = read_csv(dir_csv)

    result_sei, result_mei = kakushu_check(
        input_sei, input_mei, result_moji_list, result_kakusyu_list
    )
    calc_sei, calc_mei = calc_kakusu(result_sei, result_mei)

    print(f"　姓：{calc_sei}\n　名：{calc_mei}\n合計：{calc_sei+calc_mei}")


if __name__ == "__main__":
    main()
