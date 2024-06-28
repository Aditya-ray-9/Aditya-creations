
import phonenumbers.timezone
import pyttsx3
import datetime
import wikipedia
import webbrowser
import time
import os
import random
import math
from random import randint
from opencage.geocoder import OpenCageGeocode
import phonenumbers
from phonenumbers import carrier, geocoder
import folium
import speech_recognition as sr
import pyautogui as auto
import phonenumbers
import zipfile
import time
import email
import cryptography
import pandas


# c++
class cpp :
    def cout(string) :
        print(string)

    def cin(string) :
        user_input = input(string)
        return user_input

#c
class c :
    def printf(string) :
        print(string)

#java
class java :
    # print stament in java demo- System.out.println()
    class System :
        class out :
            def print(string) :
                print(string)
            def println(string) :
                print(string)

    # take input like in java demo- scannar.In()
    class scanner :
        class In :
            def prompt(input_text) :
                input(input_text)
        def In(input_prompt) :
            input(input_prompt)


class V2:
    def Random(a, b) :
        print(randint(a, b))

    def add(a, b) :
        print(a+b)

    def sum(a, b, c) :
        print(a+b+c)

    def sub(a, b) :
        print(a-b)



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(a) :
    engine.say(a)
    engine.runAndWait()
def say(a) :
    speak(a)
def sprint(string) :
    print(string)
    say(string)
def letter_count(str) :
    count = {"LETTERS":0}
    for c in str :
        if c.isdigit() :
            count["LETTERS"]+=1
        else :
            pass
    return count["LETTERS"]
hour = datetime.datetime.now().hour
minutes = datetime.datetime.now().minute

time = f'{hour}:{minutes}'

#mic input
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        sprint("Listening...")
        r.pause_threshold = 0.5  # Adjust the pause threshold (in seconds)
        audio = r.listen(source)

    try:
        sprint("Recognizing...")    
        query = r.recognize_google_cloud(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.
        return query
    
    except sr.WaitTimeoutError:
        say('time out error occurred. no audio deceted')
        print("Timeout occurred. No speech detected.")
        return None

#console

class Console :
    def Println(a, b) :
        print(a, b)
    def log(a) :
        print(a)
    def prompt(x) :
        print(x)
        input(': ')
    def chat(x) :
        engine = pyttsx3.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[0].id)
        say(x)
# java script part
class Runner :
    class prototype :
        def gameover() :
            Console.log("Cammond exited with code 0")
            breakpoint



def Prompt2(
    prompt: object = "",
    /
) -> str :
    pass

def wishme() :
    if hour >= 0 and hour <= 12 :
        print('Good morning')
        say('good morning')

    elif hour >= 12 and hour <= 15 :
        print('Good afternoon')
        say('good afternoon')

    elif hour >= 15 and hour <= 17 :
        print('Good evening')
        say('good evening')

    else :
        print('good night')
        say('good night')

def Web(url) :
    webbrowser.open(url)
def Print(x) :
    print(x)

def wiki(name_of_search, lines) :
    try :
        result = wikipedia.summary(name_of_search, lines)
        print(result)
    except Exception as search_wiki_error :
        Print('Failed to search ,Please check your internet connection and try again')

def repeat(a, repeat_time) :
    repeat_test = 1
    while repeat_test <= repeat_time :
        print(a)
        repeat_test += 1

def launch(path_or_url) :
    try :
        try :
            os.startfile(path_or_url)
        except Exception as launch_error :
            os.open(path_or_url)
    except Exception as launch_error :
        webbrowser.open(path_or_url)



def auto_click(number_of_autoclick) :
    for a in range(number_of_autoclick) :
        heigth = randint(1, 1080)
        width = randint(1, 1920)
        auto.click(heigth, width, duration=1)
        auto.hotkey("winleft", "m")

