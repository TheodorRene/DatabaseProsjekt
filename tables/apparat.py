from database import DB


class Apparat:

    def __init__(self, apparat_id, navn=None, beskrivelse=None):
        '''
        Makes a table instance. If all fields are provided, the function makes a new tuple in the database.
        Otherwise, it uploads a instance based on the tuple in the table.
        '''
        self.apparat_id = apparat_id
        self.navn = navn if navn else self.get_apparat_db("navn")
        self.beskrivelse = beskrivelse if beskrivelse else self.get_apparat_db("beskrivelse")

    def get_apparat_db(self, col):
        '''
        Gets an entry in the database with self.{id_field}. Projects only the given column, given by col.
        :param col: The column to be projected
        :return: Returns single entry
        '''
        con = DB.get_connection()
        db_req= f"SELECT {col} FROM apparat WHERE apparat_id={self.apparat_id}"
        result = con.execute(db_req).fetchone()[0]
        con.close()
        return result

    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO apparat (apparat_id,navn,beskrivelse) VALUES ({self.apparat_id},'{self.navn}','{self.beskrivelse}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
