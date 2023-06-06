import pyttsx3 
import speech_recognition as sr
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import pyautogui as p
import sys
from LoginDetails import password, my_gmail, destination

t = password
g = my_gmail
d = destination

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am SPidy Sir. Please tell me how may I help you")       

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

def DateConverter(Query):

    Date = Query.replace(" and ","-")
    Date1 = Date.replace(" and ","-")
    Date2 = Date1.replace("and","-")
    Date3 = Date2.replace("and","-")
    Date4 = Date3.replace(" ","")

    return str(Date4)

def TaskExecution():
    p.press('esc')
    speak("Welcome back Ketan sir")
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = 'C:\\Uzds'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        
        elif "open instagram" in query:
            webbrowser.open("https://www.instagram.com/")
     
        elif "open linkedin" in query:
            webbrowser.open("https://www.linkedin.com/feed/")
   
        elif "open drive" in query:
            webbrowser.open("https://drive.google.com/drive/u/1/my-drive")
       
        elif "open meet" in query:
            webbrowser.open("https://meet.google.com/?authuser=1")

        elif "open ca" in query:
            webbrowser.open("https://meet.google.com/ggr-ukqo-bsi?authuser=2/")

        elif "open Documents" in query:
            webbrowser.open("https://docs.google.com/document/u/6/?tgif=d")
        elif "open slides" in query:
            webbrowser.open("https://docs.google.com/presentation/u/0/")
        elif "open sheet" in query:
            webbrowser.open("https://docs.google.com/spreadsheets/?authuser=0")    

        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open notepad' in query:
            codePath = "C:\\WINDOWS\\system32\\notepad.exe"
            os.startfile(codePath)
     
        elif 'open proteus' in query:
            codePath = "C:\Program Files (x86)\Labcenter Electronics\Proteus 8 Professional\BIN\PDS.EXE"
            os.startfile(codePath)
     
        elif 'open vs code' in query:
            codePath = "M:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open code' in query:
            codePath = "C:\\Users\\ketan\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
       
        elif 'top' in query:
            sys.exit()

        elif 'stop' in query:
            sys.exit()

        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = d    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry ketan sir. I am not able to send this email") 
        
        elif 'whatsapp message' in query:

            name = query.replace("whatsapp ","")
            name1 = name.replace("message ","")
            name2 = name1.replace("send ","")
            name3 = name2.replace("to ","")
            Name= str(name3)
            speak("Whats the message")
            MSG = takeCommand()
            from WhatsappAuto import WhatsappMsg
            WhatsappMsg(Name,MSG)

        elif 'call' in query:
            from WhatsappAuto import WhatsappCall
            name = query.replace("call ","")
            name1 = name.replace("to ","")
            name2 = name1.replace("jarvis ","")
            name3 = name2.replace("please, ","")
            Name= str(name3)
            WhatsappCall(Name)

        elif 'video call' in query:
            from WhatsappAuto import WhatsappVideoCall
            name = query.replace("call ","")
            name1 = name.replace("to ","")
            name2 = name1.replace("Video ","")
            name3 = name2.replace("do ","")
            Name= str(name3)
            WhatsappVideoCall(Name)

        elif 'show chat' in query:
            speak("With whom ?")
            from WhatsappAuto import WhatsappChat
            name = takeCommand()
            WhatsappChat(name)

        elif 'space news' in query:


            speak("Tell Me The Date For News Extracting Process .")

            Date = takeCommand()

            Value = DateConverter(Date)

            from nasa import NasaNews

            NasaNews(Value)

        elif 'about' in query:
            from nasa import Summary
            query1 = query.replace("jarvis ","")
            query2 = query1.replace("about ","")
            Summary(query2)

        else:

            from DataBase.ChatBot.ChatBot import ChatterBot

            reply = ChatterBot(query)

            speak(reply)

            if 'bye' in query:

                break

            elif 'exit' in query:

                break

            elif 'go' in query:

                break

if __name__ == "__main__":
    TaskExecution()