#server.py

from flask import Flask, render_template, request
from gtts import gTTS
import pygame
from io import BytesIO
import speech_recognition as sr


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('text.html')

@app.route('/tts')
def tts():
    return render_template('texttospeech.html')

@app.route('/stt')
def stt():
    return render_template('speechtotext.html')


@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']

    if text.lower() == 'exit':
        return "Exiting the program."

    language = 'en'
    tts = gTTS(text=text, lang=language, slow=False)

    audio_data = BytesIO()
    tts.write_to_fp(audio_data)
    audio_data.seek(0)

    pygame.mixer.init()
    pygame.mixer.music.load(audio_data)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

    pygame.mixer.quit()

    return render_template('texttospeech.html')


#@app.route('/sl', methods=['GET'])



if __name__=='__main__':
    app.run(debug=True)
