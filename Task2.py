import sqlite3


class Task2:
    def __init__(self):
        self.sqlite_connection = self.connect_db()
        self.cursor = self.sqlite_connection.cursor()

    def connect_db(self, db_name='dict_ua.db'):
        try:
            return sqlite3.connect(db_name)
        except sqlite3.Error as error:
            print("Error: ", error)

    def close(self):
        if (self.sqlite_connection):
            self.sqlite_connection.close()
            # print('sqlite connection closed')

    def lemma(self, word):
        sqlite_select_query = """SELECT fk_inf,fid from wf where wf=?"""
        self.cursor.execute(sqlite_select_query, (word,))
        data = self.cursor.fetchone()
        fid_structure = data[1].rsplit('_')

        new_fid = fid_structure[0] + '_1'
        sqlite_select_query = """SELECT wf from wf where fk_inf=? and fid=?"""
        self.cursor.execute(sqlite_select_query, (data[0], new_fid))
        return [self.cursor.fetchone(), fid_structure]

    def pos_tagging(self, word):
        wf = self.lemma(word)[0]
        fid_structure = self.lemma(word)[1]

        fid_tail = int(fid_structure[1])
        if fid_tail < 8:
            number = "одн"
        else:
            number = "мн"

        vidm = "Немає"
        if fid_tail == 1 or fid_tail == 8:
            vidm = "Наз"
        if fid_tail == 2 or fid_tail == 9:
            vidm = "Род"
        if fid_tail == 3 or fid_tail == 10:
            vidm = "Дав"
        if fid_tail == 4 or fid_tail == 11:
            vidm = "Знах"
        if fid_tail == 5 or fid_tail == 12:
            vidm = "Оруд"
        if fid_tail == 6 or fid_tail == 13:
            vidm = "Місц"
        if fid_tail == 7 or fid_tail == 14:
            vidm = "Клич"

        sqlite_connection1 = self.connect_db('mph_ua.db')
        cursor1 = sqlite_connection1.cursor()

        sqlite_select_query = """SELECT com,istota,rid from parts where id=?"""
        cursor1.execute(sqlite_select_query, (fid_structure[0],))
        data = cursor1.fetchone()
        cursor1.close()

        com = data[0]

        if data[1] == 1:
            istota = 'Так'
        else:
            istota = "Ні"

        if data[2] == 1:
            rid = 'Ч'
        elif data[2] == 2:
            rid = 'Ж'
        elif data[2] == 3:
            rid = 'С'
        elif data[2] == 0:
            rid = 'Немає'
        else:
            rid= "Змішаний"

        return {
            "lemma": wf[0],
            "text": word,
            "pos": com.rsplit(' ')[0],
            "feats": "істота=" + istota + " | відм=" + vidm + " | рід=" + rid + " | число=" + number
        }


if __name__ == "__main__":
    a = Task2()

    # Лематизація
    print(a.lemma('руками')[0][0])

    # POS-тегування
    print(a.pos_tagging('сумці'))

    a.close()