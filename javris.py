# javris.py
mport datetime
import os
import time
import webbrowser

import pyttsx3  # this module is for importing voice
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)  # setting the voice


def speak(audio):  # for speaking speech
    engine.say(audio)
    engine.runAndWait()


def greating():
    '''
    this function will great

    :return:
    '''
    speak('hello I am jarvis.')
    hour = datetime.datetime.now().hour
    if 0 <= hour <= 12:
        speak('good morning rayhan')
    elif 12 < hour <= 15:
        speak('good noon rayhan')
    elif 15 < hour <= 19:
        speak('good afternoon rayhan')
    else:
        speak('good night raihan')
    speak('how can i help you')


def jairvsListen():
    """
    use microphone to take a command and convert it into string.
    :return:
    """
    r = sr.Recognizer()
    with sr.Microphone() as sourse:
        print('listening...')
        r.adjust_for_ambient_noise(sourse)  # adjust the noise in the background
        r.dynamic_energy_threshold = 1  # time for ending listening when interval
        audio = r.listen(sourse)  # listen the audio
        try:
            text = r.recognize_google(audio, language='en-in')  # try to convert the audio file into text file



        except:
            speak('try again, I could not understand what You said')
            for i in 'Try Again!!!':
                print(i, end='')
                time.sleep(.01)
            return '!!!!'
        return text


def queryResult(text):
    if 'wikipedia' in text:
        try:
            text = text.replace('wikipedia', '')
            rst = wikipedia.summary(text, sentences=2)
        except:
            speak('can not find anything. try again')

        speak(rst)
    elif 'open youtube' in text:
        try:
            webbrowser.open('youtube.com')
        except:
            speak('can not find anything. try again')


    elif 'play song' in text:
        try:
            speak('playing from your playlist')
            webbrowser.open('https://www.youtube.com/watch?v=kMRRIMmICmM&list=PLZ_YuqSB46SP6ORhgRURFJDqazBnHqMCZ')
        except:
            speak('can not find anything. try again')

    elif 'open python' in text:
        ppath = ('C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python38-32\\python.exe')
        os.startfile(ppath)


    elif 'open word' in text:
        ppath = ("C:\\Program Files\Microsoft Office\\root\Office16\\WINWORD.EXE")
        os.startfile(ppath)
    elif 'search' in text:
        text = text.replace('search', '')

        webbrowser.open_new(f'{text}')


    elif 'the time' in text:
        time=datetime.datetime.now()
        speak(time)

    elif 'sleep' in text:
        def great():
            hour = datetime.datetime.now().hour
            if 0 <= hour <= 12:
                speak('good morning sir')
            elif 12 < hour <= 15:
                speak('good noon sir')
            elif 15 < hour <= 19:
                speak('good afternoon sir')
            else:
                speak('good night sir')

        speak(f'thanks you sir Allah Hafez ')
        great()
        return

    else:
        speak('sorry')


if __name__ == '__main__':

    while (input('press any key')) != '':
        s = jairvsListen().lower()
        print(s)
        queryResult(s)
        

