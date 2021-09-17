import os
import speech_recognition as sr
import moviepy.editor as mp
import soundfile

# my_clip = mp.VideoFileClip(r"videos\sample.mp4")
# my_clip.audio.write_audiofile(r"my_result.wav")

r = sr.Recognizer()
audio = sr.AudioFile('my_result.wav')

with audio as source:
    audio = r.record(source, duration=100)
    print(r.recognize_google(audio))

