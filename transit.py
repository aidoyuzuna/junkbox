import swisseph as swe
import datetime


class Planet:
    def __init__(self):
        self._sign = (
            "牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座",
            "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座")
        self._planet = ""
        self._planet_number = 0

    @property
    def sign(self):
        return self._sign

    @property
    def planet(self):
        return self._planet

    def planet_return(self):
        return self._planet

    def planet_calc(self, now, timezone: int):
        # 日付をUTC・ユリウス暦に変換
        utc = swe.utc_time_zone(now.year, now.month, now.day, now.hour, now.minute, now.second, timezone)
        jul = swe.utc_to_jd(*utc)

        # 惑星の位置計算
        calc = swe.calc(jul[0], self._planet_number)
        return calc

    def decision_sign(self, planet):
        # 星座判定（360度の円を12等分している。1つの星座につき30度）
        idx = int(planet // 30)
        if idx < 0 or idx > 11:
            raise ValueError(f"惑星{planet}は360以下の整数である必要がある: {planet}")  # エラーで原因が分かるようにする
        return self._sign[idx]


class Sun(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "　太陽"
        self._planet_number = 0


class Moon(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "　　月"
        self._planet_number = 1


class Mercury(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "　水星"
        self._planet_number = 2


class Venus(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "　金星"
        self._planet_number = 3


class Mars(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "　火星"
        self._planet_number = 4


class Jupiter(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "　木星"
        self._planet_number = 5


class Saturn(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "　土星"
        self._planet_number = 6


class Uranus(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "天王星"
        self._planet_number = 7


class Neptune(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "海王星"
        self._planet_number = 8


class Pluto(Planet):
    def __init__(self):
        super().__init__()
        self._planet = "冥王星"
        self._planet_number = 9


def return_planet(today, yesterday):
    if today < yesterday:
        return True

    else:
        return False


def main():
    # 今日の日付とタイムゾーン指定
    now_datetime = datetime.datetime.now()
    yesterday_datetime = now_datetime - datetime.timedelta(days=1)
    timezone_offset = 9

    today_planet = [Sun(), Moon(), Mercury(), Venus(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune(), Pluto()]
    yesterday_planet = [Sun(), Moon(), Mercury(), Venus(), Mars(), Jupiter(), Saturn(), Uranus(), Neptune(), Pluto()]
    planet_name = []
    today_transit = []
    yesterday_transit = []
    today_sign = []
    return_flag = []
    result_text = f"【{now_datetime:%Y/%m/%d %H:%M} 現在のトランジット状況】\n"

    for i in range(10):
        today_transit.append(today_planet[i].planet_calc(now_datetime, timezone_offset))
        yesterday_transit.append(
            yesterday_planet[i].planet_calc(yesterday_datetime, timezone_offset))

        planet_name = today_planet[i].planet_return()
        today_sign.append(today_planet[i].decision_sign(today_transit[i][0][0]))
        return_flag.append(return_planet(today_transit[i][0][0], yesterday_transit[i][0][0]))

        if return_flag[i]:
            result_text += f"{planet_name}：{today_sign[i]}{int(today_transit[i][0][0] % 30)}度（逆行中）\n"

        else:
            result_text += f"{planet_name}：{today_sign[i]}{int(today_transit[i][0][0] % 30)}度\n"

    print(result_text)


if __name__ == '__main__':
    main()
