from kyivbot.Element import Element
from kyivbot.View import View
from kyivbot.resources import messages


def main():
    program = View()
    print(messages.greeting)
    while 1:
        program.output(messages.main_menu)
        way = program.input(['1', 'один', '2', 'два'], 'Введіть 1 або 2')
        if way == '1' or way == 'один':
            program.output(messages.choose_output_method)
            output_method = program.input(['1', 'один', "2", "два"], 'Введіть 1 або 2')
            program = View(output_method)
        else:
            # def params
            program.output(messages.params)
            way = program.input(['1', 'один', '2', 'два', '3', 'три', '4', 'чотири'],
                                'Введіть 1, 2, 3 або 4')
            column_name = 'A'
            file_name = 'districts'
            found_param = 'берег Дніпра'
            if way == '1' or way == 'один':
                element = Element(found_param, file_name, 'G')
                found_param = element.define_element()
            if way == '2' or way == 'два':
                element = Element('район', file_name, column_name)
                found_param = element.define_element()
            if way == '3' or way == 'три':
                element = Element('місцевість у районі', 'streets', 'E')
                found_param = element.define_element()
            if way == '4' or way == 'чотири':
                element = Element('район', file_name, column_name)
                found_district = element.define_element()
                if found_district == ' не знайдено':
                    continue
                element = Element('вулицю', 'streets', column_name, 'B', found_district, 'D')
                found_param = element.define_element()
            if found_param == ' не знайдено':
                continue

            # def objects_nearby
            program.output(messages.objects_nearby)
            way = program.input(['1', 'один', '2', 'два', '3', 'три', '4', 'чотири', '5', "п'ять"],
                                'Введіть 1, 2, 3, 4 або 5')
            found_obj = ''
            if way == '1' or way == 'один':
                element = Element(found_obj, file_name, column_name)
                found_obj = element.define_element()
            if way == '2' or way == 'два':
                pass
            if way == '3' or way == 'три':
                pass
            if way == '4' or way == 'чотири':
                pass
            if way == '5' or way == "п'ять":
                pass


if __name__ == "__main__":
    main()
