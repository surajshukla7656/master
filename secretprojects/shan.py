'''python AI program '''

# modules used

import pyttsx3
import subprocess
import wolframalpha
import json
import random
import operator
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import time
import requests
import shutil
from urllib.request import urlopen


# configuring voice using pyttx3 and linux voice library - espeak
engine =pyttsx3.init()            
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[13].id)        # configuring voice

#print(engine.getProperty('rate'))
engine.setProperty('rate',150)                   # configuring rate of speaking


# function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

# function to wish according to system time
def wishMe():

    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<12:
        speak('Good Morning Sir!')

    elif hour>=12 and hour<18:
        speak('Good Afternoon Sir !')

    else :
        speak('Good Evening Sir !')

    assname=('shan 1 point o')
    speak('I am your Assitant')
    speak(assname)


def usrname():
    speak('what should i call you sir')
    uname=takeCommand()
    speak('welcome mister')
    speak(uname)
    columns=shutil.get_terminal_size().columns

    print('###############'.center(columns))
    print('Welcome Mr.',uname.center(columns))
    print('###############'.center(columns))

    speak('how can i help you, sir')

def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:

        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)

    try :
        print('Recognizing...')
        query=r.recognize_google(audio,language='en-in')
        print(f'User said :{query}\n')

    except Exception as e:
        print(e)
        print('Unable to Recognize your voice.')
        return 'None'

    return query


if __name__=='__main__':

    clear=lambda : os.system('cls')

    # this function will clear any 
    # command before execution of this python file
    clear()

    wishMe()
    usrname()

    while True:

        query=takeCommand().lower()     
        '''all the commands said by user will be 
        stored here in 'query' and will be 
        converted to lower case for easily 
        recognition of command'''


        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace('wikipedia','')
            results=wikipedia.summary(query,sentences=3)
            speak('According to Wikipedia')
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('Here you go to Youtube\n')
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            speak('Here you go to Google')
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            speak('Here you go to Stack Over flow.Happy coding')
            webbrowser.open('stackoverflow.com')
        
        # still need development
        elif 'play music' in query:
            speak('Here you go with music')
            music_dir=''
            songs=os.listdir(music_dir)
            print(songs)
            random=os.startfile(os.path.join(music_dir,songs[1]))

        elif 'the time' in query:
            strtime=datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'Sir, the time is {strtime}')

        elif 'open opera' in query:
            codePath=r''
            os.startfile(codePath)

        elif 'how are you' in query:
            speak('I am fine,Thnk you')
            speak('How are you, Sir')

        elif 'fine' in query or 'good' in query:
            speak("It's good to know that you are fine")
        
        elif 'change my name to' in query:
            query=query.replace('change my name to ','')
            assname=query

        elif 'change name' in query:
            speak('what would you like to call me, sir')
            assname=takeCommand()
            speak('Thanks for naming me')

        elif "what's your name" in query or 'What is your name' in query:
            speak('My friends call me')
            speak(assname)
            print('My friends call me',assname)

        elif 'exit' in query:
            speak('Thanks for giving me your time')

            exit()

        elif 'who made you' in query or 'who created you' in query:
            speak('I have been created by Suraj shukla')

        elif 'joke' in query:
            speak(pyjokes.get_joke())
        
        # still need development
        elif 'calculate' in query:
            # app_id='Wolframalpha api id'
            # client=wolframalpha.Client(app_id)
            # indx=query.lower().split().index('calculate')
            # query=query.split()[indx+1:]
            # res=client.query(' '.join(query))
            # answer=next(res.results).text
            # print('The answer is '+answer)
            # speak('The answer is '+answer)\
            import main

        elif 'search' in query or 'play' in query:

            query=query.replace('search','')
            query=query.replace('play','')
            webbrowser.open(query)

        elif 'who i am' in query:
            speak('if you talk then definately you are human')

        elif 'why you came to world' in query:
            speak('Thanks to Suraj shukla . further Its a secret')

        elif 'what is love' in query:
            speak('It is 7th sense that destroy all other sense')

        elif 'who are you' in query:
            speak('I am your virtual assistant created by Suraj shukla')

        elif 'will you be my gf' in query or 'will you be my bf' in query:
            speak('i am not sure about,may be you should give me some time')

        elif 'how are you' in query:
            speak('I am fine,glad you me that')

        elif 'i love you' in query:
            speak('its hard to understand')

        elif 'who is suraj' in query:
            speak('suraj shukla is a genius who brought me to this world')

        elif 'who is vinay' in query:
            speak('vinay chutiya he')

        elif 'who is gagan' in query:
            speak('gagan is gay')


