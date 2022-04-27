import json
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import core
import sys
# Falar
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty(  # Substituir por o nome do arquivo de voz
    'voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_PT-BR_MARIA_11.0')


def speak(text):
    engine.say(text)
    engine.runAndWait()


# reconhecimento de fala
model = Model('model')
rec = KaldiRecognizer(model, 16000)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1,
                rate=16000, input=True, frames_per_buffer=8000)
stream.start_stream()
# loop do reconhecimento de fala
while True:
    data = stream.read(8192, exception_on_overflow=False)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        result = json.loads(result)

        if result is not None:
            text = result['text']

            print(text)
            speak(text)

            if text == 'que horas são:' or text == 'me diga as horas' or text == 'horas' or text == 'horario' or text == 'hora':
                speak(core.SystemInfo.get_time())
            if text == 'pare':
                sys.exit()
