from threading import main_thread
from pip import main
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold =1
        audio=r.listen(source)
    
    try:
        print("Recognizing...")
        query=r.recognize_google(audio, language="en-in")
        print(f"User said:  {query}\n")
    except Exception as e:
        print("Try again!")
        return "None"
    return query

# speak("Hello world")
query = takeCommand().lower()

if 'search' in query:
    query=query.replace('search', "")
    results=wikipedia.summary(query)
    speak("According to wikipedia ")
    print(results)
    speak(results)

elif 'open ' in query:
    site= query[query.find('open')+1]
    webbrowser.open(f"{site}.com")

