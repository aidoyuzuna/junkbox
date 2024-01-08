import pyperclip
import os
from PIL import Image


# 変換
def image_resize(resize_jpg, resize_png):
    image = Image.open(clip_dir).convert('RGB')
    resize_file = image.resize((image.width // 2, image.height // 2))
    resize_file.save(resize_jpg, quality=80), resize_file.save(resize_png)


# 削除
def image_delete(delete_jpg, delete_png):
    if delete_jpg < delete_png:
        os.remove(png_dir)
    else:
        os.remove(jpg_dir)


# ディレクトリー指定
clip_dir = pyperclip.paste()
clip_dir = clip_dir.replace(os.path.sep, "/").replace('"', "")
resize_dir = os.path.dirname("I:/09_ジャンクボックス/099_一時置き場/")
resize_file_name = os.path.splitext(os.path.basename(clip_dir))[0]

jpg_dir = os.path.join(resize_dir, resize_file_name) + ".jpg"
png_dir = os.path.join(resize_dir, resize_file_name) + ".png"

jpg_file_size = os.path.getsize(jpg_dir)
png_file_size = os.path.getsize(png_dir)

# 実行
image_resize(jpg_dir, png_dir)
image_delete(jpg_file_size, png_file_size)
