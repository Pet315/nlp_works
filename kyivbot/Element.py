import re
import openpyxl
from kyivbot.View import View
from kyivbot.resources import messages


class Element:
    def __init__(self, element, file_name, column_name='A', additional_cn=''):
        self.element = element
        self.file_name = file_name
        self.column_name = column_name
        self.first_row_number = 2
        self.additional_cn = additional_cn  # additional_column_name

    def find_param(self):  # введення району/вулиці/місцевості та його/її пошук
        while 1:
            element = self.element.lower()
            element = View.check_sort(element, 'З')  # вулиця => вулицю (переведення у знахідний відмінок)
            View.output('Введіть ' + element + ': ')
            user_element = input()
            if self.element == messages.param_names_ukr[1]:
                user_element = View.check_sort(user_element, 'Р', True)  # Григоренко => Григоренка (переведення у родовий відмінок)
            found_element = self.use_excel_data(user_element)[0]

            if user_element != found_element:
                if found_element == ' не знайдено':
                    View.output(self.element + found_element)
                else:
                    View.output('Ви мали на увазі: ' + found_element + "? ")
                    district_check = input()
                    if re.search('так', district_check):
                        element = View.first_letter_upper(element)
                        View.output(element + ' зафіксовано')
                        return found_element
                View.output('Бажаєте спробувати ще раз?')
                district_check = input()
                if re.search('так', district_check):
                    continue
                return ' не знайдено'
            element = View.first_letter_upper(element)
            View.output(element + ' зафіксовано')
            return found_element

    def find_object_nearby(self, user_element, file_name, column_name='A'):  # введення і пошук об'єкту поблизу
        self.file_name = file_name
        self.column_name = column_name
        user_element_list = user_element.split(' ')
        user_element = ''
        for i in range(len(user_element_list) - 1):
            user_element += user_element_list[i]
            if i<len(user_element_list) - 2:
                user_element += ' '
        found_elements = self.use_excel_data(user_element)
        # return ['']
        return found_elements

    def use_excel_data(self, user_element):  # пошук необхідного елементу в БД
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
            if len(user_element) > 0:
                if re.search(user_element, ed_element_lower):
                    if self.additional_cn == '':
                        found_elements.append(ed_element)
                    else:
                        found_elements.append(str(excel_data[self.additional_cn + str(i)].value))
            i += 1
        # print(found_elements)
        if len(found_elements) == 0:
            return [' не знайдено']
        found_elements.append(excel_data[self.column_name + '1'].value)
        return found_elements
