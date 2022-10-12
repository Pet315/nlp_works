import tts.sapi

voice = tts.sapi.Sapi()

voice.say("Hello")

voice.set_voice("Anatol")

voice.create_recording('output.wav', "Тут запис у wav-файл")

voice.say("Тут говоримо  в нормальному темпі")
voice.set_rate(5)
voice.say("А тут - швидко")

voice.set_volume(30)
voice.say("А тут тихо")

