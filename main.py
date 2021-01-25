import os
import sys
import yaml
import speech_recognition as sr

from WhiteMatter.SenseCells.tts import tts


profile = open('profile.yaml')
profile_data = yaml.safe_load(profile)
profile.close()

name = profile_data['name']
city_name = profile_data['city_name']

tts("Welcome" + name + ", the system is now located at" + city_name + "")
WIT_AI_KEY = "Z3I5F37YDLQVHZ3KEULJUC4GCDFXP4FI"

def main():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!") 
        audio = r.listen(source)
    try:
        speech_text = r.recognize_wit(audio, key=WIT_AI_KEY).lower().replace("'", "") 
        print(speech_text + "")
    except sr.UnknownValueError:
        print("Alicia could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    tts(speech_text)
main()