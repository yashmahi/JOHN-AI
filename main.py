import datetime
import webbrowser
import pyjokes
import pyttsx3
import pywhatkit
import speech_recognition as sr
import wikipedia
import smtplib
listener = sr.Recognizer()
engine = pyttsx3.init()


def talk(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good morning")
        print("Good morning")
    elif hour>=12 and hour<18:
        talk("Good Afternoon")
        print("Good Afternoon")
    else:
        talk("Good Evening")
        print("Good Evening")
    talk("I am John. How may I help you")
    print("I am John. How may I help you")


def take_command():
    #Activating microphone
    try:
        with sr.Microphone() as source:
            print('John is listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'john' in command:
                command = command.replace('john', '')
                print(command)
    except:
        pass
    return command
def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("justforcode04@gmail.com",'*******') #Enter the sender's email and password
    server.sendmail('yashmahi0404@gmail.com',to,content) #Receiver's email
    server.close()


def run_john():
    wishMe()
    # while True:
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is' + time)
    elif 'tell me about' in command:
        know = command.replace('tell me about', '')
        info = wikipedia.summary(know, 5)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(talk)
    elif 'open youtube' in command:
        webbrowser.open('https://youtube.com')
    elif 'open google' in command:
        webbrowser.open('https://google.com')
    elif 'news' in command:
        talk("Here are the latest news")
        webbrowser.open('https://news.google.co.in')
    elif 'music' in command:
        talk("I'm sure this will help you")
        webbrowser.open('https://soundcloud.com')
    elif 'search' in take_command():
        talk('Yes I can surely do it. What should I search for?')
        search = take_command()
        url = 'https://google.com/search?q=' + search
        webbrowser.open(url)
        talk('Here is What I found for' + search)
    elif "send email" in take_command():
        try:
            talk("What should I say")
            content = take_command()
            to = "mahiyash0404@gmail.com"
            sendEmail(to, content)
            talk("Email has been sent")
        except Exception as e:
            print(e)
            talk("Sorry,I am not able to send this mail")
    else:
        talk("I didn't get you please repeat again")


while True:
    run_john()
