import openai
import setting
import flet as ft
from flet import margin, alignment
import string
import pyperclip

openai.organization = setting.ORGANIZATION
openai.api_key = setting.API_KEY


class Widget:
    def __init__(self, page):
        self.page = page
        self.consult_label = ft.Text("相談内容", size=30)
        self.text_field = ft.TextField(multiline=True,
                                       min_lines=7, max_lines=7, bgcolor="#333333",
                                       label="悩みや相談内容を書いてね",
                                       value="")
        self.cbt_button = ft.ElevatedButton(text="相談開始", width=500, height=75, bgcolor="#03A9F4",
                                            disabled=False,
                                            on_click=self.cbt_button_click)
        self.answer_label = ft.Text("相談結果", size=30)
        self.answer = ft.TextField(multiline=True,
                                   min_lines=25, max_lines=25, bgcolor="#333333",
                                   label="ChatGPTの返答はここにでるよ",
                                   read_only=True,
                                   value="")
        self.copy_button = ft.ElevatedButton(text="相談内容と結果をコピー", width=500, height=75, bgcolor="#03A9F4",
                                             disabled=True,
                                             on_click=self.copy_button_click)

    def cbt_button_click(self, e):
        self.cbt_button.disabled = True
        self.page.update()
        with open("cbt_template.txt", encoding="UTF-8") as f:
            t = string.Template(f.read())

        consult = t.substitute(contents=self.text_field.value)

        message = [
            {"role": "user", "content": consult},
        ]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            # model="gpt-4",
            messages=message,
            n=1,
            stop=None,
            temperature=0.7,
            top_p=1,
        )

        self.answer.value = response.choices[0]["message"]["content"].strip()
        self.cbt_button.disabled = False
        self.copy_button.disabled = False
        self.page.update()

    def copy_button_click(self, e):
        with open("cbt_copy_template.txt", encoding="UTF-8") as w:
            open_text = string.Template(w.read())
            copy_text = open_text.substitute(contents=self.text_field.value, result=self.answer.value)
            pyperclip.copy(copy_text)


def setapp(page: ft.Page):
    widgets = Widget(page)
    page.title = "CBTアプリ"
    page.window_height = 1350

    page.add(
        ft.Column([
            ft.Container(widgets.consult_label, margin=margin.only(top=30)),
            ft.Container(widgets.text_field, margin=margin.only(bottom=20)),
            ft.Container(widgets.cbt_button, alignment=alignment.center),
            ft.Container(widgets.answer_label, margin=margin.only(top=50)),
            ft.Container(widgets.answer),
            ft.Container(widgets.copy_button, alignment=alignment.center),
        ],
        ),
    )


def main():
    ft.app(target=setapp)


if __name__ == "__main__":
    main()
