import pyperclip
import os
from PIL import Image


# 変換
def image_resize(c_dir, r_jpg, r_png):
    image = Image.open(c_dir).convert('RGB')
    resize_file = image.resize((image.width // 2, image.height // 2))
    resize_file.save(r_jpg, quality=80), resize_file.save(r_png)


# 削除
def image_delete(j_dir, p_dir):
    jpg_file_size = os.path.getsize(j_dir)
    png_file_size = os.path.getsize(p_dir)

    if jpg_file_size < png_file_size:
        os.remove(p_dir)
    else:
        os.remove(j_dir)


def main():
    # ディレクトリー指定
    clip_dir = pyperclip.paste()
    clip_dir = clip_dir.replace(os.path.sep, "/").replace('"', "")
    resize_dir = os.path.dirname("I:/09_ジャンクボックス/099_一時置き場/")
    resize_file_name = os.path.splitext(os.path.basename(clip_dir))[0]

    jpg_dir = os.path.join(resize_dir, resize_file_name) + ".jpg"
    png_dir = os.path.join(resize_dir, resize_file_name) + ".png"

    # 実行
    image_resize(clip_dir, jpg_dir, png_dir)
    image_delete(jpg_dir, png_dir)


main()
