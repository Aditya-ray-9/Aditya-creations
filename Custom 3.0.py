import email.message
import cryptography.fernet
import phonenumbers.carrier
import phonenumbers.geocoder
import phonenumbers.timezone
import pyttsx3
import datetime
import wikipedia
import tkinter
from tkinter.constants import *
import webbrowser
import random
from plyer import notification
import os as operating_system
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
import speedtest
import math
import translate
from translate import Translator
import time
from cryptography.fernet import Fernet

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
                query = input(input_text)
                return query
        def In(input_prompt) :
            input(input_prompt)

class games :
    def guessing_game(level_in_int) :
        max_number = 100 * level_in_int
        random_number = random.randint(0, max_number)
        count = 1
        # print(f"for debuging {random_number}")
        condition = False
        speech = ["i dont think you can win this game ", "you fail try again noob", "what a bot leave from here this game is not for you ", " what a bot try again ", "do you really think you can win this game", "you are a noob ", "hahahaha you can't win this game ", "you fail again", "coammon you can't win this game ", "try again bot ", "this boy can't win this game", "its not for you noob", "it not for noobs so leave from here ", "i can't control my laugh", "you, the king of bots "]
        speech_win = ["no its not possible for you to win this game", "you hacker ", "you have used hack i know it ", "you have cheated", "thats your luck ", "the luck was with you ", "the program think that noob should also win hahahaha ", "i know you won with the help of cheating ", "there is an issue with the program so you won by a mistake noob ", "i can't believe that  ", "really a noob like you can won "]
        while condition == False :
            index = random.randint(0, int(speech.__len__()) - 1)
            sprint(speech[index])
            userinput = int(input(f"Enter your number which is between 0 to {max_number} : "))
            if userinput == random_number :
                sprint("you won")
                sprint(f"you won in {count} try ")
                continue
            elif userinput >= random_number :
                sprint("too high ")
                count = count + 1
            elif userinput <= random_number :
                sprint("too low ")
                count = count + 1
            elif userinput == random_number :
                if count == 1 :
                    sprint(f"unbeleveable you won in first try ")
                elif count == 2 :
                    sprint(f"you won in second try ")
                elif count == 3 :
                    sprint(f"you won in third try ")
                elif count == 4 :
                    sprint(f"you won in fourth try ")
                elif count == 5 :
                    sprint(f"you won in fifth try ")
                else :
                    sprint(f"you won in {count} tries ")
                win_rost_len = int(speech_win.__len__())
                index = randint(0, win_rost_len - 1)
                sprint(speech_win[index])
                condition = True
                
            else :
                break

    def help() :
        print("Usage: using this function i mean games.guessing_game(your_level) you can \n play a game in which you have to choose a number of 0 to a number depending on your level, \n if your number and the computer number are equal then you won the game else the program will tell that \n you number is higher than computer or lower that can might help you \n to win the game so good luck remember this game have infinite levels \n so you can enjoy the levels ")
    

# math
class math :
    def Random(a, b) :
        print(randint(a, b))
    def add(a, b) :
        print(a+b)

    def sum(a, b, c) :
        print(a+b+c)

    def sub(a, b) :
        print(a-b)
    def lcm(number1, number2, number3) :
        try :
            print(math.lcm(number1, number2, number3))
        except TypeError as e :
            print(e)
    def hcf(number1, number2, number3) :
        try :
            print(math.gcd(number1, number2, number3))
        except TypeError as e :
            print(e)
    def Square_root(x) :
        math.sqrt(x)
        return x

    def power(number, number_of_power) :
        return math.pow(number, number_of_power)

    pi = 3.142857142857143
    def cube_root(X) :
        math.cbrt(X)

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
def forlite(number_of_times, work) :
    a = 0
    while a <= number_of_times :
        print(work)
        a = a + 1

class translation :
    def translate(text ,language) :
        translator = Translator(to_lang=language)
        translation = translator.translate(text)
        print(text)
        global language_list    

    def help() :
        print("by using this module you can translate simple words and sentances ")
        print("to download this module to go terminal and type ( pip install translate ) ")
        print("you can use the cammands to translate language to language by writing this : ")
        print("from translate import Translator")
        print("translator = Translator(to_lang=fr)")
        print('text = "your text" #create a variable in which your text to translate you can also take it input ')
        print("translation = translator.translate(text)")
        print("print(translation)")
        # translator = Translator()
        # language_list = translator.languages
        # for code, name in language_list.items():
        #     print(f"{code} {name}")

