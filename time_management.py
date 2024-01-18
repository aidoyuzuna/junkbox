import time
import flet as ft
from flet import margin, alignment


class Countdown:
    def __init__(self, page, set_time):
        self.set_time = set_time
        self.page = page
        self.count_down_label = ft.Text(elapsed_time_str(self.set_time), size=30)
        self.count_down_button = ft.ElevatedButton(text="作業開始", width=200, height=50, bgcolor="#03A9F4",
                                                   disabled=False,
                                                   on_click=self.countdown_btn_click)

    def countdown_btn_click(self, e):
        stop_flag = False
        self.count_down_button.text = "ストップ"
        self.count_down_button.bgcolor = "#F44336"
        self.count_down_button.on_click = self.countdown_btn_stop_click()

    def countdown(self):
        while self.set_time > 0:
            time.sleep(1)
            self.set_time -= 1
            self.count_down_label.value = elapsed_time_str(self.set_time)
            self.page.update()


def elapsed_time_str(seconds):
    seconds = int(seconds + 0.5)  # 秒数を四捨五入
    h = seconds // 3600  # 時の取得
    m = (seconds - h * 3600) // 60  # 分の取得
    s = seconds - h * 3600 - m * 60  # 秒の取得

    return f"{h:02}:{m:02}:{s:02}"  # hh:mm:ss形式の文字列で返す


def setapp(page: ft.Page):
    widgets = Countdown(page, 900)
    page.title = "作業用タイマー"
    page.window_height = 1350

    page.add(
        ft.Column([
            ft.Container(widgets.count_down_label, margin=margin.only(top=30)),
            ft.Container(widgets.count_down_button, margin=margin.only(bottom=20)),
        ],
        ),
    )
    widgets.countdown()


def main():
    ft.app(target=setapp)


if __name__ == "__main__":
    main()
