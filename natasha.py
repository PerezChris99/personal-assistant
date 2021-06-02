
import pyttsx3 
import speech_recognition as sr
import datetime
import PyAudio
import wikipedia 
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning..sir, how are you doing?!")
    elif hour>=12 and hour<15:
        speak("Good Afternoon..sir, how are you doing?!")   
    else:
        speak("Good evening sir, how are you doing?")  
    speak("I am Natasha Romanoff...your personal assistant..how may i help you?")       
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.play_threshold = 10
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='english-in')
        print(f"User said: {query}\n")
    except Exception as e:
          
        print("Say that again please...")
        speak("say that again please")  
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.composemail('content', to, content) 
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'what is the time' in query:
            speak('the time is'(time))
        elif 'what is the date today' in query:
            query = r.recognize_google(audio, language='ame-in')
            speak("the date today is:f: {query}\n")
        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("https://www.youtube.com")
        
        elif 'open facebook' in query:
            speak('opening facebook')
            webbrowser.open("https://www.facebook.com")
    
        elif 'open google' in query:
            speak('opening google')
            webbrowser.open("https://www.google.com")
        elif 'open stackoverflow' in query:
            speak('opening stackoverflow')
            webbrowser.open("https://www.stackoverflow.com")   
            
        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak("Sir, the time is {strTime}")

        elif 'open gmail' in query:
            webbrowser.open("https://www.gmail.com")

