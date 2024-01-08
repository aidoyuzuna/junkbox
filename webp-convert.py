from PIL import Image
import pyperclip
import glob

img_path = pyperclip.paste()
img_list = glob.glob(img_path + "\*.png")
img_list.extend(glob.glob(img_path + "\*.jpg"))
img_list.extend(glob.glob(img_path + "\*.tif"))

for i in img_list:
        imagedata = Image.open(i).convert('RGB')
        imagedata.save(i[:-4] + '.webp','webp', quality=80, method=6)
