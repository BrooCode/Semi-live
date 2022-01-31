import moviepy.editor as mp

def sound(path,token):
    print("vts1")
    my_clip = mp.VideoFileClip(path)
    print("vts2")
    temp = "my_result" + str(token) + ".wav"
    my_clip.audio.write_audiofile(temp)
    print("vts3")
    return temp