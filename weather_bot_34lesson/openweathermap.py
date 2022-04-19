import requests
import config
base_url = 'https://api.openweathermap.org/data/2.5/weather?'
# https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
# https://api.openweathermap.org/data/2.5/weather?q=Moscow&units=metric&lang=ru&appid=11302685d611216bbe07c09a620346c4

def get(city):
    try:
        data = requests.get(
            base_url,
            params={
                'q': city,
                'units': config.units,
                'lang': config.language,
                'appid': config.weather_token

            })
        data1 = data.json()#ответ в виде строки в словарь

        description = data1['weather'][0]['description']
        temp = data1['main']['temp']
        name = data1['name']
        return name, description, temp
    except Exception as e:
        return e

