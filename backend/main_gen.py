import speech_recognition as sr
import vts as vts
import vtt as vtt
import keywords as keywords

def genearte(file,token):
    # path = "keyord\" + str(file) 
    print("1")
    filename = vts.sound(file,token)
    print("2")
    str = vtt.key(filename)
    print("3")
    return keywords.generate_keyword(str)