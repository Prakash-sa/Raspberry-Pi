import pyttsx
engine = pyttsx.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
engine.say("my name is neuro")
engine.runAndWait()
