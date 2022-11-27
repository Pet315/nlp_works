import re
import openpyxl

from kyivbot.View import View


class Element:
    def __init__(self, element, file_name, column_name='A', first_row_number=2):
        self.element = element
        self.file_name = file_name
        self.column_name = column_name
        self.first_row_number = first_row_number

    def use_excel_data(self, user_element):
        user_element = user_element.lower()

        workbook = openpyxl.reader.excel.load_workbook(filename='resources/' + self.file_name + '.xlsx', data_only=True)
        workbook.active = 0
        excel_data = workbook.active
        i = self.first_row_number
        found_elements = []
        while excel_data[self.column_name + str(i)].value is not None:
            ed_element = str(excel_data[self.column_name + str(i)].value)  # excel_data_element
            ed_element_lower = ed_element.lower()  # excel_data_element_lower
            # print(ed_element_lower + '15')
            # print(user_element + '15')
            if re.search(user_element, ed_element_lower):
                found_elements.append(ed_element)
            i += 1
        if len(found_elements) == 0:
            return [' не знайдено']
        found_elements.append(excel_data[self.column_name + '1'].value)
        return found_elements

    def define_param(self):
        while 1:
            if self.element.find(' ') != -1:  # Берег Дніпра => берег Дніпра
                element = self.element.split(' ')
                element = element[0].lower() + ' ' + element[1]
            else:  # Район => район
                element = self.element.lower()
            View.output('Введіть ' + element + ': ')
            user_element = input()
            found_element = self.use_excel_data(user_element)[0]

            if user_element != found_element:
                if found_element == ' не знайдено':
                    View.output(self.element + found_element)
                else:
                    View.output('Ви мали на увазі: ' + found_element + "? ")
                    district_check = input()
                    if re.search('так', district_check):
                        View.output(self.element + ' зафіксовано')
                        return found_element
                View.output('Бажаєте спробувати ще раз?')
                district_check = input()
                if re.search('так', district_check):
                    continue
                return ' не знайдено'
            View.output(self.element + ' зафіксовано')
            return found_element

    def define_obj_nearby(self, user_element, file_name, column_name='A'):
        self.file_name = file_name
        self.column_name = column_name

        user_element_list = user_element.split(' ')
        user_element = ''
        for i in range(len(user_element_list) - 1):
            user_element += user_element_list[i]
            if i<len(user_element_list) - 2:
                user_element += ' '
        found_elements = self.use_excel_data(user_element)
        return found_elements
