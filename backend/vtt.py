import os
import speech_recognition as sr

def key(file):
    r = sr.Recognizer()
    audio = sr.AudioFile(file) 
    try:
        with audio as source:
            audio = r.record(source, duration=100)
            return r.recognize_google(audio)
    except:
        print("Noise Issue")
