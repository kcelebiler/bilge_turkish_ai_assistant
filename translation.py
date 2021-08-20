from googletrans import Translator

supported_langs={
        "ingilizce" : "en",
        "fransızca" : "fr",
        "almanca" : "de",
        "ispanyolca" : "es",
        "arapça" : "ar",
        "rusça" : "ru"
}

translator = Translator()

def translate(text, target):
    if target in supported_langs.keys():
        return translator.translate(text, dest=supported_langs[target]).text
    else:
        return "Bu dil desteklenmiyor"