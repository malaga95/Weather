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
            if arcticmonkey == day['date']:
                print(day['day']["daily_will_it_rain"])
                plik.write_file(arcticmonkey,day['day']["daily_will_it_rain"])