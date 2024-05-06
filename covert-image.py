from pathlib import Path
from PIL import Image


def find_image(search: Path):
    convert_list = list(search.glob("*.png"))
    print(f"リサイズするファイルの数は：{str(len(convert_list))}枚です。")
    print("リサイズを開始します。")
    print("-------------------------------")
    return convert_list


def convert_files(img_list: list[Path], save_dir: Path):
    i = 0
    for i, f in enumerate(img_list, 1):
        img = Image.open(f)
        img_resize = img.resize((img.width // 2, img.height // 2))
        img_resize.save(str(save_dir / f"{f.stem}_half{f.suffix}"))
        print(f"現在：{i}/{len(img_list)}番目の画像を処理しました")

    print(f"合計：{i}枚のファイルを処理しました")
    print("-------------------------------")
    print("リサイズを終了します。")


def main():
    dst_dir = Path('./output')
    search_dir = Path('./')
    print(dst_dir.is_dir())

    # 画像リストの取得
    img_list = find_image(search_dir)

    # 画像処理
    convert_files(img_list, dst_dir)


if __name__ == '__main__':
    main()
