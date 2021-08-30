print('Welcome to Alexa Project')

#part1: Take user voice as input and convert to text
#part2: Process the text and send results
#part3: Convert results to voice

#Part1 (Speech recognition)
import datetime
import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import wikipedia
import pyjokes
from Py_Weather import *

#Function to speak
def talk(answer):
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[0].id)
    engine.say(answer)
    engine.runAndWait()

def getQuestion():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Hey bro!, What's up?")
        talk("Hey bro!, What's up?")
        audio = r.listen(source)

    #Using google speech recognition
    try:
        print(r.recognize_google(audio))
        question = r.recognize_google(audio)

        if 'Alexa' in question:
            question = question.replace('Alexa', '')
            print(question)
            return question
        else:
            print("You're not talking with me. Please carry on")
            talk("You're not talking with me. Please carry on")
            return "notwithme"

    except sr.UnknownValueError:
        print("Sry, I cannot understand")
        talk("Sry, I cannot understand")


def processQuestion(question):

        if 'how are you doing' in question:
            print("I am fantastic. How can I help?")
            talk("I am fantastic. How can I help?")
            return True
        elif "what's up" in question:
            print("I am good, thank you. How can I help?")
            talk("I am good, thank you. How can I help?")
            return True
        elif "good morning" in question:
            print("Good Morning Boss, How are you?")
            talk("Good Morning Boss, How are you?")
            return True
        elif "what is today's date" in question:
            now = datetime.datetime.now()
            print(now.strftime("%Y-%m-%d %H:%M:%S"))
            talk(now.strftime("%Y-%m-%d %H:%M:%S"))
            return True
        elif "time" in question:
            time = datetime.datetime.today().time().strftime("%H:%M %p")
            print(time)
            talk(time)
            return True
        elif 'funny' in question:
            print("Honey is a good girl")
            talk("Honey is a good girl")
            return True
        elif 'Anirudh' in question:
            print("Pora pandi")
            talk("Pora pandi")
            return True
        elif 'hershey' in question:
            print("Pandi moham harshi")
            talk("Pandi moham harshi")
            return True
        elif 'Nani' in question:
            print("Rotta ASO")
            talk("Rotta ASO")
            return True
        elif 'play' in question:
            question = question.replace('play','')
            kit.playonyt(question)
            return True
        elif 'who is' in question:
            question = question.replace('who is','')
            #wiki = kit.search(question)
            wiki = wikipedia.summary(question, sentences=1)
            print(wiki)
            talk(wiki)
            return True
        elif 'joke' in question:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)
            return True
        elif 'weather' in question:
            weather = get_weather('Vijayawada')
            print(weather)
            #talk(weather)
            return True
        elif 'shut up' in question:
            print("bye bye, take care!")
            talk("bye bye, take care!")
            return False
        else:
            print("Sry, I dint get your question. Please say that again")
            talk("Sry, I dint get your question. Please say that again")
            return True


canAskQuestion = True
while canAskQuestion:
    question = getQuestion()
    if(question == "notwithme"):
        talk("Please carry on with your task, bye!")
        canAskQuestion = False
    else:
        canAskQuestion = processQuestion(question)


