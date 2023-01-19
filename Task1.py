# 1. Install libraries/modules/packages for recognition and synthesis of Ukrainian speech.
import pyttsx3
import speech_recognition


def recognition():
    recognise = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        audio = recognise.listen(source)
        recognized_text = recognise.recognize_google(audio,language="uk-UA", show_all=True)
        print("Вимовлений текст: '{0}'".format(recognized_text['alternative'][0]['transcript']))
    return 'Увага! Говорить ехо-чат-бот. Вимовлений вами текст: ' + recognized_text['alternative'][0]['transcript']


def speech(text):
    engine_object = pyttsx3.init()
    # print(engine_object)
    voices = engine_object.getProperty('voices')
    voice = voices[4] # Anatol
    engine_object.setProperty('voice', voice.id)
    engine_object.say(text)
    engine_object.runAndWait()

# 2. Install local Ukrainian voices
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print('Локально доступні голоси (встановлені + ті, що за замовчуванням):')
for voice in voices:
   print(voice.name)

# 3. A simple chatbot (echo-chatbot) with the functions of recognizing Ukrainian speech and speaking the recognized phrase.
print('---')
print('Скажіть щось...')
speech(recognition())