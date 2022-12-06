#coded by Bisno Das
#Don't change anything and make sure that your have pass the video name with extension
import moviepy
import moviepy.editor


video = moviepy.editor.VideoFileClip("")

audio = video.audio

audio.write_audiofile('new_audio.mp3')