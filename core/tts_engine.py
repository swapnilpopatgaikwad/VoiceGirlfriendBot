import pyttsx3
from config.settings import VOICE_RATE, VOICE_ID

engine = pyttsx3.init()
engine.setProperty('rate', VOICE_RATE)
engine.setProperty('voice', engine.getProperty('voices')[VOICE_ID].id)

def speak(text):
    print("Bot:", text)
    engine.say(text)
    engine.runAndWait()
