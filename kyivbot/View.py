import json
import pyttsx3


class View:
    def __init__(self, output_method='1'):
        to_json = {'output_method': output_method}
        with open('resources/output_method.json', 'w') as f:
            json.dump(to_json, f)
        method_name = 'текстовий'
        if str(output_method) == '2':
            method_name = 'голосовий'
        View.output('Спосіб виведення тексту: ' + method_name)

    @staticmethod
    def output(txt):
        print(txt)
        with open('resources/output_method.json') as f:
            dict = json.load(f)
            output_method = dict['output_method']
        if output_method == '2':
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            voice = voices[4]  # Anatol
            engine.setProperty('voice', voice.id)
            engine.say(txt)
            engine.runAndWait()

    def input(self, vars=None, repeat_message=''):
        if vars is None:
            vars = []
        value = input()
        value = str(value)
        value = value.lower()
        while 1:
            for var_i in vars:
                if value == var_i:
                    return value
            self.output(repeat_message)
            value = input()
            value = str(value)
            value = value.lower()
