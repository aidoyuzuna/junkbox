# 種族値クラスの定義、種族値を入れる変数を設定
# todo:とくこう・とくぼうの変数名他にいいのがないか調べる
class BasicStats:
    def __init__(self, hp: int, attack: int, defence: int, spattack: int, spdefence: int, speed: int):
        self.hp = hp
        self.attack = attack
        self.defence = defence
        self.spattack = spattack
        self.spdefence = spdefence
        self.speed = speed


def main():
    # ポケモンの生成
    pikachu = BasicStats(35, 55, 40, 50, 50, 90)
    eevee = BasicStats(55, 55, 50, 45, 65, 55)

    # ポケモンの情報を表示
    # todo:print表記を見やすくする
    print(
        f"ピカチュウ\nHP：{pikachu.hp}\nこうげき：{pikachu.attack}\nぼうぎょ：{pikachu.defence}\nとくこう：{pikachu.spattack}\nとくぼう：{pikachu.spdefence}\nすばやさ：{pikachu.speed}\n")
    print(
        f"イーブイ\nHP：{eevee.hp}\nこうげき：{eevee.attack}\nぼうぎょ：{eevee.defence}\nとくこう：{eevee.spattack}\nとくぼう：{eevee.spdefence}\nすばやさ：{eevee.speed}\n")

    # すばやさの比較をする
    # todo:if文の書き方他にありそうなので調べる
    if pikachu.speed > eevee.speed:
        print("先手はピカチュウ")

    else:
        print("先手はイーブイ")


if __name__ == "__main__":
    main()
