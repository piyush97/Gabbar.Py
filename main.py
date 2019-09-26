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


speak("I'm Gabbar.Py")
