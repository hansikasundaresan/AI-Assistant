import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import smtplib
import webbrowser as wb
import os 
import pyautogui
import psutil
import pyjokes

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    speak("the current time is")
    Time=datetime.datetime.now().strftime("%-I:%-M")
    speak(Time)
    if datetime.datetime.now().hour > 12:
        speak('p.m.')
    else:
        speak ('a.m.')

def date():
    speak("the current date is")
    Time=datetime.datetime.now().strftime("%a %m/%d/%Y")
    speak(Time)

def wishme():
    speak("Welcome back!")
    hour=datetime.datetime.now().hour
    if hour <= 12:
        speak("Dood morning!")
    elif hour>=16:
        speak("Good evening!")
    else:
        speak("Good afternoon!")
    speak("How can I help you today?")
    
def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print("listening")
        audio = r.listen(source)

    try:
        print("Recognizing")
        query=r.recognize_google(audio, language='en-ln')
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "None"
    return query

def sendmail(to, content):
    server = smtplib.SMTP('smpt.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('emailexample@gmail.com', 'password example')
    server.sendmail('emailexample@gmail.com', to, content)
    server.close()


def screenshot():
    img=pyautogui.screenshot()
    fileName='./'+datetime.datetime.now().strftime("%m.%d.%Y-%H.%M.%S")+'.png'
    img.save(fileName)

def cpu():
    battery= psutil.sensors_battery()
    percent = str(battery.percent)
    speak("You device's battery is at ")
    speak(percent+" percent")
    usage = str(psutil.cpu_percent())
    speak("Your CPU usage is at " + usage)

def jokes():
    speak(pyjokes.get_joke())


if __name__ =="__main__":
    wishme()
    while True:
        query = takeCommand().lower()

        if "time" in query: 
            time()
        elif 'date' in query:
            date()
        elif ('wikipedia' in query) or ('information' in query):
            speak('What are you searching about specifically in a couple of words?')
            query = takeCommand().lower()
            result = wikipedia.summary(query, sentences=3)
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak("What messege do you want to send")
                content = takeCommand()
                speak('who do you want to send it to')
                to = takeCommand()
                sendmail(to, content)
            except Exception as e:
                print(e)
                speak('unable to send the email')
        elif (('log out' in query) or ('log off' in query)) and (('computer' in query) or ('laptop' in query)):
            speak('are you sure you want to log out')
            query=takeCommand().lower()
            if 'yes' in query:
                os.system("sudo shutdown -s now")
            else:
                speak("what else can i help you with today")
                continue
        elif ('shut down' in query) and (('computer' in query) or ('laptop' in query)):
            speak('are you sure you want to shutdown')
            query=takeCommand().lower()
            if 'yes' in query:
                os.system("sudo shutdown -h now")
            else:
                speak("what else can i help you with today")
                continue
        elif ('restart' in query) and (('computer' in query) or ('laptop' in query)):
            speak('are you sure you want to restart')
            query=takeCommand().lower()
            if 'yes' in query:
                os.system("sudo shutdown -r now")
            else:
                speak("what else can i help you with today")
                continue
        elif ('play' in query) and (('songs' in query) or ('music' in query)):
            wb.open_new_tab("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
        elif ("what" in query) and (('remind me' in query) or ('remember' in query)):
            remember=open('./data.txt','r')
            speak("You asked me to remind you about "+ remember.read())
        elif ("remember that" in query) or ("remind me" in query):
            speak("What would you like me to remember ")
            data=takeCommand().lower()
            speak ('you asked me to remember' +data)
            rememeber = open('./data.txt', 'w')
            rememeber.write(data)
            rememeber.close()
            speak ('What else can I help you with today?')
        elif ('take' in query) and ('screenshot' in query):
            screenshot()
            speak('Taken!')
        elif (("I" in query) or ('my'in query)) and (('battery' in query) or ('cpu usage' in query)):
            cpu()
        elif (('tell' in query) or ('say' in query)) and ('joke' in query):
            jokes()
        elif ('google' in query) or ('search' in query) or ('what' in query) or ('how' in query) or ('where' in query) or ('who' in query) or ('when' in query) or ('why' in query):
            query= query.replace("google", "")
            query= query.replace("search", "")
            wb.open_new_tab("https://www.google.com/search?q="+query)
        elif ("offline" in query) or ("quit" in query) or ("thank you" in query) or ("thanks" in query)  or ("nevermind" in query) or ("nothing" in query):
            speak("see you next time!")
            quit()
        else:
            speak('I am not able to help you with that request. Please ask me something else')

        


takeCommand()



