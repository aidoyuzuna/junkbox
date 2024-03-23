# 要望
class Suggestion:
    def __init__(self, body: str):
        self.body = body


# 目安箱
class SuggestionBox:
    def __init__(self):
        self.box = []

    def __len__(self) -> int:
        return len(self.box)

    def post(self, suggestion: Suggestion):
        self.box.append(suggestion)

    def take_out(self) -> Suggestion:
        return self.box.pop(0)


def main():
    box = SuggestionBox()
    print(len(box))
    sug1 = Suggestion("アップルパイをメニューに入れて")
    box.post(sug1)

    sug2 = Suggestion("ゴミ箱からゴミがあふれてる")
    box.post(sug2)
    sug1_out = box.take_out()
    print(sug1_out.body)  # Call me

    sug3 = Suggestion("体育館にあるネットがボロボロだから直して")
    box.post(sug3)
    print(len(box))  # 2

    sug2_out = box.take_out()
    print(sug2_out.body)  # Buy it
    sug3_out = box.take_out()
    print(sug3_out.body)  # Marry me
    print(len(box))  # 0


if __name__ == '__main__':
    main()
