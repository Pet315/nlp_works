from kyivbot.Element import Element
from kyivbot.View import View
from kyivbot.resources import messages


def run():
    view = View()
    print(messages.greeting)
    while 1:
        view.output(messages.main_menu)
        way = view.input(['1', '2', '3'], 'Введіть 1, 2 або 3') # перший, перше => LEMMA/POS
        if way == '1':
            view.output(messages.choose_output_method)
            output_method = view.input(['1', '2'], 'Введіть 1 або 2')
            view = View(output_method)
        else:
            view.output(messages.params)
            params = get_params(view)
            streets = params[0]
            element = params[1]
            if streets[0] == ' не знайдено':
                continue
            view.output(messages.objects_nearby)
            get_objects_nearby(view, streets, element)


def get_params(view):  # визначення вулиці, або списку вулиць за вибраним районом/місцевістю
    way = view.input(['1', '2', '3'], 'Введіть 1, 2 або 3')
    streets = []
    if way == '1':
        element = Element(messages.param_names_ukr[0], messages.param_names[0])
        district = element.find_param()
        element2 = Element(messages.param_names_ukr[3], messages.param_names[1], 'B', 'A')
        streets = element2.use_excel_data(district)
        streets[len(streets) - 1] = district
        # print(streets)
    elif way == '2':
        element = Element(messages.param_names_ukr[1], messages.param_names[1])
        streets.append(element.find_param())
    else:
        element = Element(messages.param_names_ukr[2], messages.param_names[2], 'E')
        locality = element.find_param()
        element2 = Element(messages.param_names_ukr[4], messages.param_names[2], 'E', 'A')
        streets = element2.use_excel_data(locality)
        streets[len(streets) - 1] = locality
    return [streets, element]


def get_objects_nearby(view, streets, element):  # визначення об'єктів розташованих на вулиці/вулицях
    vars = ['1', '2', '3', '4', '5', '6']
    way = view.input(vars, 'Введіть 1, 2, 3, 4, 5, або 6')
    type = []
    objs_list = []
    j = 0
    for i in range(len(messages.onb_type_names)):
        # if way == vars[j] or way == vars[j + 1]:
        if way == i+1:
            type = messages.onb_type_names[i]  # objects_nearby_type_names
            objs_list = messages.onb_types[i]  # objects_nearby_types
        j += 2
    nothing = True
    for i in range(len(objs_list)):
        for j in range(len(streets)):
            objects_nearby = element.find_object_nearby(streets[j], type + objs_list[i])
            if objects_nearby[0] != ' не знайдено' and nothing:
                if len(objects_nearby) != 0:
                    nothing = False
            for k in range(len(objects_nearby) - 1):
                view.output(objects_nearby[k])
    if nothing:
        way = int(way)-1
        onb_type_name_parts = messages.onb_type_names_ukr[way].split(' ')
        onb_type_name = ''
        for i in range(len(onb_type_name_parts)):
            onb_type_name += View.check_sort(onb_type_name_parts[i], 'Р')  # Банкомат => Банкомата (переведення у родовий відмінок)
            if i == 0:
                onb_type_name = View.first_letter_upper(onb_type_name)
            if i != len(onb_type_name_parts)-1:
                onb_type_name += ' '
        view.output(onb_type_name + ' не знайдено')


if __name__ == "__main__":
    run()  # запуск бота
