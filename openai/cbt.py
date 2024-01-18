from io import BytesIO
import openai
import setting
import flet as ft
import string

openai.organization = setting.ORGANIZATION
openai.api_key = setting.API_KEY


class Widget:
    def __init__(self, page):
        self.page = page
        self.text_field = ft.TextField(multiline=True,
                                       min_lines=10, max_lines=10, bgcolor="#333333", label="悩みや相談内容を書いてね",
                                       value="")
        self.button = ft.ElevatedButton(text="相談開始", on_click=self.btn_cbt)
        self.answer_label = ft.Text(value="ChatGPTの回答")
        self.answer = ft.TextField(multiline=True,
                                   min_lines=25, max_lines=25, bgcolor="#333333", label="GPTの回答はここに出力されます",
                                   read_only=True,
                                   value="")

    def btn_cbt(self, e):
        with open("cbt_template.txt", encoding="UTF-8") as f:
            t = string.Template(f.read())

        consult = t.substitute(contents=self.text_field.value)
        print(consult)

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

        print(response.choices[0]["message"]["content"].strip())
        self.answer.value = response.choices[0]["message"]["content"].strip()
        self.page.update()


def setapp(page: ft.Page):
    widgets = Widget(page)
    page.title = "CBTアプリ"
    page.add(widgets.text_field, widgets.button,widgets.answer_label, widgets.answer)


def main():
    ft.app(target=setapp)


if __name__ == "__main__":
    main()
