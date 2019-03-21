from database import DB


class Ovelse:

    def __init__(self, ovelse_id, navn=None):
        '''
        Makes a table instance. If all fields are provided, the function makes a new tuple in the database.
        Otherwise, it uploads a instance based on the tuple in the table.
        '''
        self.ovelse_id = ovelse_id
        self.navn = navn if navn else self.get_ovelse_db("navn")

    def get_ovelse_db(self, col):
        '''
        Gets an entry in the database with self.{id_field}. Projects only the given column, given by col.
        :param col: The column to be projected
        :return: Returns single entry
        '''
        con = DB.get_connection()
        db_req = f"SELECT {col} FROM ovelse WHERE ovelse_id={self.ovelse_id}"
        result = con.execute(db_req).fetchone()[0]
        con.close()
        return result

    def save(self):
        con = DB.get_connection()
        cursor = con.cursor()
        db_req = f"INSERT INTO ovelse VALUES ({self.ovelse_id},'{self.navn}');"
        cursor.execute(db_req)
        con.commit()
        con.close()
