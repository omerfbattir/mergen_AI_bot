# -*- coding: utf-8 -*-
import baseSkills as bs 
import datetime
import time
import wolframalpha
import requests
from selenium import webdriver

'''
# Install python requirements
pip3 install -r requirements.txt
'''

def close():
    print("Görüşmek üzere!")
    bs.speak("Görüşmek üzere")

def date():
    an = datetime.datetime.now()
    date = datetime.datetime.strftime(an, '%x')
    day = datetime.datetime.strftime(an, '%A')
    bs.speak(f"Bugünün tarihi {date} {day}")
    print(f"Bugünün tarihi: {date} {day}")

def wikiSearch(text):
    text = text.replace("wikipedia", "")
    text = text.replace("nedir", "")
    text = text.replace("kimdir", "")
    bs.wikipedia_search(text)

def clock():
    cur_time = datetime.datetime.now()
    cur_time = cur_time.strftime("%H:%M:%S")
    bs.speak(f"Saat {cur_time}")

def search(text):
    text = text.replace("ara", "")
    bs.google_search(text)
    bs.speak("İşte bunları buldum", 6)

def calculate(text):
    api_id = "LYH8JE-XHUWTAJVJX"
    wolfram_cli = wolframalpha.Client(api_id)
    indx = text.split().index('hesapla')
    text = text.split()[indx + 1:]
    res = wolfram_cli.query(' '.join(text))
    answer = next(res.results).text
    print("İşlemin sonucu: " + answer)
    bs.speak("İşlemin sonucu " + answer)

def weather(text = "antalya"):
    text_city = text.replace("hava durumu", "")
    api_key = "e2024c81d0ce1686c5b70152fdd01b9d"
    base_url="https://api.openweathermap.org/data/2.5/weather?"
    full_url = base_url + "appid="+api_key+"&q="+ text_city +"&lang=tr"+"&units=metric"
    response = requests.get(full_url)
    x=response.json()
    if x["cod"]!="404":
        y=x["main"]
        cur_temp = y["temp"]
        cur_hum = y["humidity"]
        z = x["weather"]
        weather_des = z[0]["description"]
        w_f1 = f"Bugün {text_city} ilinde hava {weather_des} "
        w_f2 = f"{cur_temp} derece "
        w_f3 = f"ve nem oranı %{cur_hum}"
        weather_forecast = w_f1 + w_f2 + w_f3
        bs.speak(weather_forecast)

def news():
    driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    driver.get("https://www.bbc.com/turkce")
    bs.speak("BBC Türkçeden haberler, iyi okumalar")
    time.sleep(6)