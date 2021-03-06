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
import get_direction
import open_movie_tvshow
import make_joke

def recognize_speech(audio):

    """
    returns the spoken words, sentences as string

    Args:
        audio (speech_recognition object): recorded audio that speech_recognition creates

    Returns:
        string: if there is a recognized speech it returns that, otherwise returns empty
    """

    try:
        return r.recognize_google(audio, language='tr-TR')
    except:
        return ""
    
def assistant_speak(text, lang):

    """
    creates an mp3 file using the google service
    and plays this mp3 file using pyglet library

    Args:
        text (string): text that assistant will say
        lang (string): specified language abbreviation e.g. tr, en, fr, de

    Returns: 
        none
    """

    tts = gTTS(text=text, lang = lang)
    filename = 'temp.mp3'
    tts.save(filename)
    music = pyglet.media.load(filename, streaming=False)
    music.play()
    sleep(music.duration)
    os.remove(filename)

r = sr.Recognizer()

mic = sr.Microphone(device_index=2)

is_awaken = False

while True:
    
    if not is_awaken:
        with mic as source:
            audio = r.listen(source)
            detected_speech = recognize_speech(audio)
            print(detected_speech)
            if not is_awaken:
                if "hey bilge" in detected_speech.lower() or "hbg" in detected_speech.lower() or "hey bence" in detected_speech.lower() or "hey bilde" in detected_speech.lower() or "hey biye"  in detected_speech.lower() or "hey bege"  in detected_speech.lower() or "hey binge"  in detected_speech.lower() or "hey bg"  in detected_speech.lower() or "heybe yenge"  in detected_speech.lower() or "hey bilgi"  in detected_speech.lower() or "hey bilye" in detected_speech.lower():
                    is_awaken = True
                    assistant_speak("Buyrun benim ad??m bilge","tr")
            
            
    if is_awaken:
        with mic as source:
            audio = r.listen(source)
        intent = recognize_speech(audio)
        
        print(intent)
        
        if intent.lower() == "tamam kapat" or intent.lower() == "kapat" or intent.lower() == "sus" or intent.lower() == "sus art??k" or  intent.lower() == "vazge??tim":
            assistant_speak("Tamam anlad??m susuyorum","tr")
            is_awaken = False
        
        elif intent.lower() == "??eviri yapman?? istiyorum":
            assistant_speak("Hangi dile ??evireyim","tr")
            
            with mic as source:
                audio = r.listen(source)
            translate_target = recognize_speech(audio)
            
            assistant_speak("??evirmemi istedi??iniz c??mleyi s??yleyin","tr")
            with mic as source:
                audio = r.listen(source)
            translate_this = recognize_speech(audio)
            
            translated_text = translation.translate(translate_this, translate_target)
            if translated_text!="Bu dil desteklenmiyor":
                assistant_speak(translated_text,translation.supported_langs[translate_target])
            else:
                assistant_speak("Bu dil desteklenmiyor","tr")
        
        elif intent.lower() == "hava durumunu s??yler misin" or intent.lower() == "hava durumunu ????renmek istiyorum":
            assistant_speak("Hangi ??ehrin hava durumunu ????renmek istiyorsun","tr")
            
            with mic as source:
                audio = r.listen(source)
            city = recognize_speech(audio)
            
            temperature, humidity, description = get_weather.get_weather(city)
            
            #translated_description = translation.translate(description, "T??rk??e")
            
            speak_weather = city + " ??ehrinin havas?? "+ description +", hava s??cakl?????? "+ str(temperature)+ "derece ve nem oran?? y??zde "+ str(humidity)
            
            assistant_speak(speak_weather,"tr")
            
        elif intent.lower() == "d??viz fiyat?? ????renmek istiyorum" or intent.lower() == "d??viz fiyat??n?? ????renmek istiyorum" or intent.lower() == "d??viz kuru ????renmek istiyorum" or intent.lower() == "d??viz kurunu ????renmek istiyorum":
            
            assistant_speak("L??tfen ??evirmek istedi??iniz d??viz isimlerini s??yleyin","tr")
            
            # dolar ve euro dedi??iniz zaman source olarak dolar?? ve target olarak euroyu alacakt??r
            with mic as source:
                audio = r.listen(source)
            exchanges = recognize_speech(audio)
            
            source, target = exchanges.split(" ve ")[0].lower(), exchanges.split(" ve ")[1].lower()
            
            if get_currency.get_currency(source, target) == "Bu birim desteklenmiyor":
                
                assistant_speak("Bu birim desteklenmiyor","tr")
                
            elif get_currency.get_currency(source, target) == "Hala para birimlerini almaya ??al??????yorum. L??tfen daha sonra tekrar deneyin.":
                
                assistant_speak("Hala para birimlerini almaya ??al??????yorum. L??tfen daha sonra tekrar deneyin.","tr")
            
            else:
                try:
                    exchange_rate = round(get_currency.get_currency(source, target),2)
                    
                    speak_exchange = "bir " + source + " " +str(exchange_rate) + " " + target +" etmektedir"
                    
                    assistant_speak(speak_exchange,"tr")
                except:
                    
                    assistant_speak("Bir hata meydana geldi. L??tfen tekrar deneyin","tr")
        
        elif intent.lower() == "video a??man?? istiyorum" or intent.lower() == "video oynatman?? istiyorum" or intent.lower() == "bir video oynatman?? istiyorum" or intent.lower() == "bir video a??man?? istiyorum":
            
            assistant_speak("Hangi videoyu a??ay??m","tr")
            
            with mic as source:
                audio = r.listen(source)
            keyword = recognize_speech(audio)
            
            assistant_speak("Videoyu a????yorum. Biraz bekleyin.","tr")
            
            play_video.play_video(keyword)
            
        elif intent.lower() == "kripto fiyatlar??n?? ????renmek istiyorum" or intent.lower() == "kripto fiyat??n?? ????renmek istiyorum":
            
            assistant_speak("L??tfen istedi??iniz kriptoyu ve d??vizi s??yleyin","tr")
            
            with mic as source:
                audio = r.listen(source)
            crytocurrencies = recognize_speech(audio)
            
            source, target = crytocurrencies.split(" ve ")[0].lower(), crytocurrencies.split(" ve ")[1].lower()
            
            crypto_price = get_cryptocurrency.get_cryptocurrency(source, target)
            
            speak_crypto = "bir " + source + " " + str(crypto_price) + " " + target +" etmektedir"
            
            assistant_speak(speak_crypto,"tr")
            
        elif intent.lower() == "mail g??ndermek istiyorum" or intent.lower() == "mail atar m??s??n" or intent.lower() == "email atar m??s??n" or intent.lower() == "mail atarm??s??n" or intent.lower() == "email atarm??s??n"  or intent.lower() == "mail atmak istiyorum" or intent.lower() == "email atmak istiyorum" or intent.lower() == "email g??ndermek istiyorum" or intent.lower() == "mail g??nderir misin" or intent.lower() == "mail g??nderirmisin" or intent.lower() == "email g??nderir misin" or intent.lower() == "email g??nderirmisin":
            
            assistant_speak("Hangi adrese email g??ndermek istiyorsun","tr")
            
            with mic as source:
                audio = r.listen(source)
            target = recognize_speech(audio)
            
            target = target.replace(" alt tire ","_")
            target = target.replace(" et ","@")
            target = target.lower()
            target = target.replace("??","c")
            target = target.replace("??","s")
            target = target.replace("??","o")
            target = target.replace("??","u")
            target = target.replace("??","i")
            target = target.replace(" ","")
            
            assistant_speak("L??tfen mesaj??n??z?? s??yleyin","tr")
            
            with mic as source:
                audio = r.listen(source)
            message = recognize_speech(audio)
            
            cancelled = False
            
            if message.lower() == "iptal et" or message.lower() == "vazge??tim":
                assistant_speak("Email g??nderme i??lemi iptal edildi","tr")
                cancelled = True
                
            elif send_email.send_email(target, message) and not cancelled:
                assistant_speak("Email ba??ar??yla g??nderildi","tr")
                
            elif not send_email.send_email(target, message) and not cancelled:
                assistant_speak("Bir hata meydana geldi. L??tfen tekrar deneyin.","tr")
                
        elif intent.lower() == "haberleri okur musun" or intent.lower() == "haberleri okuman?? istiyorum" or intent.lower() == "haberleri oku" or intent.lower() == "haber oku":
            assistant_speak("Hangi kategoriden haber okumam?? istersin","tr")
            
            with mic as source:
                audio = r.listen(source)
            category = recognize_speech(audio)
            
            if category.lower() == "hangi kategoriler var" or category.lower() == "hangi kategoriden okuyabilirsin":
                assistant_speak("Spor.....Son Dakika....Magazin.....Ekonomi.....Sa??l??k.....D??nya.....Politika.....Otomobil.....Teknoloji","tr")
                with mic as source:
                    audio = r.listen(source)
                category = recognize_speech(audio)
                
            if "spor" in category.lower() or "son dakika" in category.lower() or "magazin" in category.lower() or "ekonomi" in category.lower() or "sa??l??k" in category.lower() or "d??nya" in category.lower() or "politika" in category.lower() or "otomobil" in category.lower() or "teknoloji" in category.lower():
                
                try: 
                    title, detail = get_news.get_news(category.lower())
                    
                    assistant_speak(title,"tr")
                    
                    assistant_speak("Detay??n?? okumam?? ister misin","tr")
                    
                    with mic as source:
                        audio = r.listen(source)
                    answer = recognize_speech(audio)
                    
                    if answer.lower() == "evet":
                        
                        assistant_speak(detail,"tr")
                        
                    elif answer.lower() == "hay??r":
                        
                        assistant_speak("Tamam kapat??yorum","tr")
                        
                except:
                    
                    assistant_speak("Bir hata meydana geldi. L??tfen tekrar deneyin","tr")
                    
        elif intent.lower() == "bana y??n tarifi ver" or intent.lower() == "y??n tarifi ver" or intent.lower() == "bana yol tarifi ver" or intent.lower() == "yol tarifi ver" or intent.lower() == "bir yere gitmek istiyorum":
            
            assistant_speak("Nereye gitmek istiyorsun","tr")
            
            with mic as source:
                audio = r.listen(source)
            target = recognize_speech(audio)
            
            get_direction.get_direction(target)
            
        elif intent.lower() == "bana film a??" or intent.lower() == "bana dizi a??" or intent.lower() == "film a??" or intent.lower() == "dizi a??" or intent.lower() == "bana film a??ar m??s??n" or intent.lower() == "bana dizi a??ar m??s??n" or intent.lower() == "film a??ar m??s??n" or intent.lower() == "dizi a??ar m??s??n":
            
            if "dizi" in intent.lower():
                assistant_speak("Hangi diziyi a??ay??m","tr")
            elif "film" in intent.lower():
                assistant_speak("Hangi filmi a??ay??m","tr")
                
            with mic as source:
                audio = r.listen(source)
            name = recognize_speech(audio)
            
            open_movie_tvshow.open_movie_tvshow(name)
        
        elif intent.lower() == "bir f??kra anlat" or intent.lower() == "bana bir f??kra anlat" or intent.lower() == "beni g??ld??r":
            
            joke = make_joke.make_joke()
            
            music = pyglet.media.load("fikra.mp3", streaming=False)
            music.play()
            sleep(music.duration)
            
            assistant_speak(joke,"tr")
            
            music = pyglet.media.load("fikra.mp3", streaming=False)
            music.play()
            sleep(music.duration)