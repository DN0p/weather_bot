import requests
import json

def weather(city):
    api_dr = "http://api.openweathermap.org/data/2.5/weather?appid=Enter your key"
    url = api_dr + city
    json_data = requests.get(url)
    my_data = json.loads(json_data.text)
    try:
        your_city = my_data['name']
        your_weather = my_data['main']['temp']
        your_weather = your_weather - 274.150
    except Exception:
        return 'Я не могу это прочесть -_- '
    if your_weather >= 22:
        return 'Сегодня на улице довольно жарко, {} градусов, доставай шорты и майку!'.format(round(your_weather,2))
    elif your_weather < 22 and your_weather >= 15:
        return '{} градусов. Советую захватить с собой куртку. Лишним не будет.'.format(round(your_weather,2))
    elif your_weather < 15 and your_weather >= 8:
        return '{} градусов. Зима близко.'.format(round(your_weather,2))
    else:
        return '{} градусов. Чертовски холодно! Одевайся как на экспедицию'.format(round(your_weather,2))


