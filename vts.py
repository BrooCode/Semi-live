import moviepy.editor as mp

def sound(path):
    my_clip = mp.VideoFileClip(path)
    my_clip.audio.write_audiofile(r"keyword\my_result.wav")