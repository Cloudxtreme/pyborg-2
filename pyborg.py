import pyttsx
import speech_recognition as sr

# initialize speech engine
engine = pyttsx.init()
engine.setProperty('rate', 70)

# create a recognizer
recognizer = sr.Recognizer()

# obtain audio from the microphone
with sr.Microphone() as source:
    print("Say something!")
    audio = recognizer.listen(source)

# recognize speech and echo
try:
    #utterance = recognizer.recognize_sphinx(audio)
    utterance = recognizer.recognize_google(audio)
    print("Did you say ", utterance, '?')
    engine.say(utterance)
    engine.runAndWait()
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Error; {0}".format(e))
