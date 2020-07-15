# Speech to text recognition using an audio file(existing file)
import speech_recognition as sr

r = sr.Recognizer()

with sr.AudioFile('E:\\Languages\\Projects\\speechtotext.wav') as source:
    audion_text = r.listen(source)

    try:

        text = r.recognize_google(audion_text)
        print("converting audio file into text")
        print(text)

    except:
        print("Could not recognize file")