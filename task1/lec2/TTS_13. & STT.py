import pyttsx3 # pyttsx3 is a text-to-speech conversion library in Python
import speech_recognition as s #Google Speech API in Python

def speech_to_text():
    sr=s.Recognizer()# an object r which recognises the voice
    with s.Microphone() as source:
        audio = sr.listen(source)
        recognized_text = sr.recognize_google(audio,language="uk-UA", show_all=True)
        print("recognized_text = '{0}'\n\n".format(recognized_text))
        print("ви сказали: '{0}'".format(recognized_text['alternative'][0]['transcript']))
    return "Було сказано: " + recognized_text['alternative'][0]['transcript']

def text_to_speech(text):
    eng= pyttsx3.init()
    voices = eng.getProperty('voices')
    voice = voices[4]
    eng.setProperty('voice', voice.id)
    eng.say(text)
    eng.runAndWait()
    
txt = speech_to_text()
text_to_speech(txt)

