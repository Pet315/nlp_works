import pyttsx3
import data


class Task3:
    def __init__(self):
        self.engine = pyttsx3.init()
        voices = self.engine.getProperty('voices')
        voice = voices[4]  # Anatol
        self.engine.setProperty('voice', voice.id)

    def output(self, txt, output_method):
        print(txt)
        if output_method == '2':
            self.engine.say(txt)
            self.engine.runAndWait()

    def input(self):
        value = input()
        value = str(value)
        while value != '1' and value != '2':
            print('Введіть 1 або 2')
            value = input()
            value = str(value)
        return value


if __name__ == "__main__":
    output_method = 1
    process = 0
    program = Task3()
    print(data.greeting)
    while not process:
        print(data.main_menu)
        way = program.input()
        if way == '1':
            program.output(data.output_method, output_method)
            output_method = program.input()
            txt = 'Обрано метод: ' + str(output_method)
            program.output(txt, output_method)
        else:
            program.output(data.intents, output_method)
            intent = program.input()
            txt = 'Обрано намір: ' + str(output_method)
            program.output(txt, output_method)

        process = input(data.finish)