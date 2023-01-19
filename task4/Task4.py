import sqlite3
from task4 import gr_fields


class Task4:
    def __init__(self, db_name='dict_ua.db'):
        self.words = None
        self.sqlite_connection = self.connect_db(db_name)
        self.cursor = self.sqlite_connection.cursor()

    def connect_db(self, db_name):
        try:
            return sqlite3.connect(db_name)
        except sqlite3.Error as error:
            print("Error: ", error)

    def close(self):
        if self.sqlite_connection:
            self.sqlite_connection.close()

    def find_words(self, word):
        s = """SELECT accent, fk_inf, fid from wf where wf=?"""
        self.cursor.execute(s, (word,))
        data = self.cursor.fetchall()

        self.words = {}
        i=1
        for data_el in data:
            self.words.update({data_el[0] + ' ' + str(i): [data_el[1], data_el[2], '']})
            i+=1
        return self.words

    def find_lemmas(self):
        lemmas = {}
        values = self.words.values()
        for value in values:
            s = """SELECT accent from wf where fk_inf=? order by fid"""
            self.cursor.execute(s, (value[0],))
            data = self.cursor.fetchone()[0]

            fid = value[1].rsplit('_')
            new_fid = fid[0] + '_1'
            value = [value[0], new_fid, 'лема']
            lemmas.update({data: value})

        self.words.update(lemmas)
        return self.words

    def short_description(self):
        short_descs = {}
        values = list(self.words.values())
        keys = list(self.words.keys())

        self.close()
        self.__init__('mph_ua.db')

        for i in range(len(values)):
            fid = values[i][1].rsplit('_')
            s = """SELECT com, gr_id from parts where id=?"""
            self.cursor.execute(s, (fid[0],))
            data = self.cursor.fetchone()

            new_value = [data[0], data[1], int(fid[1]), values[i][2]]
            short_descs.update({keys[i]: new_value})
        self.words = short_descs
        return self.words

    def full_description(self):
        full_descs = {}
        values = list(self.words.values())
        keys = list(self.words.keys())
        for i in range(len(self.words)):
            field = values[i][2] + 3
            s = """SELECT {table} from gr where id=?"""
            self.cursor.execute(s.format(table='field'+str(field)), (values[i][1],))
            data = self.cursor.fetchone()[0]

            data = data.split(' ')
            if len(data[0]) == 1:
                for j in range(len(gr_fields.sorts)):
                    if data[0] == gr_fields.sorts_first_letter[j]:
                        data[0] = gr_fields.sorts[j]
                for j in range(len(gr_fields.numbers)):
                    if data[1] == gr_fields.numbers_first_letter[j]:
                        data[1] = gr_fields.numbers[j]
                data = ' - ' + data[0] + ' відмінок, ' + data[1]
            else:
                data = ''

            new_value = [values[i][0], data, values[i][3]]
            full_descs.update({keys[i]: new_value})
        self.words = full_descs
        return self.words

    def get_words(self, type=''):
        words = ""
        values = list(self.words.values())
        keys = list(self.words.keys())
        number = 0
        for i in range(len(values)):
            if values[i][2] == type:
                number += 1
                key = keys[i].split(' ')
                words += '\t' + str(number) + ') ' + key[0] + ' - ' + values[i][0] + values[i][1] + '\n'
        return words

def main(word):
    a = Task4()
    print("---\nPOS tagging and word lemmatization: " + word)

    print("\n---\n1. The process of filling a dictionary with words")
    print('\t', a.find_words(word))  # {wf_accent_1: [wf_fk_inf_1, wf_fid_1, ''], ...}
    print('\t', a.find_lemmas())  # {..., wf_accent_l1: [wf_fk_inf_l1, wf_fid_l1, 'лема'], ...}
    print('\t', a.short_description())  # {wf_accent_1: [parts_com_1, parts_gr_id_1, fid_second_part_1, ''], ...}
    print('\t', a.full_description())  # {wf_accent_1: [parts_com_1, gr_field_1], ...}

    print("\n---\n2. Lemmas")
    print(a.get_words('лема'))

    print("---\n3. POS tags")
    print(a.get_words())

    a.close()


if __name__ == "__main__":
    main('мала')
    main('верби')
