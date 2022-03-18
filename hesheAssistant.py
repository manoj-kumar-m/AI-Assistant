from urllib import request
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import sys
import requests
from bs4 import BeautifulSoup
import pywhatkit
import pyautogui
import keyboard
import pyjokes
from PyDictionary import PyDictionary as Dic

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 190)


def speak(audio):
    print("   ")
    print(f"--> {audio}")
    engine.say(audio)
    print("    ")
    engine.runAndWait()

# ----------------------------- initialization ----------------------------
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Hishee. I am Your Assistant, how may I help You?")

# --------------------------- takes user command ---------------------------------------
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...\n")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...\n")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")

    except Exception as e:
        # print(e)
        print("Say that again please...\n")
        return takeCommand()
    return query.lower()


def Assistant():
    if 1:
        query = takeCommand()
        if 'hello' in query:
            speak("Hello Sir , I Am  HiShee.")
            speak("Your Personal AI Assistant!")
            speak("How May I Help You?")
            Assistant()

        elif 'how are you' in query:
            speak("I Am Fine Sir!")
            speak("Whats About YOU?")
            x = takeCommand()
            speak("Ok")
            speak("How May I Help You?")
            Assistant()

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            # print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Ok")
            speak("")
            speak("Opening Youtube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Ok")
            speak("")
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'E:\\songs'
            songs = os.listdir(music_dir)
            x = random.randint(1, 188)
            os.startfile(os.path.join(music_dir, songs[x]))
            speak("your song has been started !")

        elif 'dictionary' or 'meaning' or 'synonym' or 'antonym' in query:
            # Dict(query)
            Dict()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'repeat my words' in query:
            speak("Speak sir!")
            w = takeCommand()
            speak(f"{w}")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'youtube tool' in query:
            YoutubeAutomation()

        elif 'email to' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "exemail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

        elif 'weather' in query:
            speak("tell the city name")
            name = takeCommand().lower()
            Weather(name)

        elif 'message' in query:
            Whatsappmsg()

        elif 'screenshot' in query:
            ss = pyautogui.screenshot()
            ss.save('C:\\Users\\hp\\Pictures\\Screenshots\\img1.png')
            speak('Screenshot has been saved')

        elif 'close' in query:
            query = query.replace('the app', '')
            query = query.replace('close', '')
            CloseApps(query)


        elif 'thank you' in query:
            speak("You are Welcome!")

        elif 'search' or 'open' in query:
            if 'youtube' and 'the app' not in query:
                speak("ok")
                query = query.replace("search ", "")
                query = query.replace("open ", "")
                pywhatkit.search(query)
                speak("That's what I found for Your search ")
            elif 'the app' in query:
                query = query.replace('the app', '')
                query = query.replace('open', '')
                OpenApps(query)

            elif 'youtube search' or 'in youtube' in query:
                speak("ok")
                query = query.replace("youtube search ", "")
                query = query.replace("in youtube", "")
                query = query.replace("search", "")
                query = query.replace("open ", "")
                url = 'https://www.youtube.com/results?search_query='+query
                webbrowser.open(url)
                speak("That's what I found for Your search ")

            elif 'website' or '.com':
                speak("ok")
                query = query.replace("website ", "")
                query = query.replace("open ", "")
                query = query.replace(".com ", "")
                url = 'https://www.' + query + '.com'
                webbrowser.open(url)
        else:
            Assistant()
    

def Weather(loc):
    city = loc
    search = 'temperature in ' + city
    url = f'https://www.google.com/search?q={search}'
    r = requests.get(url)
    data = BeautifulSoup(r.text, 'html.parser')
    temp = data.find('div', class_='BNeawe').text
    speak(f'current {search} is {temp}')


def Whatsappmsg():
    speak("Tell me the name of the person ")
    name = takeCommand().lower()
    if 'sundeep' in name:
        speak('Tell me the message ')
        msg = takeCommand().lower()
        speak('Tell me the time of sending')
        speak('Time in hour ')
        hr = int(takeCommand())
        speak('Time in minutes ')
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+918088691117", msg, hr, min, 20)
        speak('OK, sending the message to sundeep')
    elif 'hrithik' in name:
        speak('Tell me the message ')
        msg = takeCommand()
        speak('Tell me the time of sending')
        speak('Time in hour ')
        hr = int(takeCommand())
        speak('Time in minutes ')
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+918904824329", msg, hr, min, 20)
        speak('OK, sending the message to hrithik')
    elif 'manoj' in name:
        speak('Tell me the message ')
        msg = takeCommand()
        speak('Tell me the time of sending')
        speak('Time in hour ')
        hr = int(takeCommand())
        speak('Time in minutes ')
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+919353521077", msg, hr, min, 20)
        speak('OK, sending the message to manoj')


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


def CloseApps(query):
    if 'msword' in query:
        os.system("TASKKILL /f /im WINWORD.EXE")
        speak('OK, closing the ms word')
    elif 'sublime' in query:
        os.system("TASKKILL /f /im sublime_text.exe")
        speak('OK, closing the sublimetext')


def OpenApps(query):
    if 'msword' in query:
        os.startfile(
            "C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE")
        speak('OK, opening the ms word')
    elif 'sublime' in query:
        os.startfile("C:\Program Files\Sublime Text 3\sublime_text.exe")
        speak('OK, opening the sublimetext')


def YoutubeAutomation():
    com = takeCommand()
    if 'pause' in com:
        keyboard.press('space bar')
    elif 'restart' in com:
        keyboard.press('0')
    elif 'mute' in com:
        keyboard.press('m')
    elif 'skip' in com:
        keyboard.press('l')
    elif 'fullscreen' in com:
        keyboard.press('f')
    elif 'film mode' in com:
        keyboard.press('t')
    elif 'back' in com:
        keyboard.press('j')


def Dict():
    word = takeCommand().lower()
    if 'meaning' in word:
        word = word.replace('what is the meaning of', '')
        word = word.replace('meaning of', '')
        res = Dic.meaning(word)
        speak(f"The meaning of {word} is {res}")
    elif 'synonym' in word:
        word = word.replace('what is the synonym of', '')
        word = word.replace('synonym of', '')
        res = Dic.synonym(word)
        speak(f"The synonym of {word} is {res}")
    elif 'antonym' in word:
        word = word.replace('what is the antonym of', '')
        word = word.replace('antonym of', '')
        res = Dic.antonym(word)
        speak(f"The antonym of {word} is {res}")


if __name__ == "__main__":
    wishMe()
    Assistant()
