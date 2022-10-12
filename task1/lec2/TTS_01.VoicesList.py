import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

print('\nСписок локально доступних голосів:\n')
for voice in voices:
   print(voice.name)

print('\nТой же список з доступом через індекс:\n')
for i in range(0,len(voices)):
   print(voices[i].name)
   
   
