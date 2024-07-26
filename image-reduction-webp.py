from pathlib import Path
import sys
from PIL import Image


def get_image_list(input_list: Path) -> list[Path]:
    """画像のファイル一覧を取得する

    :param input_list: Downloadsフォルダー
    :return: .jpg,.pngファイル一覧のPathリスト
    """

    # 画像ファイル（jpg・png）検索
    extension = ['.jpg', '.png']
    image_list = [i for i in Path(input_list).glob('**/*.*') if i.suffix in extension]

    # jpg・png画像がない場合のエラー処理
    if not image_list:
        print("エラー！Downloadsフォルダーにjpg・pngファイルがありません")
        sys.exit(1)

    return image_list


def convert_image(convert_list: list[Path], save_path: Path):
    """画像を50％に縮小・webpに変換

    :param convert_list:get_image_listで取得した変換画像リスト
    :param save_path: Desktopフォルダー
    :return: none
    """

    for i in convert_list:
        save_file_path = save_path.joinpath(Path(i.stem))
        image = Image.open(i).convert('RGB')
        resize_file = image.resize((image.width * 0.4, image.height * 0.4))
        resize_file.save(save_file_path.with_suffix('.webp'), "webp", quality=80, method=6)


def main():
    import_dir = Path.expanduser(Path('~/Downloads'))
    export_dir = Path.expanduser(Path('~/Onedrive/デスクトップ'))

    convert_image(get_image_list(import_dir), export_dir)


if __name__ == "__main__":
    main()
