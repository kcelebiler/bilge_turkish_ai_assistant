import speech_recognition as sr
from gtts import gTTS
import os
from time import sleep
import pyglet

import translation
import get_weather
import get_currency
import play_video
import get_cryptocurrency
import send_email
import get_news

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
    
    if not is_awaken:
        with mic as source:
            audio = r.listen(source)
            detected_speech = recognize_speech(audio)
            print(detected_speech)
            if not is_awaken:
                if "hey bilge" in detected_speech.lower() or "hey biye"  in detected_speech.lower() or "hey bege"  in detected_speech.lower() or "hey binge"  in detected_speech.lower() or "hey bg"  in detected_speech.lower() or "heybe yenge"  in detected_speech.lower() or "hey bilgi"  in detected_speech.lower() or "hey bilye" in detected_speech.lower():
                    is_awaken = True
                    assistant_speak("Buyrun benim adım bilge","tr")
            
            
    if is_awaken:
        with mic as source:
            audio = r.listen(source)
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
            
        elif intent.lower() == "kripto fiyatlarını öğrenmek istiyorum" or intent.lower() == "kripto fiyatını öğrenmek istiyorum":
            
            assistant_speak("Lütfen istediğiniz kriptoyu ve dövizi söyleyin","tr")
            
            with mic as source:
                audio = r.listen(source)
            crytocurrencies = recognize_speech(audio)
            
            source, target = crytocurrencies.split(" ve ")[0].lower(), crytocurrencies.split(" ve ")[1].lower()
            
            crypto_price = get_cryptocurrency.get_cryptocurrency(source, target)
            
            speak_crypto = "bir " + source + " " + str(crypto_price) + " " + target +" etmektedir"
            
            assistant_speak(speak_crypto,"tr")
            
        elif intent.lower() == "mail göndermek istiyorum" or intent.lower() == "mail atar mısın" or intent.lower() == "email atar mısın" or intent.lower() == "mail atarmısın" or intent.lower() == "email atarmısın"  or intent.lower() == "mail atmak istiyorum" or intent.lower() == "email atmak istiyorum" or intent.lower() == "email göndermek istiyorum" or intent.lower() == "mail gönderir misin" or intent.lower() == "mail gönderirmisin" or intent.lower() == "email gönderir misin" or intent.lower() == "email gönderirmisin":
            
            assistant_speak("Hangi adrese email göndermek istiyorsun","tr")
            
            with mic as source:
                audio = r.listen(source)
            target = recognize_speech(audio)
            
            target = target.replace(" alt tire ","_")
            target = target.replace(" et ","@")
            target = target.lower()
            target = target.replace("ç","c")
            target = target.replace("ş","s")
            target = target.replace("ö","o")
            target = target.replace("ü","u")
            target = target.replace("ı","i")
            target = target.replace(" ","")
            
            assistant_speak("Lütfen mesajınızı söyleyin","tr")
            
            with mic as source:
                audio = r.listen(source)
            message = recognize_speech(audio)
            
            cancelled = False
            
            if message.lower() == "iptal et" or message.lower() == "vazgeçtim":
                assistant_speak("Email gönderme işlemi iptal edildi","tr")
                cancelled = True
                
            elif send_email.send_email(target, message) and not cancelled:
                assistant_speak("Email başarıyla gönderildi","tr")
                
            elif not send_email.send_email(target, message) and not cancelled:
                assistant_speak("Bir hata meydana geldi. Lütfen tekrar deneyin.","tr")
                
        elif intent.lower() == "haberleri okur musun" or intent.lower() == "haberleri okumanı istiyorum" or intent.lower() == "haberleri oku" or intent.lower() == "haber oku":
            assistant_speak("Hangi kategoriden haber okumamı istersin","tr")
            
            with mic as source:
                audio = r.listen(source)
            category = recognize_speech(audio)
            
            if category.lower() == "hangi kategoriler var" or category.lower() == "hangi kategoriden okuyabilirsin":
                assistant_speak("Spor.....Son Dakika....Magazin.....Ekonomi.....Sağlık.....Dünya.....Politika.....Otomobil.....Teknoloji","tr")
                with mic as source:
                    audio = r.listen(source)
                category = recognize_speech(audio)
                
            if "spor" in category.lower() or "son dakika" in category.lower() or "magazin" in category.lower() or "ekonomi" in category.lower() or "sağlık" in category.lower() or "dünya" in category.lower() or "politika" in category.lower() or "otomobil" in category.lower() or "teknoloji" in category.lower():
                
                try: 
                    title, detail = get_news.get_news(category.lower())
                    
                    assistant_speak(title,"tr")
                    
                    assistant_speak("Detayını okumamı ister misin","tr")
                    
                    with mic as source:
                        audio = r.listen(source)
                    answer = recognize_speech(audio)
                    
                    if answer.lower() == "evet":
                        
                        assistant_speak(detail,"tr")
                        
                    elif answer.lower() == "hayır":
                        
                        assistant_speak("Tamam kapatıyorum","tr")
                        
                except:
                    
                    assistant_speak("Bir hata meydana geldi. Lütfen tekrar deneyin","tr")
                    
                    