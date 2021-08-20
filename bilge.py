import speech_recognition as sr
import pyaudio
from gtts import gTTS
import os
from io import BytesIO
import pygame
from time import sleep
import pyglet
import translation


def recognize_speech(audio):
    return r.recognize_google(audio, language='tr-TR')

def assistant_speak(text, lang):
    tts = gTTS(text=text, lang = lang)
    filename = 'temp.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    sleep(music.duration)
    os.remove(filename)

r = sr.Recognizer()

mic = sr.Microphone(device_index=1)
is_awaken=False
while True:
    
    with mic as source:
        audio = r.listen(source)

    detected_speech = recognize_speech(audio)
    if detected_speech.lower() == "hey bilge":
        assistant_speak("Buyrun benim adım bilge","tr")
        is_awaken=True
        break
        
if is_awaken:
    while True:
        
        with mic as source:
            audio = r.listen(source)
        intent = recognize_speech(audio)
        
        if intent.lower() == "çeviri yapmanı istiyorum":
            assistant_speak("Hangi dile çevireyim","tr")
            
            with mic as source:
                audio = r.listen(source)
            translate_target = recognize_speech(audio)
            print(translate_target)
            assistant_speak("Çevirmemi istediğiniz cümleyi söyleyin","tr")
            with mic as source:
                audio = r.listen(source)
            translate_this = recognize_speech(audio)
            
            translated_text = translation.translate(translate_this, translate_target)
            if translated_text!="Bu dil desteklenmiyor":
                assistant_speak(translated_text,translation.supported_langs[translate_target])
            else:
                assistant_speak("Bu dil desteklenmiyor","tr")