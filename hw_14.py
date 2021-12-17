"""
1. создать функцию(ии) для  определения погоды по данным(Город).
2. Вынести некоторрые данные в константу(ы).
3. Для запуска функции использовать if __name__ == '__main__': запуск!
4. Создать файл test.py  внутри создать Класс для тестирования функции, с помощью unittest.
"""

import requests


BASE_IRL = 'http://api.openweathermap.org/data/2.5/weather?'
API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa'


def get_temp(city: str='Kharkov'):

    result: str = ''
    complete_url = BASE_IRL + 'appid=' + API_KEY + '&q=' + city
    response = requests.get(complete_url)
    r_data = response.json()
    if r_data['cod'] != '404':
        y = r_data['main']
        current_t = y['temp']
        current_p = y['pressure']
        z = r_data['weather']
        # weather_description = z[0]['description']
        result = 'Celsius:' + str((round(current_t - 273.15))) + ' ' +\
                 'Pressure:' + str(current_p)
    else:
        result = 'City not found.'

    return result


