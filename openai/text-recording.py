from io import BytesIO
import openai
import speech_recognition as sr
import setting
import flet as ft

openai.organization = setting.ORGANIZATION
openai.api_key = setting.API_KEY


def setapp(page: ft.Page):
    def btn_recording(e):
        r = sr.Recognizer()
        with sr.Microphone(sample_rate=16_000) as source:
            audio = r.listen(source)
            audio_data = BytesIO(audio.get_wav_data())
            audio_data.name = "from_mic.wav"
            transcript = openai.Audio.transcribe("whisper-1", audio_data)
            page.update()

    recoding_text = ""
    page.title = "録音アプリ"
    page.add(
        ft.TextField(max_lines=10, bgcolor="#333333", label="ここに出力結果がでます", read_only=True,
                     value=recoding_text),
        ft.ElevatedButton(text="録音開始", on_click=btn_recording))


def main():
    ft.app(target=setapp)


if __name__ == "__main__":
    main()