def details(number_with_country_code, type) :
    number = number_with_country_code
    if type == "read" or "rw" :
        int_number = int(number)
        info = phonenumbers.parse(number)
        country_name = geocoder.description_for_number(info, "en")
        service = carrier.name_for_number(info, "en")
        region = geocoder._region_display_name(int_number, "en")
        query1 = phonenumbers.can_be_internationally_dialled(info)
        religion_code = phonenumbers.region_code_for_country_code(int_number)
        isemergency = phonenumbers.is_emergency_number(number, religion_code)
        Timezone = phonenumbers.timezone.time_zones_for_number(info)
        #output of info
        print(info)
        speak(info)

        #country name output
        print(country_name)
        speak(country_name)

        #service output
        print(service)
        speak(service)

        #region output
        print(region)
        speak(region)

        #displaying the timezone
        print(Timezone)
        speak(Timezone)
        if query1 == True :
            print('this number can be dialled internationlly')
        else :
            print('this number can not be dialled internationally')

        if isemergency == True :
            print('this is a emergency number')
        else :
            print('this number is a genune number')
    elif type == "write" or "w" :
        # some general info
        int_number = int(number)
        info = phonenumbers.parse(number)
        country_name = geocoder.description_for_number(info, "en")
        service = carrier.name_for_number(info, "en")
        region = geocoder._region_display_name(int_number, "en")
        query1 = phonenumbers.can_be_internationally_dialled(info)
        religion_code = phonenumbers.region_code_for_country_code(int_number)
        isemergency = phonenumbers.is_emergency_number(number, religion_code)

        print(info)
        print(country_name)
        print(f"the service provider is {service}")
        print(region)
        if query1 == True :
            print('this number can be dialled internationlly')
        else :
            print('this number can not be dialled internationally')

        if isemergency == True :
            print('this is a emergency number')
        else :
            print('this number is a genune number')
    elif type == "read" or "r" :
        # some general info
        int_number = int(number)
        info = phonenumbers.parse(number)
        country_name = geocoder.description_for_number(info, "en")
        service = carrier.name_for_number(info, "en")
        region = geocoder._region_display_name(int_number, "en")
        query1 = phonenumbers.can_be_internationally_dialled(info)
        religion_code = phonenumbers.region_code_for_country_code(int_number)
        isemergency = phonenumbers.is_emergency_number(number, religion_code)

        say(info)
        say(country_name)
        say(f"the service provider is {service}")
        say(region)
        if query1 == True :
            say('this number can be dialled internationlly')
        else :
            say('this number can not be dialled internationally')

        if isemergency == True :
            say('this is a emergency number')
        else :
            say('this number is a genune number')


def zip_opner(path) :
    zip = open(path, "r")
    print(zip)


class path :
    path = ["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe","C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe","www.youtube.com", "www.google.com", "www.invideo.io"]
    chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    vscode = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    tlauncher = "C:\\Users\\dell\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
    minecraft_java = "C:\\Users\\dell\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
    minecraft_feather = "C:\\Program Files\\Feather Launcher\\Feather Launcher.exe"
    discord = "C:\\Users\\dell\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
    photoshop = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\photoshop.exe"

class alphanumaric :
    number = 0
    while number <= 99999999999999999 :
        number+=1
    a = "a"
    b = "b"
    c = "c"
    d = "d"
    e = "e"
    f = "f"
    g = "g"
    h = "h"
    i = "i"
    j = "j"
    k = "k"
    l = "l"
    m = "m"
    n = "n"
    o = "o"
    p = "p"
    q = "q"
    r = "r"
    s = "s"
    t = "t"
    u = "u"
    v = "v"
    w = "w"
    x = "x"
    y = "y"
    z = "z"
def make_dir(folder_name) :
    if not os.path.exists(folder_name):
        try :
            os.mkdir(folder_name)
        except Exception as e :
            os.makedirs(folder_name)
    else :
        print('The folder already exist')

def rename_dir(folder_name, rename_with) :
    try :
        os.rename(folder_name, rename_with)
    except Exception as e :
        os.renames(folder_name, rename_with)



if __name__ == '__main__' :
    print(letter_count("aditya"))
