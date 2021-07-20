from bs4 import BeautifulSoup
import speech_recognition as sr
import pyttsx3
from vosk import Model, KaldiRecognizer
import sys, os, json, re
from ezprint import p
import requests

class Response:
    def __init__(self):
        if not os.path.exists('model'):
            print ("Please download the model from https://github.com/alphacep/vosk-api/blob/master/doc/models.md and unpack as 'model' in the current folder.")
            exit (1)
        model = Model('model')
        self.rec = KaldiRecognizer(model, 16000)
        p = pyaudio.PyAudio()
        self.stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.stream.start_stream()

    def micro(self):
        data = self.stream.read(4000, exception_on_overflow=False)
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if len(data) == 0:
                pass
            if self.rec.AcceptWaveform(data):
                x=json.loads(self.rec.Result())
                print(x['text'])
                return(x['text'])
            else:
                pass

def talk(words):
    engine = pyttsx3.init()
    engine.say(words)
    engine.runAndWait()

class Request:
    def __init__(self):
        url = 'https://ru.wikipedia.org/wiki/Список_городов_России'
        r = requests.get(url).text
        self.cities = []
        self.answer = ''
        self.end = ''
        html = r
        soup = BeautifulSoup(html, 'lxml')
        table = soup.find('div', class_ = 'mw-parser-output').find_all('tr')
        k = 0
        for i,j in zip(table, range(1119)):
            for x in i.find_all('td'):
                if k == 2:
                    self.cities.append(x.getText())
                    k = 0
                    break
                k+=1

    def find_city(self, message, start):
        check = 0
        if (len(self.answer)>0) and (self.end != message[0].upper()):
            return 'Правила не соблюдены'
        for i,j in zip(self.cities, range(len(self.cities))):
            i = i[1:-1]
            if (i == message.capitalize()):
                self.cities.pop(j)
                check = 1
        if (check):
            for i,j in zip(self.cities, range(len(self.cities))):
                i = i[1:-1]
                if i[0] == message[-1].upper():
                    self.answer = i
                    self.end = self.answer[-1].upper()
                    if self.answer[-1].upper() == 'й':
                        self.end = 'И'
                    elif self.answer[-1].upper() == 'Ь':
                        self.end = self.answer[-2].upper()
                    self.cities.pop(j)
                    return self.answer
        else:
            return 'Города нет в РФ или он уже был использован'