import re
import pyttsx3
import openpyxl

from kyivbot.data import messages


class Main:
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

    def input(self, output_method, vars=None, repeat_message=''):
        if vars is None:
            vars = []
        value = input()
        value = str(value)
        value = value.lower()
        while 1:
            for var_i in vars:
                if value == var_i:
                    return value
            self.output(repeat_message, output_method)
            value = input()
            value = str(value)
            value = value.lower()

    def use_excel_data(self, file_name, user_element, column_name, first_row_number, additional_cn=None):
        user_element = user_element.lower()
        wb = openpyxl.reader.excel.load_workbook(filename='data/' + file_name + '.xlsx', data_only=True)
        wb.active = 0
        excel_data = wb.active
        i = first_row_number
        while 1:
            if excel_data[column_name + str(i)].value == None:
                return 'Не знайдено'
            ed_element = str(excel_data[column_name + str(i)].value)
            ed_element_lower = ed_element.lower()
            if re.search(user_element, ed_element_lower):
                ede_additional = ''
                if additional_cn is not None:
                    ede_additional = str(excel_data[additional_cn + str(i)].value)
                return ede_additional + ' ' + ed_element
            i += 1


def main():
    output_method = 1
    program = Main()
    print(messages.greeting)
    while 1:
        program.output(messages.main_menu, output_method)
        way = program.input(output_method, ['1', 'один', '2', 'два'], 'Введіть 1 або 2')
        if way == '1' or way == 'один':
            program.output(messages.output_method, output_method)
            output_method = program.input(output_method, ['1', 'один', "2", "два"], 'Введіть 1 або 2')
            txt = 'Обрано метод: ' + str(output_method)
            program.output(txt, output_method)
        else:
            program.output(messages.params, output_method)
            way = program.input(output_method, ['1', 'один', '2', 'два', '3', 'три', '4', 'чотири'],
                                'Введіть 1, 2, 3 або 4')
            param = ''
            column_name = 'A'
            file_name = 'districts'
            first_row_number = 2
            additional_cn = None
            if way == '1' or way == 'один':
                param = 'берег Дніпра'
                column_name = 'G'
            if way == '2' or way == 'два':
                param = 'район'
            if way == '3' or way == 'три':
                param = 'місцевість у районі'
                column_name = 'E'
                file_name = 'streets'
            if way == '4' or way == 'чотири':
                param = 'вулиця'
                file_name = 'streets'
                additional_cn = 'B'

            while 1:
                program.output('Введіть ' + param + ': ', output_method)
                user_district = input()
                found_district = program.use_excel_data(file_name, user_district, column_name, first_row_number, additional_cn)
                if user_district != found_district:
                    if found_district == 'Не знайдено':
                        # found_district = param + " " + found_district # USE POS!!!
                        program.output(found_district, output_method)
                        break
                    txt = 'Ви мали на увазі: ' + found_district + "? "
                    program.output(txt, output_method)
                    district_check = input()
                    if not re.search('так', district_check):
                        continue
                program.output(param + ' зафіксовано', output_method) # USE POS!!!
                break


if __name__ == "__main__":
    main()