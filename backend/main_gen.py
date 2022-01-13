import speech_recognition as sr
import vts as vts
import vtt as vtt
import keywords as keywords

def genearte(file):
    # path = "keyord\" + str(file) 
    vts.sound(file)
    str = vtt.key()
    return keywords.generate_keyword(str)