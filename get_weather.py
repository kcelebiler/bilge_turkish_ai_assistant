import requests, json
# base URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
METRIC = "&units=metric"
API_KEY = "c16d1e4215ae8e4f626060820b0d2158"

def get_weather(CITY):
    
    URL = BASE_URL + "q=" + CITY + METRIC + "&appid=" + API_KEY
    response = requests.get(URL)
    if response.status_code == 200:
       data = response.json()
       main = data['main']
       temperature = main['temp']
       humidity = main['humidity']
       report = data['weather']
       description = report[0]['description']
       return temperature, humidity, description
    else:
       return "Hata " + str(response.status_code)
       
print(get_weather("istanbul"))