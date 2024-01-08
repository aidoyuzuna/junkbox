import pyperclip
import os
from PIL import Image

# ディレクトリ指定
clip_dir = pyperclip.paste()
clip_dir = clip_dir.replace(os.path.sep,"/").replace('"', "")
resize_dir = os.path.dirname("I:/09_ジャンクボックス/099_一時置き場/")
resize_file_name = os.path.splitext(os.path.basename(clip_dir))[0]
jpg_dir = os.path.join(resize_dir,resize_file_name)+".jpg"
png_dir = os.path.join(resize_dir,resize_file_name)+".png"

# 変換
image = Image.open(clip_dir).convert('RGB')
resize_file = image.resize((image.width // 2, image.height // 2))
resize_file.save(jpg_dir, quality=80)
resize_file.save(png_dir)

# 削除
jpg_file_size = os.path.getsize(jpg_dir)
png_file_size = os.path.getsize(png_dir)

if jpg_file_size < png_file_size:
    os.remove(png_dir)
else:
    os.remove(jpg_dir)