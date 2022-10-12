import sqlite3


class Addition:
    @staticmethod
    def connect_db(db_name='dict_ua.db'):
        try:
            return sqlite3.connect(db_name)
        except sqlite3.Error as error:
            print("Error: ", error)

    @staticmethod
    def lemma(cursor, word):
        sqlite_select_query = """SELECT fk_inf,fid from wf where wf=?"""
        cursor.execute(sqlite_select_query, (word,))
        data = cursor.fetchone()
        fid_structure = data[1].rsplit('_')

        new_fid = fid_structure[0] + '_1'
        sqlite_select_query = """SELECT wf from wf where fk_inf=? and fid=?"""
        cursor.execute(sqlite_select_query, (data[0], new_fid))
        return [cursor.fetchone(), fid_structure]