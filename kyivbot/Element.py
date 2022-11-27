import re
import openpyxl

from kyivbot.View import View


class Element:
    def __init__(self, element, file_name, column_name, additional_cn=None, additional_element=None,
                       additional_element_cn=None, first_row_number=2):
        self.element = element
        self.file_name = file_name
        self.column_name = column_name
        self.additional_cn = additional_cn
        self.additional_element = additional_element
        self.additional_element_cn = additional_element_cn
        self.first_row_number = first_row_number

    def define_element(self):
        while 1:
            View.output('Введіть ' + self.element + ': ')
            user_element = input()
            found_element = self.use_excel_data(user_element)
            if user_element != found_element:
                if found_element == ' не знайдено':
                    View.output(self.element + found_element) # EDIT!!!
                else:
                    View.output('Ви мали на увазі: ' + found_element + "? ")
                    district_check = input()
                    if re.search('так', district_check):
                        View.output(self.element + ' зафіксовано')  # EDIT!!!
                        return found_element
                View.output('Бажаєте спробувати ще раз?')
                district_check = input()
                if re.search('так', district_check):
                    continue
                return ' не знайдено'
            View.output(self.element + ' зафіксовано')  # EDIT!!!
            return found_element

    def use_excel_data(self, user_element):
        user_element = user_element.lower()
        wb = openpyxl.reader.excel.load_workbook(filename='resources/' + self.file_name + '.xlsx', data_only=True)
        wb.active = 0
        excel_data = wb.active
        i = self.first_row_number
        while 1:
            if excel_data[self.column_name + str(i)].value is None:
                return ' не знайдено'
            ed_element = str(excel_data[self.column_name + str(i)].value)
            ed_element_lower = ed_element.lower()
            if self.additional_element is not None:
                if re.search(self.additional_element, excel_data[self.additional_element_cn + str(i)].value):
                    i += 1
                    continue
            if re.search(user_element, ed_element_lower):
                ede_additional = ''
                if self.additional_cn is not None:
                    ede_additional = str(excel_data[self.additional_cn + str(i)].value)
                return ede_additional + ' ' + ed_element
            i += 1
