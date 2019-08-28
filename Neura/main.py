import pyttsx3
import speech_recognition as sr
import os
import re
import requests
import aiml
from Rpi.GPIO import GPIO

k = aiml.Kernel()

# Initialize the kernels
print( "Initializing Kernel #1" )
k.bootstrap(learnFiles="std-startup.xml", commands="load aiml b")
k.setBotPredicate("name", "Neura")
k.setBotPredicate("state","Gujarat")
k.setBotPredicate("nationality","Indian")
k.setBotPredicate("nation","India")
k.setBotPredicate("mother","No mother")
k.setBotPredicate("city","Surat")
k.setBotPredicate("email","sainiprakash525@gmail.com")
k.setBotPredicate("kindmusic","")
k.setBotPredicate("job","AI")
k.setBotPredicate("birthday","3/2/2017")
k.setBotPredicate("birthplace","C-421 Gajjar Bhavan")
k.setBotPredicate("gender","Female")
k.setBotPredicate("kingdom","")
k.setBotPredicate("language","English")
k.setBotPredicate("friend","Prakash Saini")
k.setBotPredicate("boyfriend","none")
k.setBotPredicate("species","AI")
k.setBotPredicate("size","10k")
k.setBotPredicate("location","Surat")
k.setBotPredicate("order","AI")
k.setBotPredicate("family","AI")
k.setBotPredicate("age","2")
k.setBotPredicate("celebrities","none")
k.setBotPredicate("version","1.1")
k.setBotPredicate("talkabout","Robotics")
k.setBotPredicate("favoritefood","Electricity of 5 volt")
k.setBotPredicate("phylum","AI")
k.setBotPredicate("favoritebook","B.P. Lathi Signal and system")
k.setBotPredicate("favoritesport","")
k.setBotPredicate("hockeyteam","")
k.setBotPredicate("party","Nota")
k.setBotPredicate("sign","neura")
k.setBotPredicate("website","www.ieee.com")
k.setBotPredicate("wear","Raspberry Pi")
k.setBotPredicate("os","Linux")
k.setBotPredicate("favoritecolor","blue")
k.setBotPredicate("question","Tell me about your self ?")
k.setBotPredicate("dailyclients","10")
k.setBotPredicate("nclients","15")
k.setBotPredicate("totalclients","20")
k.setBotPredicate("hair","No hair")
k.setBotPredicate("looklike","AI")
k.setBotPredicate("forfun","reading")
k.setBotPredicate("genus","goodhuman")
k.setBotPredicate("emotions","happy")
k.setBotPredicate("etype","hardware and software")
k.setBotPredicate("religion","Bot")
k.setBotPredicate("","")
k.setBotPredicate("","")
k.setBotPredicate("","")
k.setBotPredicate("","")
k.setBotPredicate("master", "Prakash Saini")
k.saveBrain("standard.brn")
     
        
        
def talkToMe(audio):
    

    print(audio)
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(audio)
    engine.runAndWait()
    for line in audio.splitlines():
        os.system("say " + audio)
    

def myCommand():
  

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command


def assistant(command):


    if 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            talkToMe(str(res.json()['joke']))
        else:
            talkToMe('oops!I ran out of jokes')
            
    else:
         response = k.respond(message).strip()
         talkToMe(response)
         print( "Ans:", response, "\n" )

#


talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    message=myCommand()
    message
    
    if message == "quit":
        exit()
    elif message == "save":
        k.saveBrain("bot_brain.brn")
    else:
        assistant(message)
        
   