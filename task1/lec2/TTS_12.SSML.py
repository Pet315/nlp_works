import tts.sapi
import tts.flags

voice = tts.sapi.Sapi()

voice.say('<PRON SYM = "h eh l ow"/>', tts.flags.SpeechVoiceSpeakFlags.IsXML.value)
voice.say('<speak version="1.0" xmlns="https://www.w3.org/2001/10/synthesis" xml:lang="en-US"><phoneme alphabet="sapi" ph="w er 1 l d"></phoneme></speak>', tts.flags.SpeechVoiceSpeakFlags.IsXML.value)

txt = """
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="uk-UA">
    <voice name="Anatol">
        Так то воно так!
    </voice>
    <voice name="Natalia">
        Але трішки не так!
    </voice>
</speak>
"""
voice.say(txt, tts.flags.SpeechVoiceSpeakFlags.IsXML.value)


