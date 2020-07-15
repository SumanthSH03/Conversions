# Speech recognition using microphone
# importing speech_recognition module
import speech_recognition as sr

r = sr.Recognizer()

# Using microphone as source
with sr.Microphone() as source:
    print("Talk now")
    audio_text = r.listen(source)
    print("Times up")

    try:
        print("Text: "+r.recognize_google(audio_text))
# adding an exception in case the audio is not recoognized
    except:
        print("sorry, audio not recognized")
        print("Be clear while pronouncing")