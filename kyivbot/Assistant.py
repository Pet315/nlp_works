import sqlite3
import json
import pyttsx3
from resources import messages


class Assistant:
    def __init__(self, output_method='1'):
        to_json = {'output_method': output_method}
        with open('resources/output_method.json', 'w') as f:
            json.dump(to_json, f)
        method_name = 'текстовий'
        if str(output_method) == '2':
            method_name = 'голосовий'
        Assistant.speech('Спосіб виведення тексту: ' + method_name)

    # def __str__(self):
    #     return str(View.output('Спосіб виведення тексту: ' + self.method_name))

    @staticmethod
    def speech(txt):
        with open('resources/output_method.json') as f:
            dict = json.load(f)
            output_method = dict['output_method']
        print(txt)
        if output_method == '2':
            engine = pyttsx3.init()
            voices = engine.getProperty('voices')
            voice = voices[4]  # Anatol
            engine.setProperty('voice', voice.id)
            engine.say(txt)
            engine.runAndWait()

    @staticmethod
    def check_sort(word, new_sort='Н', surname=False):  # змінити відмінок
        sqlite_connection = Assistant.connect_dict()
        cursor = sqlite_connection.cursor()
        word = word.lower()
        if surname:
            word = Assistant.first_letter_upper(word)
        for i in range(len(messages.sorts)):
            if new_sort == messages.sorts[i]:
                new_sort = i + 1
        sqlite_select_query = """SELECT fid, fk_inf from wf where wf=?"""
        cursor.execute(sqlite_select_query, (word,))
        data = cursor.fetchone()
        if data is not None:
            sort = data[0]
            word_root = data[1]
            sort = sort.split('_')
            if sort[1] != new_sort:
                sort = sort[0] + '_' + str(new_sort)
                sqlite_select_query = """SELECT wf from wf where fid=? and fk_inf=?"""
                cursor.execute(sqlite_select_query, (sort, word_root))
                wf = cursor.fetchone()[0]
                return wf
        return word

    @staticmethod
    def connect_dict(db_name='resources/dict_ua.db'):  # підключити словник
        try:
            return sqlite3.connect(db_name)
        except sqlite3.Error as error:
            print("Error: ", error)

    @staticmethod
    def first_letter_upper(unedited_word):  # зробити великою першу літеру в рядку
        word = unedited_word[0].upper()
        for i in range(1, len(unedited_word)):
            word += unedited_word[i]
        return word