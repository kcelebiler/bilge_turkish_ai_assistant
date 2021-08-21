from forex_python.converter import CurrencyRates

currency_abbreviations = {
        "dolar": "USD",
        "türk lirası": "TRY",
        "tl": "TRY",
        "Türk": "TRY",
        "euro": "EUR",
        "japon yeni": "JPY",
        "avustralya doları": "AUD",
        "isviçre frangı": "CHF",
        "ingiliz sterlini": "GBP",
        "sterlin": "GBP",
        "ermeni dramı": "AMD",
        "belçika frangı": "BEF",
        "azerbaycan manatı": "AZN",
        "manat": "AZN",
        "bahreyn dinarı": "BHD",
        "kuveyt dinarı": "KWD",
        "ruble": "RUB",
        "rus rublesi": "RUB",
        "hint rupisi": "INR",
        "kanada doları": "CAD"
        
    }


c = CurrencyRates()

def get_currency(source='türk lirası', target='dolar'):
    
    return c.get_rate(currency_abbreviations[source], currency_abbreviations[target])