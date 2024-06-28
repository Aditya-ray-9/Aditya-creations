import phonenumbers
from phonenumbers import geocoder, carrier, timezone
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voices", voices[0].id)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()

def say(audio) :
    speak(audio)

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
        Timezone = timezone.time_zones_for_number(info)
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


if __name__ == "__main__" :
    number = input("Enter your mobile number : ")
    details(number, "r")
