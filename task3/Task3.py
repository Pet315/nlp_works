import re
import pyttsx3
from task3.data import messages
import openpyxl


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

    def input(self, vars=None):
        if vars is None:
            vars = []
        value = input()
        value = str(value)
        value = value.lower()
        while 1:
            for var_i in vars:
                if value == var_i:
                    return value
            print('Введіть 1 або 2')
            value = input()
            value = str(value)
            value = value.lower()

    def open_excel(self):
        wb = openpyxl.reader.excel.load_workbook(filename='data/districts.xlsx', data_only=True)
        wb.active = 0
        wc = wb.active
        return wc


if __name__ == "__main__":
    output_method = 1
    process = ""
    program = Task3()
    print(data.greeting)
    while not re.search('зупинити', process) and not re.search('так', process) and not re.search('бажаю', process):
        print(data.main_menu)
        way = program.input(['1', 'один', "2", "два"])
        if way == '1' or way == 'один':
            program.output(data.output_method, output_method)
            output_method = program.input(['1', 'один', "2", "два"])
            txt = 'Обрано метод: ' + str(output_method)
            program.output(txt, output_method)
        else:
            user_district = input('Введіть район')
            wc = program.open_excel()

            for district in districts:
                if re.search(district, user_district):
                    user_district = district
                    break
            print(user_district)

        process = input(data.finish)
        process = process.lower()