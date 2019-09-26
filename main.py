import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)


def getAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))

    return said


speak("I'm Gabbar.Py")
getAudio()

text = getAudio()

if "hello" in text:
    speak("Hello, how're your?")

if "what is your name" in text:
    speak("My name is Gabbar.Py!")
