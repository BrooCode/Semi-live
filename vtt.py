import os
import speech_recognition as sr

def key():
    r = sr.Recognizer()
    audio = sr.AudioFile('keyword\my_result.wav') 

    with audio as source:
        audio = r.record(source, duration=100)
        return r.recognize_google(audio)

