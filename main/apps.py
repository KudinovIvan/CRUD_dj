from bs4 import BeautifulSoup
from ezprint import p
import requests
import os
import re

url = 'https://ru.wikipedia.org/wiki/Список_городов_России'

def get_html(url):
    r = requests.get(url).text
    return r

def parse():
    cities = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find('div', class_ = 'mw-parser-output').find_all('tr')
    k = 0
    for i,j in zip(table, range(1119)):
        for x in i.find_all('td'):
            if k == 2:
                cities.append(x.getText())
                k = 0
                break
            k+=1
    return cities

cities=[]

def find_city(message, start):
    global cities
    check = 0
    if(start):
        cities=parse()
        return cities
    else:
        for i,j in zip(cities, range(len(cities))):
            i = i[1:-1]
            if (i == message.capitalize()):
                cities.pop(j)
                check = 1
        if (check):
            for i,j in zip(cities, range(len(cities))):
                i = i[1:-1]
                if i[0] == message[-1].upper():
                    answer = i
                    cities.pop(j)
                    return answer
        else:
            return "Города нет в РФ или он уже был использован"