from kyivbot.Element import Element
from kyivbot.View import View
from kyivbot.resources import messages


def open_excel_file(file_name):
    workbook = openpyxl.reader.excel.load_workbook(filename='resources/' + file_name + '.xlsx', data_only=True)
    workbook.active = 0
    excel_data = workbook.active
    return excel_data


def main():
    view = View()
    print(messages.greeting)
    while 1:
        view.output(messages.main_menu)
        way = view.input(['1', 'один', '2', 'два'], 'Введіть 1 або 2')
        if way == '1' or way == 'один':  # перший, перше => LEMMA+POS
            view.output(messages.choose_output_method)
            output_method = view.input(['1', 'один', "2", "два"], 'Введіть 1 або 2')
            view = View(output_method)
        else:
            # def params
            view.output(messages.params)
            way = view.input(['1', 'один', '2', 'два', '3', 'три'],
                                'Введіть 1, 2, або 3')
            file_name = 'districts'
            streets = []
            if way == '1' or way == 'один':
                element = Element('Район', file_name)
                district = element.find_param()
                element2 = Element('Вулиці району', 'streets', 'B', 'A')
                streets = element2.use_excel_data(district)
                streets[len(streets)-1] = district
                # print(streets)
            else:
                element = Element('Вулицю', 'streets')
                streets.append(element.find_param())
            if streets[0] == ' не знайдено':
                continue

            # def objects_nearby
            view.output(messages.objects_nearby)
            vars = ['1', 'один', '2', 'два', '3', 'три', '4', 'чотири', '5', "п'ять", '6', 'шість']
            way = view.input(vars, 'Введіть 1, 2, 3, 4, 5, або 6')
            type = []
            objs_list = []
            j=0
            for i in range(len(messages.onb_type_names)):
                if way == vars[j] or way == vars[j+1]:
                    type = messages.onb_type_names[i]  # objects_nearby_type_names
                    objs_list = messages.onb_types[i]  # objects_nearby_types
                j+=2

            nothing = True
            for i in range(len(objs_list)):
                for j in range(len(streets)):
                    objects_nearby = element.find_object_nearby(streets[j], type + objs_list[i])
                    for k in range(len(objects_nearby)-1):
                        view.output(objects_nearby[k])
                    if objects_nearby[0] != ' не знайдено' and nothing:
                        if len(objects_nearby) != 0:
                            nothing = False
            if nothing:
                view.output('Не знайдено')
                # "Продуктового магазину за вулицею ... не знайдено" => LEMMA+POS!!!


if __name__ == "__main__":
    main()  # запуск бота