class os :
    def launch(path_or_url) :
        try :
            try :
                operating_system.startfile(path_or_url)
            except Exception as launch_error :
                operating_system.open(path_or_url)
        except Exception as launch_error :
            webbrowser.open(path_or_url)
    def rename(path_of_file) :
        try :
            os.rename(path_of_file)
        except Exception as launch_error : 
            print("Could not rename")
            print(f"reason : \n {launch_error}")
    def replace(path_of_file, replacement_location):
        try :
            pass
        except Exception as launch_error :
            print("failed to move file ")
            print("reasons: \n" + str(launch_error))
    def move(path_of_file, moving_path):
        os.replace(path_of_file, moving_path)
    def listdir(path) :
        try :
            os.listdir(path)
        except OSError as e :
            print("Could not list directory reason : " + str(e))
    def remove(path) :
        try :
            os.remove(path)
        except OSError as e :
            print("Could not remove directory reason : " + str(e))
    def exists(path) :
        files = operating_system.listdir()
        for file in files :
            if path == file:
                return True
            else :
                return False
    def change_dir(path) :
        try :
            operating_system.chdir(path)
        except Exception as e :
            print(f"Error reason : \n {e}")
    def make_directory(path): 
        operating_system.mkdir(path)

#hacks

class hack :
    def encrypt_file(file_path, key):
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = Fernet(key).encrypt(data)
        with open(file_path, 'wb') as file:
            file.write(encrypted_data)

    def decrypt_file(file_path, key):
        with open(file_path, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = Fernet(key).decrypt(encrypted_data)
        with open(file_path, 'wb') as file:
            file.write(decrypted_data)

    def encrypt_directory(directory_path, key):
        file_paths = []
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                hack.encrypt_file(file_path, key)

    def decrypt_directory(directory_path, key):
        file_paths = []
        for root, _, files in os.walk(directory_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                hack.decrypt_file(file_path, key)

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

            print(service)
            speak(service)

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

def table(number, number_of_times) :
    answer = number
    i = 1
    while i <= number_of_times :
        print(f"{number}x{i}={answer * i}")
        i = i + 1

def SpeedTest() :
    st = speedtest()
    print("checking downloading speed... ")
    print("this may take a long... ")
    try :
        download_speed = st.download() / 1_000_000
        print(f"your downlaod speed is {download_speed:.2f}")
    except Exception as e :
        print(f"test failed reasion {e}")
    print("checking upload speed... ")
    print("this may take a long... ")
    try :
        upload_speed = st.upload() / 1_000_000
        print(f"upload speed is {upload_speed:.2f}")
    except Exception as e :
        print(f"test failed reasion : {e}")


class path :
    path = ["C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe","C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe","www.youtube.com", "www.google.com", "www.invideo.io"]
    chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
    vscode = "C:\\Users\\dell\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    tlauncher = "C:\\Users\\dell\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
    minecraft_java = "C:\\Users\\dell\\AppData\\Roaming\\.minecraft\\TLauncher.exe"
    minecraft_feather = "C:\\Program Files\\Feather Launcher\\Feather Launcher.exe"
    discord = "C:\\Users\\dell\\AppData\\Local\\Discord\\Update.exe --processStart Discord.exe"
    photoshop = "C:\\Program Files\\Adobe\\Adobe Photoshop 2020\\photoshop.exe"

def text_to_binary(text):
    binary = ''.join(format(ord(char), '08b') for char in text)
    return binary

def binary_to_text(binary):
    n = 8
    text = ''.join(chr(int(binary[i:i+n], 2)) for i in range(0, len(binary), n))
    return text

class Time :
    global hour, minutes, date
    hour = datetime.datetime.now().hour
    minutes = datetime.datetime.now().minute
    date = datetime.datetime.today()
    def help() :
        print("hey this is the time class from Custom so using this class you can some functions that can might help you so the \n1st i randdate this function returns a random date like 4 february or something randomly\n 2nd rantime   you this you can returns a random time like 12:34 9 september  \n 3rd function randclock using this function you can generate a random time like 3:23 am or something \n 4th realtime this function prints the returns the realtime thet is currently on your phone\n thank you your friend aditya")
    
    def randdate() :
        month = random.randint(1, 12)
        if month == 1 :
            date = random.randint(1, 31)
        elif month == 2 :
            date = random.randint(1, 28)
        elif month == 3 :
            date = random.randint(1, 31)
        elif month == 4 :
            date = random.randint(1, 30)
        elif month == 5 :
            date = random.randint(1, 31)
        elif month == 6 :
            date = random.randint(1, 30)
        elif month == 7 :
            date = random.randint(1, 31)
        elif month == 8 :
            date = random.randint(1, 30)
        elif month == 9 :
            date = random.randint(1, 31)
        elif month == 10 :
            date = random.randint(1, 3)
        elif month == 11 :
            date = random.randint(1, 31)
        elif month == 12 :
            date = random.randint(1, 3)
        else :
            pass

        if month == 1 :
            month_name = "january"
        elif month == 2 :
            month_name = "february"
        elif month == 3 :
            month_name = "march"
        elif month == 4 :
            month_name = "april"
        elif month == 5 :
            month_name = "may"
        elif month == 6 :
            month_name = "june"
        elif month == 7 :
            month_name = "july"
        elif month == 8 :
            month_name = "Augest"
        elif month == 9 :
            month_name = "September"
        elif month == 10 :
            month_name = "October"
        elif month == 11 :
            month_name = "November"
        elif month == 12 :
            month_name = "December"
        else :
            pass
        return f"{date} {month_name}"
    def randclock() :
        minutes_random = randint(0, 60)
        hour_random = randint(0, 12)
        am_or_pm = randint(1, 4)

        if am_or_pm == 1 or am_or_pm == 3 :
            period = "am"
        elif am_or_pm == 2 or am_or_pm == 4 :
            period = "pm"
        else :
            pass
        return f"{hour_random}:{minutes_random} {period}"

    def randtime() :
        hour = randint(1, 12)
        am_or_pm = randint(1, 4)
        min = randint(0, 60)

        
        if am_or_pm == 1 or am_or_pm == 3 :
            random_time = f"{hour}:{min} am"
        elif am_or_pm == 2 or am_or_pm == 4 :
            random_time = f"{hour}:{min} pm"
        else :
            pass
        return random_time
    
    def realtime() :
        real_time = f"{hour}:{minutes} {date}"
        return real_time

def notify(title_for_massage, massage_for_massage, duration):
    notification.notify(
        title=title_for_massage,
        message=(massage_for_massage),
        app_name=title_for_massage,
        # app_icon="glass_water.ico",  # ensure this path is correct
        timeout = duration  # duration in seconds
    )

def displayer(text) :
    tk = tkinter.Tk()
    frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
    frame.pack(fill=BOTH,expand=1)
    randtime_displayer = tkinter.Label(frame, text=text)
    randtime_displayer.pack(fill=X, expand=1)
    button = tkinter.Button(frame,text="Exit",command=tk.destroy)
    button.pack(side=BOTTOM)
    tk.mainloop()

slash = "'\'"
class Alpha:
    char_map = {chr(i): str(i-96) + '.' for i in range(97, 123)}  # a-z
    char_map.update({chr(i): str(i-64) + str(i-64) + '.' for i in range(65, 91)})  # A-Z
    special_char_map = {
        '@': '_1_', '!': '_2_', '#': '_3_', '$': '_4_',
        '+': '__1__', '-': '__2__', '*': '__3__', '/': '__4__',
        '%': '__5__', '^': '__6__', '(': '_5_', ')': '_6_',
        '{': '_7_', '}': '_8_', '[': '_9_', ']': '_10_',
        '<': '_11_', '>': '_12__', ':': '_13_', ';': '_14_',
        "'": '_15_', '"': '_16_', '|': '_17_', ',': '_18_',
        '?': '_19_', '.': '_20_', '=': '_21_', '_': '_22_',
        '~': '_23_', '`': '_24_', ' ': '..', slash: '_25_'
    }

    @staticmethod
    def generate(string_base):
        output = []
        for char in string_base:
            if char in Alpha.char_map:
                output.append(Alpha.char_map[char])
            elif char in Alpha.special_char_map:
                output.append(Alpha.special_char_map[char])
            elif char.isdigit():
                output.append(f"${char}")
            elif char.isdecimal():
                output.append(f"!{char}")
        return "".join(output)

    def help() :
        help_file = open("C:\\Users\\dell\\.vscode\\projects\\python projects\\projets\\Alpha\\help.txt", "r")
        help_text = help_file.read()
        print(help_text)

if __name__ == '__main__' :
    # encrypt("C:\\Users\\dell\\Pictures\\test of ransomware")
    level = int(input("Enter your level : "))
    games.guessing_game(level)
