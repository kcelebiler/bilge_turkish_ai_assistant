import speech_recognition as sr
import pyaudio
from gtts import gTTS
import os
from io import BytesIO
import pygame
from time import sleep
import pyglet

def recognize_wakeword(audio):
    
    return r.recognize_google(audio, language='tr-TR')

def assistant_speak():
    tts = gTTS(text='Buyrun benim adım bilge...', lang='tr')
        
    filename = 'temp.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    sleep(music.duration)
    os.remove(filename)

r = sr.Recognizer()

mic = sr.Microphone(device_index=1)

while True:
    
    with mic as source:
        audio = r.listen(source)

    detected_speech = recognize_wakeword(audio)
    if detected_speech.lower() == "hey bilge":
        assistant_speak()
        break
        