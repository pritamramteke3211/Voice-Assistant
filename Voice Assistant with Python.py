import pyttsx3 as p
import speech_recognition as sr
import os
import wikipedia
import datetime
import webbrowser
import random
from selenium_web import *
import psutil ### this module used to check application (.exe) open or not
import pyaudio
import time ## use for delay time (time.sleep(2))
from News import *
import randfacts


engine = p.init()


## speed of voice(rate)
# rate = engine.getProperty('rate')  ## to  get rate of voice
engine.setProperty('rate',150)    ## to set rate of voice

"""VOICE"""
voices = engine.getProperty('voices')      #getting details of current voice
#engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


# engine.say("Hello World. My name is nova")
# engine.say("Hi, What are you doing")
def speak(word):
    engine.say(word)
    engine.runAndWait()
    return word

## Speech recongnizer
r = sr.Recognizer()

# speak("hello sir, I am your voice assistant.")
# speak("What can i do for you??")

def take_command():
    ## Select Microphone
    with sr.Microphone() as source:
        r.energy_threshold = 10000  # increase thresold of voice (if increase capture low voices)
        r.adjust_for_ambient_noise(source,1.2)


        try:
            print("Listening...")
            audio = r.listen(source) ## listening using source
            text = r.recognize_google(audio)
            print(f"User Said: {text}")

        except Exception as e:
            # print(e)
            print("Say that again please...")
            # speak("Say that again please...")
            return "None"
        return text



if __name__ == '__main__':

    program = []
    pro = 'None'
    while True:
        command = take_command().lower()
        # global program
        if  pro != 'None':
            program.append(pro)
            program1 = set(program)
            program = list(program1)

        # if 'what' and 'about' and 'you' in command:
        #     speak("I am having a good day Sir")
        #     speak("What can i do for you??")


        if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace('wikipedia', "")
            result = wikipedia.summary(command, sentences=2)
            speak("According to Wikipedia")
            print(result)
            speak(result)

        elif 'open' in command:
           speak('What you want to open')
           command = take_command().lower()
           if 'google' in command:
             webbrowser.open("http://www.google.com")  ## always use full address instead short like google

           elif 'stackoverflow' in command:
              webbrowser.open_new_tab("http://www.stackoverflow.com")

           elif 'youtube' in command:
               webbrowser.open_new_tab("http://www.youtube.com")

           elif 'code' in command:
               if 'Code.exe' in program:
                   speak("Program already open")
                   pass
               else:
                   # codePath = "C:\\Program programs\\Microsoft VS Code\\Code.exe"
                   codePath= "C:\Program Files\Microsoft VS Code\Code.exe"
                   os.startfile(codePath)
                   pro = 'Code.exe'

           elif 'notepad' in command:
               if 'notepad.exe' in program:
                   speak("Program already open")
                   pass
               else:
                   # codePath = "C:\\Program programs\\Microsoft VS Code\\Code.exe"
                   codePath= r"C:\Windows\system32\notepad.exe"
                   os.startfile(codePath)
                   pro = 'notepad.exe'

        elif 'play music' in command or 'change music' in command:
            if "vlc.exe" in [i.name() for i in psutil.process_iter()]:
                os.system(f'TASKKILL /F /IM vlc.exe')
                time.sleep(2)

            music_dir = 'D:\\Music\\Hindi Songs'
            songs = os.listdir(music_dir)
            print(songs)
            choice = random.randint(0,len(songs)-1)
            print(f"Playing.. {songs[choice]}")
            speak(f"Playing.. {songs[choice]}")
            os.startfile(os.path.join(music_dir, songs[choice]))
            pro = 'vlc.exe'

        elif 'play youtube video' in command:
            speak("Which youtube video you want to play? ")
            query = take_command().lower()
            assist = info()
            assist.get_music(query)
            pro = 'chrome.exe'


        elif 'the time' in command:
            strTime = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f"Sir, the time is {strTime}")

        elif 'information' in command:
            speak("You need information about which topic? ")
            query = take_command().lower()
            assist = info()
            assist.get_info(query)

            pro = 'chrome.exe'

        elif 'active program' in  command:
            print(program)
            speak(program)

        elif 'close' in command:
            os.system(f'TASKKILL /F /IM {program[0]}')  ## to close program
            program.remove(program[0])

        elif 'news' in command:
            speak('Sure sir, Now I will read news for you')
            arr = news()
            for j in range(len(arr)):
                print(arr[j])
                speak(arr[j])
                time.sleep(1)


        elif 'hi' in command:
            speak('Hi Sir!')

        elif 'exit' in command or 'quit' in command  or 'bye' in command :
            # speak("Thank You,for gave chance to serve You")
            speak('OK, Sir')
            speak('Have a nice day!')
            exit()









