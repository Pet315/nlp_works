import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
voice = voices[4]  # Anatol

engine.setProperty('voice', voice.id)
print(voice)

txt = 'Ні слова, ні півслова' 

engine.say(txt)
engine.runAndWait()

engine.save_to_file(txt, '02_speak.mp3')
engine.runAndWait()

voice = voices[5] # Natalia
engine.setProperty('voice', voice.id)
print(voice)

txt = 'Говорить синтезатор ' + voice.name + '.'

engine.say(txt)
engine.runAndWait()


rate = engine.getProperty('rate')   # getting details of current speaking rate
print (f"Поточна швидкість = {rate} wpm (words per minute). Вона буде змінена")   #printing current voice rate
rate = 300
engine.setProperty('rate', rate)    # setting up new voice rate
print (f"Поточна швидкість = {rate} wpm")

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print ('Рівень гучності: '+str(volume)) #printing current volume level
engine.setProperty('volume',1.0)        # setting up volume level  between 0 and 1

engine.say("Вітаю увесь світ!")
engine.say('Новий навчальний рік у нас завжди починався 1 вересня.')
engine.say('Швидкість мовлення зараз: ' + str(rate) + ' wpm')
engine.say('Рівень гучності - ' + str(volume))
engine.runAndWait()
