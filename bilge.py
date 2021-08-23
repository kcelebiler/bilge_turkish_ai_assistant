import speech_recognition as sr
from gtts import gTTS
import os
from time import sleep
import pyglet
import translation
import get_weather
import get_currency
import play_video

def recognize_speech(audio):
    try:
        return r.recognize_google(audio, language='tr-TR')
    except:
        return ""
    
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
    
    print(recognize_speech(audio))
    if not is_awaken:
        detected_speech = recognize_speech(audio)
        if detected_speech.lower() == "hey bilge" or detected_speech.lower() == "hey biye" or detected_speech.lower() == "hey bege" or detected_speech.lower() == "hey binge" or detected_speech.lower() == "hey bg" or detected_speech.lower() == "heybe yenge" or detected_speech.lower() == "hey bilgi" or detected_speech.lower() == "hey bilye":
            print(detected_speech)
            assistant_speak("Buyrun benim adım bilge","tr")
            is_awaken=True
            
    elif is_awaken:
        intent = recognize_speech(audio)
        
        print(intent)
        
        if intent.lower() == "tamam kapat" or intent.lower() == "kapat" or intent.lower() == "sus" or intent.lower() == "sus artık" or  intent.lower() == "vazgeçtim":
            assistant_speak("Tamam anladım susuyorum","tr")
            is_awaken = False
        
        elif intent.lower() == "çeviri yapmanı istiyorum":
            assistant_speak("Hangi dile çevireyim","tr")
            
            with mic as source:
                audio = r.listen(source)
            translate_target = recognize_speech(audio)
            
            assistant_speak("Çevirmemi istediğiniz cümleyi söyleyin","tr")
            with mic as source:
                audio = r.listen(source)
            translate_this = recognize_speech(audio)
            
            translated_text = translation.translate(translate_this, translate_target)
            if translated_text!="Bu dil desteklenmiyor":
                assistant_speak(translated_text,translation.supported_langs[translate_target])
            else:
                assistant_speak("Bu dil desteklenmiyor","tr")
        
        elif intent.lower() == "hava durumunu söyler misin" or intent.lower() == "hava durumunu öğrenmek istiyorum":
            assistant_speak("Hangi şehrin hava durumunu öğrenmek istiyorsun","tr")
            
            with mic as source:
                audio = r.listen(source)
            city = recognize_speech(audio)
            
            temperature, humidity, description = get_weather.get_weather(city)
            
            #translated_description = translation.translate(description, "Türkçe")
            
            speak_weather = city + " şehrinin havası "+ description +", hava sıcaklığı "+ str(temperature)+ "derece ve nem oranı yüzde "+ str(humidity)
            
            assistant_speak(speak_weather,"tr")
            
        elif intent.lower() == "döviz fiyatı öğrenmek istiyorum" or intent.lower() == "döviz fiyatını öğrenmek istiyorum" or intent.lower() == "döviz kuru öğrenmek istiyorum" or intent.lower() == "döviz kurunu öğrenmek istiyorum":
            
            assistant_speak("Lütfen çevirmek istediğiniz döviz isimlerini söyleyin","tr")
            
            # dolar ve euro dediğiniz zaman source olarak doları ve target olarak euroyu alacaktır
            with mic as source:
                audio = r.listen(source)
            exchanges = recognize_speech(audio)
            
            source, target = exchanges.split(" ve ")[0].lower(), exchanges.split(" ve ")[1].lower()
            
            if get_currency.get_currency(source, target) == "Bu birim desteklenmiyor":
                
                assistant_speak("Bu birim desteklenmiyor","tr")
                
            elif get_currency.get_currency(source, target) == "Hala para birimlerini almaya çalışıyorum. Lütfen daha sonra tekrar deneyin.":
                
                assistant_speak("Hala para birimlerini almaya çalışıyorum. Lütfen daha sonra tekrar deneyin.","tr")
            
            else:
                try:
                    exchange_rate = round(get_currency.get_currency(source, target),2)
                    
                    speak_exchange = "bir " + source + " " +str(exchange_rate) + " " + target +" etmektedir"
                    
                    assistant_speak(speak_exchange,"tr")
                except:
                    
                    assistant_speak("Bir hata meydana geldi. Lütfen tekrar deneyin","tr")
        
        elif intent.lower() == "video açmanı istiyorum" or intent.lower() == "video oynatmanı istiyorum" or intent.lower() == "bir video oynatmanı istiyorum" or intent.lower() == "bir video açmanı istiyorum":
            
            assistant_speak("Hangi videoyu açayım","tr")
            
            with mic as source:
                audio = r.listen(source)
            keyword = recognize_speech(audio)
            
            assistant_speak("Videoyu açıyorum. Biraz bekleyin.","tr")
            
            play_video.play_video(keyword)