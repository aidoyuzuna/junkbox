import swisseph as swe
import datetime
import math


def calculate_moon_position(date, timezone):
    # 日付をUTC・ユリウス暦に変換
    date_components = [date.year, date.month, date.day, date.hour, date.minute, date.second]
    utc = swe.utc_time_zone(date_components[0], date_components[1], date_components[2], date_components[3],
                            date_components[4], date_components[5], timezone)
    jul = swe.utc_to_jd(utc[0], utc[1], utc[2], utc[3], utc[4], utc[5])

    # 月の位置を計算
    moon_calc = swe.calc(jul[0], 1)
    return moon_calc


def determine_moon_sign(moon):
    # 星座
    sign = ("牡羊座", "牡牛座", "双子座", "蟹座", "獅子座", "乙女座", "天秤座", "蠍座", "射手座", "山羊座", "水瓶座", "魚座")

    # 星座判定（360度の円を12等分している。1つの星座につき30度）
    if 0 < moon < 30:
        print(sign[0])

    elif 31 < moon < 60:
        print(sign[1])

    elif 61 < moon < 90:
        print(sign[2])

    elif 91 < moon < 120:
        print(sign[3])

    elif 121 < moon < 150:
        print(sign[4])

    elif 151 < moon < 180:
        print(sign[5])

    elif 180 < moon < 210:
        print(sign[6])

    elif 211 < moon < 240:
        print(sign[7])

    elif 241 < moon < 270:
        print(sign[8])

    elif 271 < moon < 300:
        print(sign[9])

    elif 301 < moon < 330:
        print(sign[10])

    else:
        print(sign[11])


def check_luna_return(birth_position, today_position):
    if math.isclose(birth_position, today_position, abs_tol=13) and today_position < birth_position:
        print("今日はルナリターン日です")


def main():
    # 日付・タイムゾーン入力
    birthdate = datetime.datetime(1989, 12, 1, 20, 24, 00)
    todaydate = datetime.datetime.now()
    timezone_offset = 9

    # 日付計算
    birth_moon = calculate_moon_position(birthdate, timezone_offset)
    today_moon = calculate_moon_position(todaydate, timezone_offset)

    # ルナリターン判定
    determine_moon_sign(int(birth_moon[0][0]))
    determine_moon_sign(int(today_moon[0][0]))
    check_luna_return(birth_moon[0][0], today_moon[0][0])


if __name__ == '__main__':
    main()
