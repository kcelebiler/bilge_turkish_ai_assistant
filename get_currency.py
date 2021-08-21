from forex_python.converter import CurrencyRates

currency_abbreviations = {
        "dolar": "USD",
        "türk lirası": "TRY",
        "tl": "TRY",
        "Türk": "TRY",
        "euro": "EUR",
        "japon yeni": "JPY"
    
    }

#print("türk lirası ve dolar".split(" ve "))

c = CurrencyRates()

def get_currency(source='türk lirası', target='dolar'):
    
    return c.get_rate(currency_abbreviations[source], currency_abbreviations[target])