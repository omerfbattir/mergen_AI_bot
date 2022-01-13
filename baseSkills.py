# -*- coding: utf-8 -*-
import speech_recognition as sr
from playsound import playsound
from gtts import gTTS
import locale
import wikipedia
import random
import os
from selenium import webdriver

'''
# Install python requirements
pip3 install -r requirements.txt
'''

re = sr.Recognizer()
mic = sr.Microphone()
locale.setlocale(locale.LC_ALL, '')

def speak(text, num = random.randint(50,3000)):
    tts = gTTS(text, lang ='tr')
    file = "audio-"+str(num)+".mp3"
    print(text)
    tts.save(file)
    playsound(file)
    os.remove(file)

def listen():
    "listens for commands"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
    try:
        u_text = r.recognize_google(audio, language = "tr").lower()
        print(u_text + ' dediniz')
    
    except sr.UnknownValueError:
        print("Üzgünüm ne dediğinizi anlayamadım")
        speak("Üzgünüm ne dediğinizi anlayamadım")
        u_text = listen()
    return u_text

def google_search(stext):
    stext = stext.split()
    search_object = ""
    for i in stext[1:-2]:
        search_object = search_object + i
    driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    driver.get("http://google.com/search?q=" + search_object)
    
def wikipedia_search(stext): # stext = searched text
    wikipedia.set_lang("tr")
    search_result = wikipedia.summary(stext, sentences = 5)
    speak(search_result)
    driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    driver.get("https://tr.wikipedia.org/wiki/" + stext)
    
def youtube_search(stext):
    stext = stext.split()
    song_name = ""
    for i in stext[1:-1]:
        song_name = song_name + i
    driver = webdriver.Chrome(r"C:\Program Files\Google\Chrome\Application\chrome.exe")
    driver.get("https://www.youtube.com/results?search_query=" + song_name)
    select_element = driver.find_elements_by_xpath('//*[@id="video-title"]')
    for option in select_element:
        option.find_element_by_xpath('//*[@id="video-title"]').click()
        break
    return driver
    