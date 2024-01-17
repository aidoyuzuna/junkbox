from io import BytesIO
import openai
import speech_recognition as sr
import setting
import flet as ft

openai.organization = setting.ORGANIZATION
openai.api_key = setting.API_KEY


class Widget:
    def __init__(self,page):
        self.page = page
        self.text_field = ft.TextField(max_lines=10, bgcolor="#333333", label="ここに出力結果がでます", read_only=True,
                                       value="")
        self.button = ft.ElevatedButton(text="録音開始", on_click=self.btn_recording)

    def btn_recording(self, e):
        r = sr.Recognizer()
        with sr.Microphone(sample_rate=16_000) as source:
            audio = r.listen(source)
            audio_data = BytesIO(audio.get_wav_data())
            audio_data.name = "from_mic.wav"
            transcript = openai.Audio.transcribe("whisper-1", audio_data)
            self.text_field.value = transcript["text"]
            self.page.update()


def setapp(page: ft.Page):
    widgets = Widget(page)
    page.title = "録音アプリ"
    page.add(widgets.text_field, widgets.button)


def main():
    ft.app(target=setapp)


if __name__ == "__main__":
    main()
