import pprint
import sys

import requests


class GetData:
    def __init__(self, url):
        self.url = url
        self.data = self.get_data()
    
    def get_data(self):
        r = requests.get(self.url)
        return r.json()


class CheckFile:
    def __init__(self):
        with open('weather.txt', 'r') as file:
            for line in file.readlines():
                date = line.split(',')[0]
                #print(date)
    
    def will_it_rain(self, dzien):
        self.dzien = dzien
        flag = False
        with open('weather.txt', 'r') as file:
            for line in file.readlines():
                date = line.split(',')[0]
                willitrain = line.split(',')[1]
            if self.dzien == date:
                print('Chance of rain :' + willitrain)
                flag = True
        return flag
    def write_file(self, date, chance):
        with open ('weather.txt', 'a') as file:
            file.write(str(date) + ',' + str(chance) + '\n')


    #def __str__(self):


class SortThingsOut:
    def __init__(self):   
        pass


key = sys.argv[1]
try:
    days = str(sys.argv[2])
except:
    days = '1'
town = 'Szczecin'

arcticmonkey = input("Hello dear customer, please tell us, which date are u insterested in ?? Remember to input date in format YYYY-MM-DD\n")
if arcticmonkey:
    plik = CheckFile()
    deszcz = plik.will_it_rain(arcticmonkey)
    if not deszcz:
        data = GetData('http://api.weatherapi.com/v1/forecast.json?key=' + key + '&q=' + town + '&days=' + days + '&aqi=no')
        for day in data.data['forecast']['forecastday']:
            #print(day['date'])
            if arcticmonkey == day['date']:
                print(day['day']["daily_will_it_rain"])
                plik.write_file(arcticmonkey,day['day']["daily_will_it_rain"])



#data = int(input('Dla którego dnia chcesz znac szanse na deszcz ?'))
#importuje z api do pliku informacje o tym czy bedzie padac. Potem pytam uzytkownika o date jaka chce znac, jesli nie ma daty w pliku zwracam blad. Najpierw sprawdzam plik, czy istnieje zapis, potem dopiero wysylam zapytanie do API.
#print(data.data['forecast']['forecastday'][0]['date'])
#wrzucam 10 dni do pliku

#możliwy print jest na x dni do przodu.
'''{
    "location": {
        "name": "Szczecin",
        "region": "",
        "country": "Poland",
        "lat": 53.42,
        "lon": 14.58,
        "tz_id": "Europe/Warsaw",
        "localtime_epoch": 1623847930,
        "localtime": "2021-06-16 14:52"
    },
    "current": {
        "last_updated_epoch": 1623846600,
        "last_updated": "2021-06-16 14:30",
        "temp_c": 23.0,
        "temp_f": 73.4,
        "is_day": 1,
        "condition": {
            "text": "Sunny",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
            "code": 1000
        },
        "wind_mph": 0.0,
        "wind_kph": 0.0,
        "wind_degree": 133,
        "wind_dir": "SE",
        "cloud": 0,
        "uv": 6.0,
        "gust_mph": 5.8,
        "gust_kph": 9.4
    }
}'{
    "location": {
        "name": "Szczecin",
        "region": "",
        "country": "Poland",
        "lat": 53.42,
        "lon": 14.58,
        "tz_id": "Europe/Warsaw",
        "localtime_epoch": 1624378108,
        "localtime": "2021-06-22 18:08"
    },
    "current": {
        "last_updated_epoch": 1624374000,
        "last_updated": "2021-06-22 17:00",
        "temp_c": 18.0,
        "temp_f": 64.4,
        "is_day": 1,
        "condition": {
            "text": "Partly cloudy",
            "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
            "code": 1003
        },
        "wind_mph": 10.5,
        "wind_kph": 16.9,
        "wind_degree": 340,
        "wind_dir": "NNW",
        "cloud": 25,
        "uv": 6.0,
        "gust_mph": 11.9,
        "gust_kph": 19.1
    },
    "forecast": {
        "forecastday": [
            {
                "date": "2021-06-22",
                "date_epoch": 1624320000,
                "day": {
                    "maxtemp_c": 22.9,
                    "maxtemp_f": 73.2,
                    "mintemp_c": 13.7,
                    "mintemp_f": 56.7,
                    "avgtemp_c": 17.7,
                    "avgtemp_f": 63.9,
                    "maxwind_mph": 10.1,
                    "maxwind_kph": 16.2,
                    "totalprecip_mm": 0.0,
                    "totalprecip_in": 0.0,
                    "avgvis_km": 10.0,
                    "avgvis_miles": 6.0,
                    "avghumidity": 72.0,
                    "daily_will_it_rain": 0,
                    "daily_chance_of_rain": "0",
                    "daily_will_it_snow": 0,
                    "daily_chance_of_snow": "0",
                    "condition": {
                        "text": "Partly cloudy",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/116.png",
                        "code": 1003
                    },
                    "uv": 5.0
                },'''


