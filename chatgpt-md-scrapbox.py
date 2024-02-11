import webbrowser
import os
import re
import sys


def markdown_check(root_dir):
    for file_base in os.listdir(root_dir):
        ext = os.path.basename(file_base)
        if ext == "ChatGPT-.md":
            full_path = os.path.join(root_dir, file_base)
            return full_path

        # sys.exit("該当ファイルがないので終了します")


def markdown_replace(md_dir):
    result_text = ""
    with open(md_dir, encoding="UTF-8") as f:
        lines = f.readlines()
        for line in lines:
            # 強調解除
            line = line.replace("**", "")

            # ユーザーのコード処理変換
            line = line.replace("\`\`\`", "`")

            # 見出し
            if re.match(r'## ', line):
                line = line.replace("##", "[**") + "**]"
            line = line.__add__("%0A")

            # コードブロック（ここがわからん）
            if re.search("```python", line):
                for code in range(2):
                    line = line.replace("```python", "code:python")
                    line = line.rjust(len(line) + 1)
                    line = line.replace("```", "")

            # 文章
            result_text += line
        f.close()
        return result_text
        # os.remove(md_dir)


def chrome_start(text):
    url = f"https://scrapbox.io/saro-chatgpt/new?body={text}"
    browser = webbrowser.get("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
    browser.open(url)


def main():
    root = f"D:\\Download"
    md_path = markdown_check(root)
    result = markdown_replace(md_path)
    print(result)
    # chrome_start(result_path)


if __name__ == "__main__":
    main()
