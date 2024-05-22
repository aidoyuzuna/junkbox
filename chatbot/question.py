import flet as ft
from flet import margin
from openai import OpenAI
import anthropic
import os
from dotenv import load_dotenv
import winsound

load_dotenv()

chatgpt = OpenAI(
    api_key=os.environ.get("OPENAI_KEY")
)
claude = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_KEY")
)


def main(page: ft.Page):
    # 送信ボタンのクリックイベント
    def send_click(e):
        # 回答中の処理を行う
        send_button.disabled = True
        reset_button.disabled = True
        chatgpt_response.value = "回答中"
        claude_response.value = "回答中"
        page.update()

        question = input_box.value

        if model_switcher.value == "品質優先（4o & Opus）":
            print("品質優先で行います")
            chatgpt_model = "gpt-4o"
            claude_model = "claude-3-opus-20240229"

        else:
            print("速度優先で行います")
            chatgpt_model = "gpt-3.5-turbo-0125"
            claude_model = "claude-3-sonnet-20240229"

        chatgpt_message = chatgpt.chat.completions.create(
            model=chatgpt_model,
            max_tokens=1000,
            temperature=0.0,
            messages=[
                {"role": "user", "content": question}
            ]
        )

        claude_message = claude.messages.create(
            model=claude_model,
            max_tokens=1000,
            temperature=0.0,
            messages=[
                {"role": "user", "content": question}
            ]
        )

        chatgpt_response.value = chatgpt_message.choices[0].message.content
        claude_response.value = claude_message.content[0].text
        winsound.PlaySound("fin.wav", winsound.SND_FILENAME)
        send_button.disabled = False
        reset_button.disabled = False
        page.update()

    # リセットボタンのクリックイベント
    def reset_click(e):
        input_box.value = ""
        chatgpt_response.value = ""
        claude_response.value = ""
        input_box.update()
        chatgpt_response.update()
        claude_response.update()

    # ページの設定
    page.title = "調べものアプリ"
    page.window_width = 1200
    page.window_height = 1000

    # 悩み・質問を書くテキストボックス
    input_box = ft.TextField(label="悩み・質問を書く", min_lines=4, multiline=True, width=1010, bgcolor="#333333", )

    # モデル変更機能
    model_switcher = ft.Dropdown(
        width=300,
        value="速度優先（3.5 & Sonnet）",
        label="使用モデル",
        bgcolor="#333333",
        options=[
            ft.dropdown.Option(text="品質優先（4o & Opus）"),
            ft.dropdown.Option(text="速度優先（3.5 & Sonnet）"),
        ],
    )

    # 送信、コピー、リセットボタンの設定
    send_button = ft.ElevatedButton(text="送信", width=300, height=50, bgcolor="#009688", color="#ffffff",
                                    disabled=False, on_click=send_click)
    reset_button = ft.ElevatedButton(text="リセット", height=50, bgcolor="#757575", color="#ffffff",
                                     disabled=False, on_click=reset_click)

    # 回答エリア
    chatgpt_response = ft.TextField(label="ChatGPTの回答", value="", read_only=True, width=500, height=900,
                                    min_lines=27, max_lines=71, bgcolor="#212121", multiline=True)
    claude_response = ft.TextField(label="Claudeの回答", value="", read_only=True, width=500, height=900,
                                   min_lines=27, max_lines=71, bgcolor="#212121", multiline=True)
    # レイアウトの作成
    page.add(
        ft.Container(input_box, margin=margin.only(bottom=10, left=75)),
        ft.Container(
            ft.Row([model_switcher, send_button, reset_button], alignment=ft.MainAxisAlignment.CENTER),
            margin=margin.only(bottom=30)
        ),
        ft.Container(
            ft.Row([chatgpt_response, claude_response], alignment=ft.MainAxisAlignment.CENTER),
        )
    ),


# アプリケーションの開始
ft.app(target=main)

if __name__ == "__main__":
    main()
