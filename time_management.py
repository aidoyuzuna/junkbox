import time
import flet as ft
from flet import margin, alignment


class Countdown:
    def __init__(self, page, time_left):
        self.is_running = True
        self.time_left = time_left
        self.page = page
        self.time_left_label = ft.Text(elapsed_time_str(self.time_left), size=30)
        self.start_stop_button = ft.ElevatedButton(text="作業開始", width=200, height=50, bgcolor="#03A9F4",
                                                   disabled=False,
                                                   on_click=self.countdown_btn_click)

    def countdown_btn_click(self, e):
        self.start_stop_button.text = "ストップ"
        self.start_stop_button.bgcolor = "#F44336"
        self.start_stop_button.on_click = self.countdown_btn_stop_click
        self.countdown()

    def countdown(self):
        while self.time_left > 0 and self.is_running:
            time.sleep(1)
            self.time_left -= 1
            self.time_left_label.value = elapsed_time_str(self.time_left)
            self.page.update()

    def countdown_btn_stop_click(self, e):
        self.is_running = False


def elapsed_time_str(seconds):
    seconds = int(seconds + 0.5)  # 秒数を四捨五入
    h = seconds // 3600  # 時の取得
    m = (seconds - h * 3600) // 60  # 分の取得
    s = seconds - h * 3600 - m * 60  # 秒の取得

    return f"{h:02}:{m:02}:{s:02}"  # hh:mm:ss形式の文字列で返す


def setapp(page: ft.Page):
    widgets = Countdown(page, 900)
    page.title = "作業用タイマー"
    page.window_width = 400
    page.window_height = 200

    page.add(
        ft.Column([
            ft.Container(widgets.time_left_label, margin=margin.only(top=30)),
            ft.Container(widgets.start_stop_button, margin=margin.only(bottom=20)),
        ],
        ),
    )


def main():
    ft.app(target=setapp)


if __name__ == "__main__":
    main()
