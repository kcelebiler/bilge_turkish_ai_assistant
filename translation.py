from google_trans_new import google_translator  

supported_langs={
        'İngilizce' : "en",
        'Fransızca' : "fr",
        'Almanca' : "de",
        'İspanyolca' : "es",
        'Arapça' : "ar",
        'Rusça' : "ru",
        'Türkçe' : "tr"
}

translator = google_translator()

def translate(text, target):
    if target in supported_langs.keys():
        if target == "Türkçe":
            return translator.translate(text, lang_src='en', lang_tgt='tr')
        else:
            return translator.translate(text, lang_src='tr', lang_tgt=supported_langs[target])
    else:
        return "Bu dil desteklenmiyor"