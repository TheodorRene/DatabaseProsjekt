from database import DB


class Ovelse_pa_apparat:

    def __init__(self, ovelse_id, antall_kilo=None, antall_set=None, apparat_id=None):
        '''
        Makes a table instance. If all fields are provided, the function makes a new tuple in the database.
        Otherwise, it uploads a instance based on the tuple in the table.
        '''
        self.ovelse_id = int(ovelse_id)
        self.antall_kilo = int(antall_kilo if antall_kilo else self.get_ovelse_pa_apparat_db("antall_kilo"))
        self.antall_set = int(antall_set if antall_set else self.get_ovelse_pa_apparat_db("antall_set"))
        self.apparat_id = int(apparat_id if apparat_id else self.get_ovelse_pa_apparat_db("apparat_id"))

    def get_ovelse_pa_apparat_db(self, col):
        '''
        Gets an entry in the database with self.{id_field}. Projects only the given column, given by col.
        :param col: The column to be projected
        :return: Returns single entry
        '''
        con = DB.get_connection()
        db_req= f"SELECT {col} FROM ovelse_pa_apparat WHERE ovelse_id={self.ovelse_id}"
        result = con.execute(db_req).fetchone()[0]
        return result

    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO ovelse_pa_apparat VALUES ({self.ovelse_id}, {self.antall_kilo},{self.antall_set},{self.apparat_id});"
        cursor.execute(db_req)
        con.commit()
        con.close()
