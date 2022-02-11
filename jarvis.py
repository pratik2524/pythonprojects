import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    pass
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<16:
        speak("good afternoon")
    elif hour>=16 and hour<20:
        speak("good evening")
    else:
        speak("good night")
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source1:
        print("Listening......")
        r.pause_threshold = 1
        audio = r.listen(source1)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said : {query}\n")
    except Exception as e:
        #print(e)
        print("say that again")
        return "none"
    return query


if __name__ == '__main__':

    wishme()
    speak(" How may I help you")
    while(True):
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("searching in wiki")
            query = query.replace("wikipedia"," ")
            results = wikipedia.summary(query,sentences = 3)
            speak("Accoding the wikipedia")
            print(results)
            speak(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strtime}")

