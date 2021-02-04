import pyttsx3
engine = pyttsx3.init("sapi5")
voice = engine.getProperty("voices")
engine.setProperty('voice',voice[0].id)  # voice[1] will give different voice. only index 1 and 2 is permitted

def speak(msg):
    engine.say(msg)
    engine.runAndWait()

name = input("Enter the name: ")
speak("    Welcome back   " + name)

