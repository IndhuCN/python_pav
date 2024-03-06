import pyttsx3, datetime, os, random, requests
import wikipedia, webbrowser, sys, pywhatkit
import speech_recognition as sr

engine = pyttsx3.init('sapi5')  # Initialize pyttsx3 with the 'sapi5' driver
voices = engine.getProperty("voices") # Get the list of available voices
engine.setProperty('voice', voices[1].id) # setting value to male or female


# To convert text into voice
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# To convert voice into text
def takecommand():
    r = sr.Recognizer() # speech recognizer
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception:
        speak("Can you please say that again ... ")
        return 'none'
    return query


# To wish
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning ")
    elif hour >= 12 and hour < 16:
        speak("Good afternoon ")
    elif hour >= 16 and hour < 24:
        speak("Good evening ")
    # else:
    #     speak("Good night ")
    speak("I am your personal assistant Luna. Please tell me how can i help you!")


if __name__ == "__main__":
    wish()
    if 1:
        query = takecommand().lower()

        if 'open notepad' in query:
            npath = 'C:\\Windows\\System32\\notepad.exe'
            os.startfile(npath)
            speak("Please wait ! While I am opening notepad for you!")

        elif "open cmd" in query:
            os.system('start cmd')
            speak("Opening Command Promte")

        elif "play music" in query:
            music_dir = 'D:\\Songs'
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))  # connecting to the song from D file
            speak("Playing Music")

        elif "ip address" in query:
            ip = requests.get("https://api.ipify.org").text
            speak(f"Your Ip address is {ip}")

        elif 'wikipedia' in query:
            speak("Searching in wikipedia")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak(f"according to wikipedia {results}")

        elif "open youtube" in query:
            webbrowser.open('www.youtube.com/')

        elif "open instagram" in query:
            webbrowser.open('www.instagram.com/')

        elif "open facebook" in query:
            webbrowser.open('www.facebook.com/')

        elif "open twitter" in query:
            webbrowser.open('www.twitter.com/')

        elif "open google" in query:
            speak('Hey what should i search on google ! ')
            varg = takecommand().lower()
            webbrowser.open(varg)

        elif 'play song on youtube' in query:
            speak("Which song would you like to play on youtube ? ")
            song = takecommand().lower()
            pywhatkit.playonyt(song)

        elif 'play video' in query:
            speak("Which video would you like to play on youtube ? ")
            vsong = takecommand().lower()
            pywhatkit.playonyt(vsong)

        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye dear, have a good day.')
            sys.exit()

        elif 'hello' in query:
            speak('Hello dear')

        elif 'bye' in query:
            speak('Bye dear, have a good day.')
            sys.exit()


        elif "what's up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))





##### MODULES ####

# Pyttsx3>>>Python library for text-to-speech conversion. It allows you to convert written text into spoken words

# datetime>>>In Python, datetime is a module that provides classes for manipulating dates and times.
# It allows you to work with dates, times, and time intervals, perform arithmetic operations on them, and format them as strings.

# os>>In Python, os is a built-in module that provides a way to interact with the operating system.
#It offers functions for tasks such as file and directory manipulation, process management, environment variables

#  random module is used for generating random numbers. It provides various functions for generating random integers,
# floating-point numbers, and making choices randomly from sequences like lists.

# requests library is a popular HTTP library used for making HTTP requests. It provides a simple and elegant way to
# interact with websites and web services, allowing you to send HTTP requests, handle responses, and manage sessions

# wikipedia >> Wikipedia as a website, Wikipedia API, Python libraries for Wikipedia:

# webbrowser >> In Python, the webbrowser module provides a high-level interface to display web-based documents to users. It allows you to
#  open URLs in the user's default web browser, retrieve the browser's name, and perform other simple operations related to web browsing.

# sys module provides access to some variables used or maintained by the Python interpreter and to functions that
#interact with the interpreter. It is particularly useful for accessing system-specific parameters and functions,
#  such as command-line arguments, the Python runtime environment, and the standard I/O streams.

# pywhatkit >>> PyWhatKit is a Python library that provides various functionalities to automate
# certain tasks. It allows you to perform actions such as sending WhatsApp messages, playing YouTube videos,
# searching Google, converting text to handwriting, and more, all from within your Python script.

# speech_rfecognition >>  is a library that provides speech recognition functionality, allowing you to convert spoken language into text.

