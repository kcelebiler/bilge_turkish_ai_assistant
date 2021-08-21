from forex_python.converter import CurrencyRates

currency_abbreviations = {
        "dolar": "USD",
        "türk lirası": "TRY",
        "tl": "TRY",
        "Türk": "TRY",
        "euro": "EUR",
        "japon yeni": "JPY",
        "avustralya doları": "AUD",
        "ingiliz sterlini": "GBP",
        "sterlin": "GBP",
        "ruble": "RUB",
        "rus rublesi": "RUB",
        "hint rupisi": "INR",
        "kanada doları": "CAD"
        
    }


c = CurrencyRates()

def get_currency(source='türk lirası', target='dolar'):
    print(target)
    print(source)
    if target in currency_abbreviations.keys():
        try:
            return c.get_rate(currency_abbreviations[source], currency_abbreviations[target])
        except:
            return "Bir hata meydana geldi. Lütfen tekrar deneyin."
    
    return "Bu birim desteklenmiyor"