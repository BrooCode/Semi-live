import speech_recognition as sr
import vts as vts
import vtt as vtt
import keywords as keywords

path=r'videos\sample.mp4'
vts.sound(path)
str = vtt.key()

keywords.generate_keyword(str)