from Customer import Customer
from Intent import Intent
from Assistant import Assistant
from resources import messages


def start():
    assistant = Assistant()
    print(messages.greeting)
    while 1:
        assistant.speech(messages.how_to_help)
        way = Customer.speech(['1', '2', '3'], 'Введіть 1, 2 або 3')
        if way == '1':
            assistant.speech(messages.choose_output_method)
            output_method = Customer.speech(['1', '2'], 'Введіть 1 або 2')
            assistant = Assistant(output_method)
        elif way == '2':
            assistant.speech(messages.params)
            params = get_params()
            streets = params[0]
            element = params[1]
            if streets[0] == messages.not_understand:
                continue
            assistant.speech(messages.objects_nearby)
            get_objects_nearby(assistant, streets, element)
        else:
            print(messages.goodbye)
            break


def get_params():  # definition of a street, or a list of streets by the selected district/locality
    way = Customer.speech(['1', '2', '3'], 'Введіть 1, 2 або 3')
    streets = []
    if way == '1':
        intent = Intent(messages.param_names_ukr[0], messages.param_names[0])
        district = intent.find_param()
        intent2 = Intent(messages.param_names_ukr[3], messages.param_names[1], 'B', 'A')
        streets = intent2.use_excel_data(district)
        streets[len(streets) - 1] = district
        # print(streets)
    elif way == '2':
        intent = Intent(messages.param_names_ukr[1], messages.param_names[1])
        streets.append(intent.find_param())
    else:
        intent = Intent(messages.param_names_ukr[2], messages.param_names[2], 'E')
        locality = intent.find_param()
        intent2 = Intent(messages.param_names_ukr[4], messages.param_names[2], 'E', 'A')
        streets = intent2.use_excel_data(locality)
        streets[len(streets) - 1] = locality
    return [streets, intent]


def get_objects_nearby(assistant, streets, intent):  # identification of objects located on the street/streets
    vars = ['1', '2', '3', '4', '5', '6']
    way = Customer.speech(vars, 'Введіть 1, 2, 3, 4, 5, або 6')
    type = []
    objs_list = []
    j = 0
    for i in range(len(messages.onb_type_names)):
        # if way == vars[j] or way == vars[j + 1]:
        if int(way) == i+1:
            type = messages.onb_type_names[i]  # objects_nearby_type_names
            objs_list = messages.onb_types[i]  # objects_nearby_types
        j += 2
    nothing = True
    for i in range(len(objs_list)):
        for j in range(len(streets)):
            objects_nearby = intent.find_object_nearby(streets[j], type + objs_list[i])
            if objects_nearby[0] != messages.not_understand and nothing:
                if len(objects_nearby) != 0:
                    nothing = False
            for k in range(len(objects_nearby) - 1):
                assistant.speech(objects_nearby[k])
    if nothing:
        way = int(way)-1
        onb_type_name_parts = messages.onb_type_names_ukr[way].split(' ')
        onb_type_name = ''
        for i in range(len(onb_type_name_parts)):
            onb_type_name += assistant.check_sort(onb_type_name_parts[i], 'Р')  # Банкомат => Банкомата (transformation into genitive case)
            if i == 0:
                onb_type_name = assistant.first_letter_upper(onb_type_name)
            if i != len(onb_type_name_parts)-1:
                onb_type_name += ' '
        assistant.speech(onb_type_name + messages.not_understand)


if __name__ == "__main__":
    start()  # bot launch
