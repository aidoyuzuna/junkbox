import pyperclip
import os
from PIL import Image

clip_dir = pyperclip.paste()
resize_dir = "I://09_ジャンクボックス//099_一時置き場"
print(clip_dir)
image_dir = clip_dir.replace(os.path.sep,"/")
print(image_dir)

image = Image.open(image_dir)
resize_file = image.resize(image,None, None, 0.5, 0.5)
resize_file.save(resize_dir)