# 要望
class Suggestion:
    def __init__(self, body: str):
        self.body = body


# 目安箱
class SuggestionBox:
    def __init__(self):
        ...

    def __len__(self) -> int:

    # 入っている数を返す

    def post(self, suggestion: Suggestion):

    # 要望を箱に入れる

    def take_out(self) -> Suggestion:
# 入っている要望をひとつ取り出す(なければエラー or None(どちらかで実装))

def main():
    

if __name__ == '__main__':
    main()