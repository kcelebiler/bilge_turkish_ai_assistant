import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
METRIC = "&units=metric"
API_KEY = "c16d1e4215ae8e4f626060820b0d2158"

weather_descriptions = {
    "clear sky" : "açık",
    "few clouds": "az bulutlu",
    "scattered clouds": "parçalı bulutlu",
    "broken clouds": "parçalı bulutlu",
    "shower rain": "sağanak yağışlı",
    "rain": "yağmurlu",
    "thunderstorm": "gök gürültülü",
    "snow": "karlı",
    "mist": "sisli",
    "thunderstorm with light rain": "gök gürültülü ve az yağışlı",
    "thunderstorm with rain": "yağmurlu ve gök gürültülü",
    "thunderstorm with heavy rain": "gök gürültülü ve sağanak yağışlı",
    "light thunderstorm": "hafif gök gürültülü",
    "heavy thunderstorm": "sert gök gürültülü",
    "ragged thunderstorm": "gök gürültülü",
    "thunderstorm with light drizzle": "gök gürültülü ve az çiseleyen yağışlı",
    "thunderstorm with drizzle": "gök gürültülü ve çiseleyen yağışlı",
    "thunderstorm with heavy drizzle": "gök gürültülü ve fazla çiseleyen yağışlı",
    "light intensity drizzle": "az çiseleyen yağışlı",
    "drizzle": "çiseleyen yağışlı",
    "heavy intensity drizzle": "fazla çiseleyen yağışlı",
    "light intensity drizzle rain": "az çiseleyen yağmurlu",
    "drizzle rain": "çiseleyen yağmurlu",
    "heavy intensity drizzle rain": "sert çiseleyen yağmurlu",
    "shower rain and drizzle": "sert çiseleyen yağmurlu",
    "heavy shower rain and drizzle": "sert çiseleyen yağmurlu",
    "shower drizzle": "bardaktan boşalırcasına yağmurlu",
    "light rain": "hafif yağmurlu",
    "moderate rain": "ılımlı yağmurlu",
    "heavy intensity rain": "sert yağmurlu",
    "very heavy rain": "sert yağmurlu",
    "extreme rain": "aşırı yağmurlu",
    "freezing rain": "dondurucu yağmurlu",
    "light intensity shower rain": "hafif yağmurlu",
    "heavy intensity shower rain": "sert yağmurlu",
    "ragged shower rain": "düzensiz bardaktan boşalırcasına yağmurlu",
    "light snow": "hafif karlı",
    "heavy snow": "sert karlı",
    "sleet": "sulu karlı",
    "light shower sleet": "hafif sulu karlı",
    "shower sleet": "aşırı sulu karlı",
    "light rain and snow": "hafif yağmurlu ve karlı",
    "rain and snow": "yağmurlu ve karlı",
    "light shower snow": "hafif karlı",
    "shower snow": "aşırı karlı",
    "heavy shower snow": "aşırı karlı",
    "smoke": "dumanlı",
    "haze": "puslu",
    "sand/ dust whirls": "kum ve toz girdaplı",
    "fog": "sisle",
    "sand": "kumlu",
    "dust": "tozlu",
    "volcanic ash": "volkanik küllü",
    "squalls": "fırtınalı",
    "tornado": "fırtınalı",
    "overcast clouds": "kapalı bulutlu"
    }

def get_weather(CITY):
    
    """
    gets weather conditions from the openweathermap api

    Args:
        city (string): city name
    Returns:
        temperature (int): temperature value of that city
        humidity (int): humidity value of that city
        weather description (string): weather description of that city
    """

    URL = BASE_URL + "q=" + CITY + METRIC + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
       data = response.json()
       main = data['main']
       temperature = main['temp']
       humidity = main['humidity']
       report = data['weather']
       description = report[0]['description']
       return int(temperature), humidity, weather_descriptions[description]
    else:
       return "Hata " + str(response.status_code)

if __name__ == "__main__":
    
    temperature, humidity, desc = get_weather("istanbul")

    print(str(temperature) + "\n" + str(humidity) + "\n" + desc)
