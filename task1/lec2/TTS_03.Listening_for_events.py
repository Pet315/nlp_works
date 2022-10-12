import pyttsx3

def onStart(name):
   print('\nstarting', name)
def onWord(name, location, length):
   print('word', name, location, length)
def onEnd(name, completed):
   print('finishing', name, completed)

engine = pyttsx3.init()
voices = engine.getProperty('voices')
voice = voices[4]  # Anatol
engine.setProperty('voice', voice.id)

engine.connect('started-utterance', onStart)
engine.connect('started-word', onWord)
engine.connect('finished-utterance', onEnd)
engine.say('Тут ми сподівались спостерігати за подіями обробки тексту.')
engine.say('Але, із-за проблем з подією "started-word" в SAPI5, нас спіткала невдача.')
engine.runAndWait()
