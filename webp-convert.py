from PIL import Image
import pyperclip
import os
import glob


# WebPコンバート
def webp_convert(i_dir, c_list):
    # 画像ファイル以外のものを検知
    for w in c_list:
        if w.endswith(".jpg") or w.endswith(".png"):
            img_data = Image.open(w).convert('RGB')
            full_path = os.path.join(i_dir, os.path.splitext(os.path.basename(w))[0])
            img_data.save(full_path + ".webp", 'webp', quality=80, method=6)
        else:
            print(f"画像ファイル以外のものが検出されました：{os.path.basename(w)}")
            continue


# 実行
def main():
    # ディレクトリ指定
    img_dir = pyperclip.paste()
    img_dir = img_dir.replace('"', "")
    img_list = glob.glob(img_dir + "/*")

    webp_convert(img_dir, img_list)


main()
