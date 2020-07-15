# Using the gtts module
from gtts import gTTS
import os

print("Converting the text to speech and the creating an audio file")

text = "Hello!, this is a phython program to demonstrate text to speech"
language = 'en'

speech = gTTS(text = text, lang = language, slow = False)

speech.save("E:\\Languages\\Projects\\audio.mp3")

os.system("start E:\\Languages\\Projects\\audio.mp3")

print("")