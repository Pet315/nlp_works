from Task2_2 import Task2_2


class Task2_1:
    def __init__(self):
        self.sqlite_connection = Task2_2.connect_db()
        self.cursor = self.sqlite_connection.cursor()

    def close(self):
        if (self.sqlite_connection):
            self.sqlite_connection.close()
            # print('sqlite connection closed')

    def lemma(self, word):
        wf = Task2_2.lemma(self.cursor, word)[0]
        return wf[0]

    def taging(self, word):
        wf = Task2_2.lemma(self.cursor, word)[0]
        fid_structure = Task2_2.lemma(self.cursor, word)[1]

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

        sqlite_connection1 = Task2_2.connect_db('mph_ua.db')
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
    a = Task2_1()

    # Лематизація
    print(a.lemma('руками'))

    # POS-тегування
    print(a.taging('сумці'))

    a.close()