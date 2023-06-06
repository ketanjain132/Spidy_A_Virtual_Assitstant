import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
from LoginDetails import password, my_gmail, destination
import smtplib

t = password
g = my_gmail
d = destination

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(g, t)
    server.sendmail(g, to, content)
    server.close()

def TaskExecution():
    speak("Welcome back Ketan sir")
    
    while True:
    # if 1:
        query = takeCommand().lower()

        if 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = d    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ketan sir. I am not able to send this email")